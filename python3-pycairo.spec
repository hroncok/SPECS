Name:          python3-pycairo
Version:       1.10.0
Release:       1%{?dist}
License:       LGPLv3
Summary:       Python 3 bindings for the cairo library
URL:           http://cairographics.org/pycairo
Source:        http://cairographics.org/releases/pycairo-%{version}.tar.bz2

Provides:      py3cairo
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: cairo-devel

%description
Python 3 bindings for the cairo library.

%package devel
Summary:       Libraries and headers for Python 3 pycairo
Requires:      %{name} = %{version}-%{release}
Requires:      cairo-devel
Requires:      pkgconfig
Requires:      python3-devel
Provides:      py3cairo-devel

%description devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with Python 3 pycairo.

%prep
%setup -qn pycairo-%{version}

# for tests
sed -i 's/python /python3 /' test/examples_test.py

%build
export PYTHON="%{__python3}"
%{__python3} ./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__python3} ./waf build

%install
export PYTHON="%{__python3}"
%{__python3} ./waf install --destdir=%{buildroot}

%check
# now this is ugly, but I have no better idea
# the tests seem to be designed for running on installed pycairo,
# so juts copy .so and __init__ to a fake site-packages

mkdir -p site-packages/cairo
cd site-packages/cairo
ln -s ../../src/__init__.py .
ln -s ../../build_directory/src/_cairo*.so .
cd -
cd site-packages
export PYTHONPATH=`pwd`
cd -

cd test
py.test-%{python3_version}
cd -

%files
%doc AUTHORS COPYING* NEWS README
%doc examples doc/faq.rst doc/overview.rst doc/README
%{python3_sitearch}/cairo/

%files devel
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/py3cairo.pc

%changelog
* Mon Jun 30 2014 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-1
- Initial package

