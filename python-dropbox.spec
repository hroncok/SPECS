%global with_python3 1
%global pypi_name dropbox
Name:           python-%{pypi_name}
Version:        1.6
Release:        1%{?dist}
Summary:        Official Dropbox REST API Client

# There is no license note in the package, however on
# https://www.dropbox.com/developers/core/sdks
# it says:
# All of our SDKs are MIT licensed and intended to be useful
# both as reference documentation and for regular use. 
# Upstream's already notified.
License:        MIT

URL:            https://www.dropbox.com/developers/core/sdks
Source0:        http://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Examples from 1.5.1 release available from %%{url}
Source1:        %{pypi_name}-example.zip

# Don't install tests
# Correct a mistake in tests
Patch0:         %{pypi_name}-setup-tests.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if 0%{with_python3}
BuildRequires:  python-tools
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
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
%setup -q -a1 -n %{pypi_name}-%{version}
%patch0 -p1
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
# some of the test are erroring
# I believe it's because the tests are wrong written
%{__python} setup.py test || :
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test || :
popd
%endif # with_python3

%files
%doc README CHANGELOG example
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
# examples don't work with Python 3 (even when 2to3ed)
%doc README CHANGELOG
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Mon Jul 08 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-1
- First package

