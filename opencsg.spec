Name:           opencsg
Version:        1.3.2
Release:        6%{?dist}
Summary:        Library for Constructive Solid Geometry using OpenGL
Group:          System Environment/Libraries
# license.txt contains a linking exception for CGAL
License:        GPLv2 with exceptions
URL:            http://www.opencsg.org/
Source0:        http://www.opencsg.org/OpenCSG-%{version}.tar.gz
Patch0:         OpenCSG-1.3.2-3.remove-example.patch
Patch1:         OpenCSG-1.3.2-4.remove-unresolved.patch
BuildRequires:  qt-devel, freeglut-devel, glew-devel, dos2unix

%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.

CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by
taking the union of them, by intersecting them, or by subtracting one shape
of the other. The most basic shapes, which are not result of such a CSG
operation, are called primitives. Primitives must be solid, i.e., they must
have a clearly defined interior and exterior. By construction, a CSG shape is
also solid then.

Image-based CSG rendering (also z-buffer CSG rendering) is a term that denotes
algorithms for rendering CSG shapes without an explicit calculation of the
geometric boundary of a CSG shape. Such algorithms use frame-buffer settings
of the graphics hardware, e.g., the depth and stencil buffer, to compose CSG
shapes. OpenCSG implements a variety of those algorithms, namely the
Goldfeather algorithm and the SCS algorithm, both of them in several variants.

%package devel
Summary: OpenCSG development files
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for OpenCSG.

%prep
%setup -q -n OpenCSG-%{version}
%patch0 -p1
%patch1 -p1

rm src/Makefile RenderTexture/Makefile Makefile example/Makefile
dos2unix license.txt
# New FSF Address
for FILE in src/*.h src/*.cpp include/opencsg.h
do
  sed -i s/"59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"/ $FILE
done

# Use Fedora's glew
rm -rf glew/

%build
%{_qt4_qmake}
make %{?_smp_mflags}

%install
# No make install
chmod g-w lib/*
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
cp -pP lib/* %{buildroot}/%{_libdir}/
cp -p include/opencsg.h %{buildroot}/%{_includedir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc changelog.txt index.html news.html publications.html license.txt img
%{_libdir}/*so.*

%files devel
%{_includedir}/*
%{_libdir}/*so

%changelog
* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> - 1.3.2-6
- Removed FSF Address path
   - using sed instead, so the path is not needed to update in newer version
   - don't modify license file
- License exception explained in a comment
- Dropped doc form devel package
- Usiyng cp -pP instead of mv to preserve timestamps

* Mon Oct 8 2012 Miro Hrončok <miro@hroncok.cz> - 1.3.2-5
- Added img to doc (needed by html files)
- Added odc to devel package (to avoid W: no-documentation)

* Thu Jul 5 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-4
- Removed extranous build-depend to libXmu
- Fix undefined-non-weak-symbol for libGLEW
- Deprecate patch for fixing build order now the example program is gone
- Remove dependencies to qtGui and qtCore
- Remove example application from package
- Fix newlines in license.txt

* Thu Jun 7 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-3
- Fixed spec according to Volker's suggestions

* Wed May 30 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-2
- Fixed incorrect-fsf-address lint error

* Sat May 26 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-1
- Updated source material for OpenCSG version 1.3.2
- Patched opencsg.pro to build in proper order (src then example)
- Patched example.pro to require libGLU (else error is thrown)
- Fixed devel/debuginfo cpio call 'missing include/opencsg.h'

* Sat Mar  5 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-5
- Enable parallel compiling.
- Corrected license to GPLv2 with exceptions.
- Improved -devel Requires for multilib.
- Remove BuildRoot tag.
- Remove %%clean section
- Change mv and mkdir to direct commands, not macros.

* Sat Feb 26 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-4
- Regenerate Makefiles to fix rpath and debuginfo-without-sources
- Use Fedora's glew instead of included copy
- Remove tab from .spec

* Mon Feb 21 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-3
- Add ldconfig to %%post and %%postun
- Fix rpath
- Fix library permissions

* Sun Feb 20 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-2
- Use qmake macro

* Sun Feb 20 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-1
- Add -devel package
- Add BuildRequires

* Fri Feb 18 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-0
- Initial spec

