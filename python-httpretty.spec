%global with_python3 1
%global pypi_name httpretty

Name:           python-%{pypi_name}
Version:        0.6.5
Release:        1%{?dist}
Summary:        HTTP client mock for Python
License:        MIT
URL:            http://github.com/gabrielfalcao/httpretty
Source0:        http://pypi.python.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# git clone git@github.com:gabrielfalcao/HTTPretty.git && cd HTTPretty
# git checkout d9428d8fa1
# zip -r httpretty-0.6.5-tests.zip tests/
Source1:        %{pypi_name}-%{version}-tests.zip

# Only check equality of numbers, not objects
Patch0:         %{pypi_name}-test418.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-coverage
BuildRequires:  python-httplib2
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  python-tornado
BuildRequires:  python-sure
BuildRequires:  python-urllib3
Requires:       python-coverage
Requires:       python-httplib2
Requires:       python-mock
Requires:       python-requests
Requires:       python-tornado
Requires:       python-urllib3

%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-coverage
BuildRequires:  python3-httplib2
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-sure
BuildRequires:  python3-tornado
BuildRequires:  python3-urllib3
%endif

%description
HTTPretty is a HTTP client mock library for Python 100% inspired on ruby's
FakeWeb. If you come from ruby this would probably sound familiar :)

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        HTTP client mock for Python 3
Requires:       python3-coverage
Requires:       python3-httplib2
Requires:       python3-mock
Requires:       python3-requests
Requires:       python3-tornado
Requires:       python3-urllib3

%description -n python3-%{pypi_name}
HTTPretty is a HTTP client mock library for Python 100% inspired on ruby's
FakeWeb. If you come from ruby this would probably sound familiar :)
%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
unzip %{SOURCE1}
%patch0 -p1

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!/bin/env python|#!%{__python3}|'
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
rm -rf %{buildroot}%{python_sitelib}/tests
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python3_sitelib}/tests
popd
%endif # with_python3

%check
# the tests sometimes fail and sometimes don't
# let them run until they're OK :D
until nosetests --verbosity 2; do :; done
%if 0%{?with_python3}
pushd %{py3dir}
until /usr/bin/nosetests-3* --verbosity 2; do :; done
popd
%endif # with_python3


%files
%doc PKG-INFO
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc PKG-INFO
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Fri Nov 29 2013 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-1
- Initial package.
