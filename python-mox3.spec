# Created by pyp2rpm-1.1.1
%global pypi_name mox3

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Mock object framework for Python

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# https://bugs.launchpad.net/heat-cfntools/+bug/1403214/
Patch0:         %{name}-ismethod.patch
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-pbr >= 0.5.21
BuildRequires:  python-pbr < 1.0
BuildRequires:  python-nose
BuildRequires:  python-testrepository
 
BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 0.5.21
BuildRequires:  python3-pbr < 1.0
BuildRequires:  python3-nose
BuildRequires:  python3-testrepository


%description
Mox3 is an unofficial port of the
Google mox framework to Python 3. It was
meant to be as compatible
with mox as possible, but small enhancements have
been made.

This is Python 2 version.

%package -n     python3-%{pypi_name}
Summary:        Mock object framework for Python


%description -n python3-%{pypi_name}
Mox3 is an unofficial port of the
Google mox framework to Python 3. It was
meant to be as compatible
with mox as possible, but small enhancements have
been made.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -rf %{py3dir}
cp -a . %{py3dir}

# Only apply the patch on Python 3
pushd %{py3dir}
%patch0 -p1
popd

%build
%{__python2} setup.py build

pushd %{py3dir}
%{__python3} setup.py build
popd


%install
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests

pushd %{py3dir}
nosetests-%{python3_version}
popd

%files
%doc README.rst COPYING.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst COPYING.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue Dec 16 2014 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-1
- Initial package.
