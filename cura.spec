Name:           cura
Version:        13.03
Release:        1%{?dist}
Summary:        3D printer control software

# Code is AGPLv3
# Icons AGPLv3 https://github.com/daid/Cura/issues/231#issuecomment-12209683
# Example models are CC-BY-SA
License:        AGPLv3 and CC-BY-SA

URL:            http://daid.github.com/Cura/

# I've stripped the source with the script in Source3
# To remove CC BY-NC content and bundled pypy binaries
# Already asked upstream to include free package
#Source0:       http://software.ultimaker.com/current/Cura-%%{version}-linux.tar.gz
Source0:        Cura-%{version}-linux-fedora.tar.gz
Source1:        %{name}
Source2:        %{name}.desktop
Source3:        %{name}-stripper.sh

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
Requires:       PyOpenGL
Requires:       wxPython
Requires:       pyserial
Requires:       numpy
Requires:       python-power
Requires:       pypy
Requires:       ultimaker-marlin-firmware >= 12.12-0.5.RC1

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

# Remove useless shebangs
cd slice/cura_sf/skeinforge_application/skeinforge_plugins/craft_plugins
for FILE in alteration.py scale.py dimension.py limit.py fill.py inset.py widen.py bottom.py preface.py ../../../../../cura.py ../../../../../util/pymclevel/mce.py; do
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
ln -s %{_datadir}/ultimaker-marlin-firmware %{buildroot}%{_datadir}/%{name}/firmware

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%files
%doc LICENSE resources/example/Attribution.txt
%{python_sitelib}/Cura
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.ico
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%changelog
* Sat Apr 20 2013 Miro Hrončok <mhroncok@redhat.com> - 13.03-1
- New upstream release

* Tue Feb 19 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-3
- chmod 755 cura-stripper.sh
- Use firmware from ultimaker-marlin-firmware package
- removed bundling note

* Sun Jan 20 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-2
- Launcher is in Python now

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-1
- First version

