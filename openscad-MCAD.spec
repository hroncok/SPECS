%global         githash  9af89906fa
%global         snapshot 20121031git%{githash}
Name:           openscad-MCAD
Version:        0.0
Release:        2.%{snapshot}%{?dist}
Summary:        OpenSCAD Parametric CAD Library
License:        LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
Group:          Applications/Engineering
URL:            https://www.github.com/openscad/MCAD
# git clone git://github.com/openscad/MCAD.git; cd MCAD
# git archive master --format tar.gz > ../%%{name}-%%{snapshot}.tar.gz
Source0:        %{name}-%{snapshot}.tar.gz     
Requires:       openscad
BuildArch:      noarch

%description
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
%setup -cq
pwd
rm -rf *.py SolidPython ThingDoc # we don't need them
rm -f .gitmodules # git crap
# New FSF Address
sed -i s/"59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"/ regular_shapes.scad metric_fastners.scad

%build
# do nothing

%install
mkdir -p %{buildroot}%{_datadir}/openscad/libraries/MCAD
cp -R * %{buildroot}%{_datadir}/openscad/libraries/MCAD

%files
%doc lgpl-2.1.txt README.markdown
%{_datadir}/openscad/libraries/MCAD

%changelog
* Sun Dec 09 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-2.20121031git9af89906fa
- Added empty %%build section

* Thu Dec 06 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-1.20121031git9af89906fa
- Separated MCAD from openscad source package
