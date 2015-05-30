%global pypi_name Fiona

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Fiona reads and writes spatial data files

License:        BSD
URL:            http://github.com/Toblerity/Fiona
Source0:        https://pypi.python.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# So user will find this with lowercase as well
Provides:       python-fiona%{?_isa} = %{version}-%{release}

BuildRequires:  gdal-devel
BuildRequires:  /usr/bin/ogrinfo

BuildRequires:  python2-devel
BuildRequires:  python-cligj
BuildRequires:  python-nose
BuildRequires:  python-six
BuildRequires:  Cython
BuildRequires:  pytest
 
BuildRequires:  python3-devel
BuildRequires:  python3-cligj
BuildRequires:  python3-nose
BuildRequires:  python3-six
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

Requires:       python-cligj
Requires:       python-six

%description
Fiona is OGR's neat, nimble, no-nonsense API for Python
programmers.
Python 2 version.

%package -n     python3-%{pypi_name}
Summary:        Fiona reads and writes spatial data files

# So user will find this with lowercase as well
Provides:       python3-fiona%{?_isa} = %{version}-%{release}


Requires:       python3-cligj
Requires:       python3-six

%description -n python3-%{pypi_name}
Fiona is OGR's neat, nimble, no-nonsense API for Python
programmers.
Python 3 version.

%prep
%setup -qn %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove shebang
sed -i '1d' fiona/fio/fio.py

rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd


%install
%{__python2} setup.py install --skip-build --root %{buildroot}
chmod 0755 %{buildroot}%{python2_sitearch}/fiona/*.so

pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
chmod 0755 %{buildroot}%{python3_sitearch}/fiona/*.so
popd

%check
export LANG=en_US.UTF-8

export PYTHONPATH=`echo build/lib.linux-*/`
mv fiona{,no} # Move the directory away so it does not import from here
nosetests --exclude test_filter_vsi --exclude test_geopackag
mv fiona{no,} # Move it back


pushd %{py3dir}
export PYTHONPATH=`echo build/lib.linux-*/`
mv fiona{,no} # Move the directory away so it does not import from here
nosetests-%{python3_version} --exclude test_filter_vsi --exclude test_geopackag
mv fiona{no,} # Move it back
popd

%files
%license LICENSE.txt CREDITS.txt
%doc README.rst CHANGES.txt docs
%{python2_sitearch}/fiona
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt CREDITS.txt
%doc README.rst CHANGES.txt docs
%{_bindir}/fio
%{python3_sitearch}/fiona
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Thu Mar 19 2015 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-1
- Initial package.
