%global with_python3 1
%global commit 2cfe611348d84512a1590840a7e0d24bec1d1d93
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20121103git%{shortcommit}
Name:           python-power
Version:        1.1
Release:        3.%{snapshot}%{?dist}
Summary:        Cross-platform system power status information
License:        MIT
URL:            https://github.com/Kentzo/Power
Source0:        https://github.com/Kentzo/Power/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python-tools
%endif

%description
Python module that allows you to get power and battery status of the system.

%if 0%{?with_python3}
%package -n python3-power
Summary:        Cross-platform system power status information

%description -n python3-power
Python module that allows you to get power and battery status of the system.
%endif # with_python3

%prep
%setup -qn Power-%{commit}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!%{__python}|#!%{__python3}|'
2to3 --write --nobackup %{py3dir}/power/tests.py
%endif # with_python3

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with_python3

%install
mkdir -p %{buildroot}%{python_sitelib}
cp -ar build/lib/power %{buildroot}%{python_sitelib}

%if 0%{?with_python3}
pushd %{py3dir}
mkdir -p %{buildroot}%{python3_sitelib}
cp -ar build/lib/power %{buildroot}%{python3_sitelib}
popd
%endif # with_python3

%files
%doc docs/*
%{python_sitelib}/power
%files -n python3-power
%doc docs/*
%{python3_sitelib}/power

%changelog
* Wed Feb 20 2013 Miro Hrončok <mhroncok@redhat.com> - 1.1-3.20121103git2cfe611
- Introduced Python 3 subpackage

* Mon Jan 14 2013 Miro Hrončok <mhroncok@redhat.com> - 1.1-2.20121103git2cfe611
- Added python-setuptools BR

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 1.1-1.20121103git2cfe611
- First version
