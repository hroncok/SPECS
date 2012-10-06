Name:           openscg
Version:        1.3.2
Release:        1%{?dist}
Summary:        The CSG rendering library
License:        GPLv2 # Check
URL:            http://www.opencsg.org/
Source0:        http://www.opencsg.org/OpenCSG-%{version}.tar.gz
BuildRequires:  libXmu
BuildRequires:  qt-devel
Requires:       libXmu

%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.
OpenCSG is written in C++ and supports most modern graphics hardware.
CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by taking
the union of them, by intersecting them, or by subtracting one shape of the
other. The most basic shapes, which are not result of such a CSG operation,
are called primitives. Primitives must be solid, i.e., they must have a clearly
defined interior and exterior. By construction, a CSG shape is also solid then.

%prep
%setup -q -n OpenCSG-%{version}
sed -ibak s/example// opencsg.pro # examples might be broken without GLUT
# modifying makefile for 64 bit machine
%ifarch x86_64
  sed -ibak64 s/"\-lXmu"/"\-L\/usr\/lib64\/libXmu.so.6"/ src/Makefile 
%endif
# insecure rpath
sed -ibak s/" -Wl,-rpath,..\/lib"// src/Makefile


%build
qmake-qt4
make

%install
%{__mkdir} -p %{buildroot}%{_libdir}
%{__cp} -av lib/* %{buildroot}%{_libdir}
%{__mkdir} -p %{buildroot}%{_includedir}
%{__cp} -av include/* %{buildroot}%{_includedir}

%files
%doc license.txt changelog.txt *.html img src/*.cpp src/*.h src/Make*
%{_libdir}/*
%{_includedir}/*

%changelog
* Sat Oct 06 2012 Miro Hrončok <miro@hroncok.cz> 1.3.2-1
- New package.
