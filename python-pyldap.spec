# Created by pyp2rpm-1.1.2
%global pypi_name pyldap

Name:           python-%{pypi_name}
Version:        2.4.20
Release:        1%{?dist}
Summary:        An object-oriented Python API to access LDAP directory servers

License:        Python
URL:            https://github.com/pyldap/pyldap
Source0:        pyldap-2.4.20.tar.gz
Source1:        tox.ini
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel

# for tests
BuildRequires:  /usr/bin/ldapadd
BuildRequires:  /usr/bin/tox
BuildRequires:  /usr/sbin/slaptest

Requires:       openldap
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       python-setuptools

# Fedora specific patch
Patch0:         %{name}-dirs.patch

%description
pyldap provides an object-oriented API for working with LDAP within
Python programs.  It allows access to LDAP directory servers by wrapping the 
OpenLDAP 2.x libraries, and contains modules for other LDAP-related tasks 
(including processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%package -n     python3-%{pypi_name}
Summary:        An object-oriented Python 3 API to access LDAP directory servers
 
Requires:       openldap
Requires:       python3-pyasn1
Requires:       python3-pyasn1-modules
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
pyldap provides an object-oriented API for working with LDAP within
Python 3 programs.  It allows access to LDAP directory servers by wrapping the 
OpenLDAP 2.x libraries, and contains modules for other LDAP-related tasks 
(including processing LDIF, LDAPURLs, LDAPv3 schema, etc.).


%prep
%setup -qc
mv %{pypi_name}-%{version} python2

pushd python2
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%patch0 -p1
cp %{SOURCE1} .
popd

cp -a python{2,3}

find python2 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python2}|'
find python3 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'


%build
pushd python2
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
popd

pushd python3
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd


%install
pushd python2
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

pushd python3
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%check
pushd python2
LANG=en_US.UTF-8 TOXENV=py27 tox
popd

pushd python3
LANG=en_US.UTF-8 TOXENV=py%{python3_version_nodots} tox
popd

%files
%doc python2/CHANGES python2/README python2/TODO
%{python2_sitearch}/_ldap.so
%{python2_sitearch}/ldapurl.py*
%{python2_sitearch}/ldif.py*
%{python2_sitearch}/dsml.py*
%{python2_sitearch}/ldap
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info


%files -n python3-%{pypi_name}
%doc python3/CHANGES python3/README python3/TODO
%{python3_sitearch}/_ldap.cpython-??m.so
%{python3_sitearch}/ldapurl.py*
%{python3_sitearch}/ldif.py*
%{python3_sitearch}/dsml.py*
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/ldap
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Fri Jul 17 2015 Miro Hrončok <mhroncok@redhat.com> - 2.4.20-1
- Initial package.
