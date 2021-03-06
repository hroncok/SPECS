%global with_python3 1
%global pypi_name defusedxml

Name:           python-%{pypi_name}
Version:        0.4
Release:        1%{?dist}
Summary:        XML bomb protection for Python stdlib modules
License:        Python
URL:            https://bitbucket.org/tiran/defusedxml
Source0:        http://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif


%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        XML bomb protection for Python stdlib modules

%description -n python3-%{pypi_name}
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.
%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
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
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%check
%{__python} tests.py
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} tests.py
popd
%endif # with_python3

%files
%doc README.txt README.html LICENSE CHANGES.txt
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.txt README.html LICENSE CHANGES.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Tue Mar 26 2013 Miro Hrončok <mhroncok@redhat.com> - 0.4-1
- Initial package.
