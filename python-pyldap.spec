# Created by pyp2rpm-1.1.2
%global pypi_name pyldap

# Do not build python2 package yet, as it would collide with python-ldap
%bcond_with python2

Name:           python-%{pypi_name}
Version:        2.4.20
Release:        1%{?dist}
Summary:        An object-oriented Python API to access LDAP directory servers

License:        Python
URL:            https://github.com/%{pypi_name}/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# tox.ini from upstream git for better %%check
Source1:        https://raw.githubusercontent.com/%{pypi_name}/%{pypi_name}/%{pypi_name}-%{version}/tox.ini
 
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

%if %{with python2}
Requires:       openldap
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       python-setuptools
Provides:       python-ldap%{?_isa} = %{version}-%{release}
Provides:       python-ldap = %{version}-%{release}
#Obsoletes:      python-ldap < FIXME add specific version when python-ldap goes away
%endif

# Fedora specific patch (from python-ldap package)
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
mv %{pypi_name}-%{version} python3

pushd python3
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%patch0 -p1
cp %{SOURCE1} .
popd

# remove shebang
sed -i '1d' python3/Lib/ldap/controls/readentry.py

cp -a python{3,2}

find python2 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python2}|'
find python3 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'


%build
%if %{with python2}
pushd python2
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
popd
%endif

pushd python3
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd


%install
%if %{with python2}
pushd python2
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif

pushd python3
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%check
%if %{with python2}
pushd python2
LANG=en_US.UTF-8 TOXENV=py27 tox
popd
%endif

pushd python3
LANG=en_US.UTF-8 TOXENV=py%{python3_version_nodots} tox
popd

%if %{with python2}
%files
%doc python2/CHANGES python2/README python2/TODO
%attr(0755,root,root) %{python2_sitearch}/_ldap.so
%{python2_sitearch}/ldapurl.py*
%{python2_sitearch}/ldif.py*
%{python2_sitearch}/dsml.py*
%{python2_sitearch}/ldap
%{python2_sitearch}/%{pypi_name}-%{version}-py2.7.egg-info
%endif


%files -n python3-%{pypi_name}
%doc python3/CHANGES python3/README python3/TODO
%attr(0755,root,root) %{python3_sitearch}/_ldap.cpython-??m.so
%{python3_sitearch}/ldapurl.py*
%{python3_sitearch}/ldif.py*
%{python3_sitearch}/dsml.py*
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/ldap
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 17 2015 Miro Hrončok <mhroncok@redhat.com> - 2.4.20-1
- Initial package.
