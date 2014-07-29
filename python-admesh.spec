%global pypi_name admesh
%global with_python3 1

Name:           python-%{pypi_name}
Version:        0.98
Release:        1%{?dist}
Summary:        Python bindings for ADMesh, STL maipulation library

License:        GPLv2+
URL:            https://github.com/admesh/python-admesh
Source0:        https://pypi.python.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  admesh-devel >= %{version}
BuildRequires:  Cython
 
%if %{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
%endif # if with_python3


%description
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.


%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Python 3 bindings for ADMesh, STL maipulation library


%description -n python3-%{pypi_name}
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.
%endif # with_python3


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%endif # with_python3


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3


%files
%doc README.rst COPYING
%{python2_sitearch}/%{pypi_name}.so
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst COPYING
%{python3_sitearch}/%{pypi_name}.cpython-??m.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3


%changelog
* Tue Jul 29 2014 Miro Hrončok <mhroncok@redhat.com> - 0.98-1
- Initial package.
