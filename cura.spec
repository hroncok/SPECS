Name:           cura
Version:        12.12
Release:        1%{?dist}
Summary:        3D printer control software
# Code is AGPLv3
# Example models are CC
# Firmware UNKNOWN (daid has been asked)
# Ultimaker platform model UNKNOWN (daid has been asked)
License:        AGPLv3 and CC-BY-SA
URL:            http://daid.github.com/Cura/
Source0:        http://software.ultimaker.com/current/Cura-%{version}-linux.tar.gz
Source1:        cura
Source2:        cura.desktop
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
Requires:       PyOpenGL
Requires:       wxPython
Requires:       pyserial
Requires:       numpy
Requires:       python-power

## Note about bundling:
# It might seem like bundling skeinforge, but author of this software has said:
# 
# Mine is different, next to a bunch of bug fixes on SF50, I also made a lot of
# changes to add features. I also changed stuff to make it better integrated
# into Cura, so you cannot drop-in an SF version without changes. But I'm
# up-to-date with SF50.
#
# https://github.com/daid/Cura/issues/231#issuecomment-9317695

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura helps you to setup an Ultimaker, shows your 3D model, allows for scaling /
positioning, can slice the model to G-Code, with sane editable configuration
settings and send this G-Code to the 3D printer for printing.

%prep
%setup -qn Cura-%{version}-linux/Cura

dos2unix resources/example/Attribution.txt

# Until we know the license:
rm -rf resources/firmware resources/meshes

# CC-BY-NC is not possible in Fedora
rm -rf resources/example/UltimakerRobot_support.stl
echo -e '\n\nPlease note, that files under the terms of CC BY-NC has been removed form this Fedora package for legal reasons.' >> resources/example/Attribution.txt
sed -i 's/UltimakerRobot_support.stl/UltimakerHandle.stl/g' util/profile.py gui/app.py

# Remove useless shebangs
cd cura_sf/skeinforge_application/skeinforge_plugins/craft_plugins
for FILE in alteration.py scale.py dimension.py limit.py fill.py inset.py widen.py bottom.py preface.py ../../../../cura.py; do
  awk 'FNR>1' $FILE > $FILE.nobang && mv -f $FILE.nobang $FILE
done
cd -

%build
# do nothing

%install
mkdir -p %{buildroot}%{python_sitelib}/Cura
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}

cp -apr [acgpu_]* %{buildroot}%{python_sitelib}/Cura
cp -apr resources/* %{buildroot}%{_datadir}/%{name}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name} %{buildroot}%{python_sitelib}/Cura/resources
ln -s %{_datadir}/%{name}/%{name}.ico %{buildroot}%{_datadir}/pixmaps

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%files
%doc LICENSE resources/example/Attribution.txt
%{python_sitelib}/Cura
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.ico
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%changelog
* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-1
- First version

