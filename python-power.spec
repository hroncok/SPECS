%global commit 2cfe611348d84512a1590840a7e0d24bec1d1d93
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20121103git%{shortcommit}
Name:           python-power
Version:        1.1
Release:        0.%{snapshot}%{?dist}.2
Summary:        Cross-platform system power status information
License:        MIT
URL:            https://github.com/Kentzo/Power
Source0:        https://github.com/Kentzo/Power/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel

%description
Python module that allows you to get power and battery status of the system.

%prep
%setup -qn Power-%{commit}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
mkdir -p %{buildroot}%{python_sitelib}
cp -ar build/lib/power %{buildroot}%{python_sitelib}

%files
%doc docs/*
%{python_sitelib}/power

%changelog
* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 1.1-0.20121103git2cfe611.2
- First version
