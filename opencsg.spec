Name:           opencsg
Version:        1.3.2
Release:        1%{?dist}
Summary:        The CSG rendering library
License:        GPLv2 # Check
URL:            http://www.opencsg.org/
Source0:        http://www.opencsg.org/OpenCSG-%{version}.tar.gz
BuildRequires:  libXmu
BuildRequires:  qt-devel

%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.
OpenCSG is written in C++ and supports most modern graphics hardware.
CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by taking
the union of them, by intersecting them, or by subtracting one shape of the
other. The most basic shapes, which are not result of such a CSG operation,
are called primitives. Primitives must be solid, i.e., they must have a clearly
defined interior and exterior. By construction, a CSG shape is also solid then.

###############################################

%package        devel
Summary:        Development package of OpenCSG
License:        GPLv2 # Check

%description    devel
OpenCSG is a library that does image-based CSG rendering using OpenGL.
This is the devel package, you only need it to build software against OpenCSG.

###############################################

%prep
%setup -q -n OpenCSG-%{version}
sed -ibak s/example// opencsg.pro # examples might be broken without GLUT
# modifying makefile for 64 bit machine
%ifarch x86_64
  sed -ibak64 s/"\-lXmu"/"\-L\/usr\/lib64\/libXmu.so.6"/ src/Makefile 
%endif
# insecure rpath
sed -ibak s/" -Wl,-rpath,..\/lib"// src/Makefile
# New FSF Address, newlines
for FILE in src/*
do
  sed -ibak s/"59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"/ $FILE
  sed -i "s/\r//" $FILE
done
sed -ibak s/"59 Temple Place, Suite 330, Boston, MA  02111-1307  USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA"/ license.txt
sed -i "s/\r//" license.txt

%build
qmake-qt4
make

%install
%{__mkdir} -p %{buildroot}%{_libdir}
%{__cp} -av lib/* %{buildroot}%{_libdir}
%{__mkdir} -p %{buildroot}%{_includedir}
%{__cp} -av include/* %{buildroot}%{_includedir}

%files
%doc license.txt changelog.txt *.html img src/*.cpp src/*.h src/Makefile
%{_libdir}/*

%files devel
%doc license.txt changelog.txt *.html img src/*.cpp src/*.h src/Makefile
%{_includedir}/*

%changelog
* Sat Oct 06 2012 Miro Hrončok <miro@hroncok.cz> 1.3.2-1
- New package.
