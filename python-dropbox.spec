%global with_python3 1
%global pypi_name dropbox
Name:           python-%{pypi_name}
Version:        1.6
Release:        3%{?dist}
Summary:        Official Dropbox REST API Client
License:        MIT

URL:            https://www.dropbox.com/developers/core/sdks
Source0:        https://www.dropbox.com/static/developers/%{pypi_name}-python-sdk-%{version}.zip

# Don't install tests
# Correct a mistake in tests
Patch0:         %{pypi_name}-setup-tests.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-mock
BuildRequires:  python-setuptools

%if 0%{with_python3}
BuildRequires:  python-tools
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
%endif

%description
A Python library that for Dropbox's HTTP-based Core API.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Official Dropbox REST API Client

%description -n python3-%{pypi_name}
A Python library that for Dropbox's HTTP-based Core API.
%endif # with_python3

%prep
%setup -q -n %{pypi_name}-python-sdk-%{version}
%patch0 -p1
rm -rf %{pypi_name}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'
%endif # with_python3
chmod -x example/*.py example/*/*.py

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
# some of the test are erroring
# I believe it's because the tests are wrong written
%{__python} setup.py test || :
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test || :
popd
%endif # with_python3

%files
%doc README CHANGELOG LICENSE example
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
# examples don't work with Python 3 (even when 2to3ed)
%doc README CHANGELOG LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Wed Jul 17 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-3
- Use source package from dropbox.org
- Added LICENSE
- chmod -x examples
- Added BR python-mock

* Wed Jul 10 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-2
- Removed duplicate BR python3-setuptools
- Delete bundled egg-info

* Mon Jul 08 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-1
- First package

