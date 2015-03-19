%global pypi_name cligj
Name:           python-%{pypi_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Click params for GeoJSON CLI (Python 2)
License:        MIT
URL:            https://github.com/mapbox/cligj
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
 
BuildRequires:  python3-devel
 
Requires:       python-click >= 3.0

%description
Common arguments and options for GeoJSON processing commands, using Click.
Python 2 version.

%package -n     python3-%{pypi_name}
Summary:        Click params for GeoJSON CLI (Python 3)
 
Requires:       python3-click >= 3.0

%description -n python3-%{pypi_name}
Common arguments and options for GeoJSON processing commands, using Click.
Python 3 version.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# README is executable
chmod -x README.rst

rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%{__python2} setup.py build

pushd %{py3dir}
%{__python3} setup.py build
popd


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd


%files
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Thu Mar 19 2015 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-1
- Initial package.
