%global commit 89e1e76d35899ad21516a2facc75df274c5550e1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20121114git%{shortcommit}
Name:           sfact
Version:        0.0
Release:        2.%{snapshot}%{?dist}
Summary:        Converts 3D model into G-Code for RepRap
# Sent pull request with the license text
# https://github.com/ahmetcemturan/SFACT/pull/25
# You can find the license in files
License:        AGPLv3
Group:          Applications/Engineering
URL:            http://www.reprapfordummies.net/
Source0:        https://github.com/ahmetcemturan/SFACT/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}
Source3:        %{name}-craft
Patch0:         %{name}-remove-help-button.patch
Patch1:         %{name}-setting-dir.patch
Patch2:         %{name}-empty-extrusion-profile.patch
Patch3:         %{name}-empty-winding-profile.patch
Patch4:         %{name}-empty-cutting-profile.patch
Patch5:         %{name}-empty-milling-profile.patch
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
Requires:       python2
Requires:       pypy
Requires:       tkinter

%description
SFACT is the new Skeinforge, it is a tool chain composed of Python scripts
that converts your 3D model into G-Code instructions for RepRap.

%package        doc
Requires:       %{name} = %{version}-%{release}
Summary:        Documentation for %{name}

%description    doc
SFACT is the new Skeinforge, it is a tool chain composed of Python scripts
that converts your 3D model into G-Code instructions for RepRap.
This is the documentation.

%prep
%setup -qn SFACT-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

chmod +x sfact.py
chmod -x fabmetheus_utilities/settings.py

# Removing stupid useless files
rm -rf skeinforge_application/*.sh skeinforge_application/*.stl skFrontend.py *.sh

# Removing shebangs
cd skeinforge_application/skeinforge_plugins/craft_plugins/
for FILE in  alteration.py bottom.py dimension.py fill.py inset.py limit.py preface.py scale.py widen.py ../../profiles/dimension2.py ../../skeinforge.py; do
  awk 'FNR>1' $FILE > $FILE.nobang && mv -f $FILE.nobang $FILE
done
cd -

cd fabmetheus_utilities/miscellaneous/fabricate/
for FILE in example.py send.py RepRapArduinoSerialSender.py; do
  awk 'FNR>1' $FILE > $FILE.nobang && mv -f $FILE.nobang $FILE
done
chmod +x frank_davies/t.sh
cd -

%build

%install
mkdir -p %{buildroot}%{python_sitelib}/%{name}
mkdir -p %{buildroot}%{_bindir}
cp -ar [fs_]* %{buildroot}%{python_sitelib}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1} # desktop file
cp -a %{SOURCE2} %{SOURCE3} %{buildroot}%{_bindir} # launchers

%files
%doc SFACT?Readme.txt
%{python_sitelib}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}*

%files      doc
%doc documentation

%changelog
* Tue Jan 29 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-2.20121114git89e1e76
- SFACT?Readme.txt instead of SFACT\ Readme.txt in %%doc to make this work in rawhide

* Sun Jan 27 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20121114git89e1e76
- Started as a fork of skeinforge.spec
- Updated source to GitHub, SFACT has no tarballs
- Added patches from Debain
- Added patch to keep setting in HOME
