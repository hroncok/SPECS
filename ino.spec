Name:           ino
Version:        0.3.5
Release:        1%{?dist}
Summary:        Command line toolkit for working with Arduino hardware
# See README.rst
License:        MIT
URL:            http://inotool.org/
Source0:        http://pypi.python.org/packages/source/i/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-jinja2 pyserial python-configobj python-ordereddict
Requires:       arduino-core

%description
Ino is a command line toolkit for working with Arduino hardware.

It allows you to:
Quickly create new projects
Build a firmware from multiple source files and libraries
Upload the firmware to a device
Perform serial communication with a device (aka serial monitor)

Ino may replace Arduino IDE UI if you prefer to work with command line and
an editor of your choice or if you want to integrate Arduino build process
to third party IDE.

Ino is based on make to perform builds. However Makefiles are generated
automatically and you'll never see them if you don't want to.

%prep
%setup -q
sed -i 's|/usr/bin/env python|/usr/bin/python|' ino/runner.py
rm -f ino/templates/*/lib/.holder

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
chmod +x %{buildroot}%{python_sitelib}/%{name}/runner.py

%files
%doc README.rst MIT-LICENSE.txt
%{_bindir}/%{name}
%{python_sitelib}/%{name}*

%changelog
* Tue Jan 29 2013 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-1
- New version with license file
- Removed empty hidden files
- Require arduino -> arduino-core

* Sun Jan 27 2013 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-1
- Started
