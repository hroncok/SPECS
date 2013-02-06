%global pypi_name MultipartPostHandler2
Name:           python-%{pypi_name}
Version:        0.1.1
Release:        1%{?dist}
Summary:        A handler for urllib2 to enable multipart form uploading
# License note in MultipartPostHandler.py
License:        LGPLv2+
URL:            http://pypi.python.org/pypi/%{pypi_name}/0.1.1
Source0:        http://pypi.python.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel

%description
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf doc # no real doc there

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}
chmod +x %{buildroot}%{python_sitelib}/MultipartPostHandler.py

%files
%doc README.txt
%{python_sitelib}/MultipartPostHandler*

%changelog
* Fri Jan 25 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Created by pyp2rpm-0.5.1
- Revised
