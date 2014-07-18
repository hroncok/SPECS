Name:           python3-openid
Version:        3.0.4
Release:        1%{?dist}
Summary:        Python 3 OpenID support for servers and consumers
License:        ASL 2.0
URL:            https://github.com/necaris/python3-openid
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This is a set of Python packages to support use of the OpenID decentralized
identity system in your application. Want to enable single sign-on for your
web site? Use the openid.consumer package. Want to run your own OpenID server?
Check out openid.server. Includes example code and support for a variety of
storage back-ends.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%check
%{__python3} -m unittest openid.test.test_suite

%files
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Mar 26 2014 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-1
- First package

