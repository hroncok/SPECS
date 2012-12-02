Name:           openscad
Version:        2012.10.31
Release:        3%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
License:        GPLv2 with exceptions
Group:          Applications/Engineering
URL:            http://www.openscad.org/
# openscad commit hash b04734cbf5
#     MCAD commit hash 9af89906fa
# git clone git://github.com/openscad/openscad.git; cd openscad
# git archive master --format tar.gz > ../%%{name}-%%{version}.tar.gz
# git submodule init; git submodule update; cd libraries/MCAD/
# git archive master --format tar.gz > ../../../%%{name}-MCAD-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-MCAD-%{version}.tar.gz
BuildRequires:  qt-devel >= 4.4
BuildRequires:  bison >= 2.4
BuildRequires:  flex >= 2.5.35
BuildRequires:  eigen2-devel >= 2.0.13
BuildRequires:  boost-devel >= 1.3.5
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  glew-devel >= 1.6
BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  desktop-file-utils

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

###############################################

%package        MCAD
Summary:        OpenSCAD Parametric CAD Library
License:        LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

### LICENSES:

##  LGPLv2+:
#   3d_triangle.scad
#   fonts.scad
#   gridbeam.scad
#   hardware.scad
#   multiply.scad
#   shapes.scad
#   screw.scad

##  LGPLv2:
#   gears.scad
#   involute_gears.scad
#   servos.scad
#   transformations.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPLv3+:
#   teardrop.scad

##  GPLv3 or LGPLv2:
#   motors.scad
#   nuts_and_bolts.scad


##  GPLv3+ or LGPLv2:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA or LGPLv2+:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   utilities.scad

##  CC-BY-SA or LGPLv2:
#   units.scad

##  CC-BY:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

## BSD
#   boxes.scad

## MIT
#   constants.scad
#   curves.scad
#   math.scad

## Public Domain
#   lego_compatibility.scad
#   trochoids.scad

###############################################

%prep
%setup -qa1 -Tcn %{name}-%{version}/libraries/MCAD
rm -rf *.py SolidPython ThingDoc # we don't need them
rm -f .gitmodules # git crap
%setup -Dcq
# New FSF Address
for FILE in libraries/MCAD/regular_shapes.scad libraries/MCAD/metric_fastners.scad
do
  sed -i s/"59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"/ $FILE
done

%build
qmake-qt4 VERSION=%{version} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%{__make} install INSTALL_ROOT=%{buildroot}
# manpage
mkdir -p %{buildroot}%{_mandir}/man1
cp doc/%{name}.1 %{buildroot}%{_mandir}/man1/
gzip %{buildroot}%{_mandir}/man1/%{name}.1


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*


%files      MCAD
%doc libraries/MCAD/lgpl-2.1.txt libraries/MCAD/README.markdown
%{_datadir}/%{name}/libraries/MCAD

%changelog
* Sun Dec 02 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-3
- Added manpage

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-2
- Commented macros in comments
- Fully versioned dependency of the main package
- added desktop-file-validate

* Wed Oct 31 2012 Miro Hrončok <miro@hroncok.cz> 2012.10.31-1
- New version
- Solved 2 MLCAD files license issues
- Using full date version

* Mon Oct 08 2012 Miro Hrončok <miro@hroncok.cz> 2012.10-1
- New version.

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 2012.08-1
- New package.
