%global with_python3 1
Name:           python-social-auth
Version:        0.1.22
Release:        1%{?dist}
Summary:        Social authentication/registration mechanism for Python frameworks
License:        BSD
URL:            http://psa.matiasaguirre.net/
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-oauthlib
BuildRequires:  python-openid
BuildRequires:  python-requests
BuildRequires:  python-requests-oauthlib
BuildRequires:  python-setuptools
BuildRequires:  python-six

Requires:       python-oauthlib
Requires:       python-openid
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-six


%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-oauthlib
BuildRequires:  python3-openid
BuildRequires:  python3-requests
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%endif

%description
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

Crafted using base code from django-social-auth, implements a common interface
to define new authentication providers from third parties. And to bring support
for more frameworks and ORMs.

%if 0%{?with_python3}
%package -n python3-social-auth
Summary:        Social authentication/registration mechanism for Python 3 frameworks
Requires:       python3-oauthlib
Requires:       python3-openid
Requires:       python3-requests
Requires:       python3-requests-oauthlib
Requires:       python3-six

%description -n python3-social-auth
A Python library that for Dropbox's HTTP-based Core API.
%endif # with_python3

%prep
%setup -q

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'
%endif # with_python3

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%{__python} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%check
%{__python} setup.py test
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif # with_python3

%files
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-social-auth
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Fri Mar 21 2014 Miro Hrončok <mhroncok@redhat.com> - 0.1.22-1
- First package

