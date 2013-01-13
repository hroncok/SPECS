Name:           skeinforge
Version:        12.03.14
Release:        12%{?dist}
Summary:        Converts 3D model into G-Code for RepRap
# Asked author for LICENSE file - will be in next release
# Dev version for check: http://members.axion.net/~enrique/reprap_python_beanshell.zip
# Don't ask me, why the dev version isn't on the same website :(
License:        AGPLv3
Group:          Applications/Engineering
URL:            http://fabmetheus.crsndoo.com/wiki/index.php/Skeinforge
Source0:        http://fabmetheus.crsndoo.com/files/50_reprap_python_beanshell.zip
Source1:        skeinforge.desktop
Source2:        skeinforge
Patch0:         skeinforge-12.03.14-12.remove-help-button.patch
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
Requires:       python2
Requires:       tkinter

%description
Skeinforge is a tool chain composed of Python scripts that converts your
3D model into G-Code instructions for RepRap.

%package        doc
Requires:       %{name} = %{version}-%{release}
Summary:        Documentation for %{name}

%description    doc
Skeinforge is a tool chain composed of Python scripts that converts your
3D model into G-Code instructions for RepRap.
This is the documentation.

%prep
%setup -cq
%patch0 -p1

# Removing stupid useless files
rm -rf %{name}_application/*.sh %{name}_application/*.stl

# Removing shebangs
cd skeinforge_application/skeinforge_plugins/craft_plugins/
for FILE in preface.py alteration.py bottom.py dimension.py fill.py inset.py limit.py scale.py widen.py; do
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
cp -a %{SOURCE2} %{buildroot}%{_bindir} # launcher 

%files
%doc
%{python_sitelib}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%files      doc
%doc documentation

%changelog
* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 12.03.14-12
- Comment macros in changelog
- Remove shebangs from nonexecutable files
- Move deleting files from %%install to %%prep
- Added bash launcher to /usr/bin
- Modified .desktop file to use that launcher
- Moved documentation to %doc (help button in the app doesn't work anyway)
- Patch0: Remove non-working help button

* Tue Jan 08 2013 Miro Hrončok <mhroncok@redhat.com> - 12.03.14-11
- Don't add license.txt as a separate source

* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-10
- Changed location of skeinforge from %%{_datadir}/%%{name}/
                                   to %%{python_sitelib}/%%{name}

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-9
- Do not download the desktop file from my GitHub.

* Mon Oct 29 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-8
- Added desktop file
- Don't use macros for rm and cp
- Removed license file from doc package

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-7
- Do not install directly to printrun dir

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-6
- Include license file

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-5
- Noarch

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-4
- Owns %%{_datadir}/printrun/

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-3
- Splited documentation

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-2
- Added tkinter and python2 to requires

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-1
- New package
