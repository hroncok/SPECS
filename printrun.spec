%global         githash  6fa47668f2
%global         snapshot 20121103git%{githash}
Name:           printrun
Version:        0.0
Release:        14.%{snapshot}%{?dist}
Summary:        RepRap printer interface and tools
License:        GPLv3+
Group:          Applications/Engineering
URL:            https://github.com/kliment/Printrun
# git clone https://github.com/kliment/Printrun.git; cd Printrun
# git archive --format tar.gz master > ../%%{name}-%%{snapshot}.tar.gz
Source0:        %{name}-%{snapshot}.tar.gz

# Desktop files
Source1:        pronsole.desktop
Source2:        pronterface.desktop
Source3:        plater.desktop

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       pronterface = %{version}-%{release}
Requires:       pronsole = %{version}-%{release}
Requires:       plater = %{version}-%{release}

%description
Printrun is a set of G-code sending applications for RepRap.
It consists of printcore (dumb G-code sender), pronsole (featured command line
G-code sender), pronterface (featured G-code sender with graphical user
interface), and a small collection of helpful scripts. Together with skeinforge
they form a pretty powerful softwarecombo. This package installs whole Printrun.

###############################################

%package        common
Summary:        Common files for Printrun
Requires:       python2
Requires:       pyserial

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

###############################################

%package     -n pronsole
Summary:        CLI interface for RepRap
Requires:       python2
Requires:       %{name}-common = %{version}-%{release}
Requires:       skeinforge

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

###############################################

%package     -n pronterface
Summary:        GUI interface for RepRap
Requires:       python2
Requires:       wxPython
Requires:       %{name}-common = %{version}-%{release}
Requires:       pronsole = %{version}-%{release}
Requires:       skeinforge

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

###############################################

%package     -n plater
Summary:        RepRap STL plater
Requires:       python2
Requires:       wxPython
Requires:       %{name}-common = %{version}-%{release}

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.

###############################################


%prep
%setup -cq

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

# rebuild locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || echo plater not there
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || echo pronterface not there
done
cd ..

%install
%{__python} setup.py install --skip-build --prefix %{buildroot}%{_prefix}
cp pronsole.ico %{buildroot}%{_datadir}/pixmaps/
cp gcoder.* %{buildroot}%{_bindir}

# use absolute path for skeinforge
sed -i 's|python skeinforge/skeinforge_application|python %{python_sitelib}/skeinforge/skeinforge_application|' %{buildroot}%{_bindir}/pronsole.py

# desktop files
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}

# locales
mkdir -p %{buildroot}%{_datadir}/locale
cp -ar %{buildroot}%{_datadir}/pronterface/locale/* %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{_datadir}/pronterface/locale
ln -s -f %{_datadir}/locale/ %{buildroot}%{_datadir}/pronterface/ # the app expects the locale folder in here

# exacutables
cd %{buildroot}%{python_sitelib}/%{name}
chmod +x gcview.py graph.py stlview.py SkeinforgeQuickEditDialog.py calibrateextruder.py webinterface.py
cd -

%{find_lang} pronterface
%{find_lang} plater

%files
%doc README* COPYING

%files common -f pronterface.lang
%{python_sitelib}/%{name}
%{python_sitelib}/Printrun*
%{_bindir}/printcore.*
%doc README* COPYING

%files -n pronsole
%{_bindir}/pronsole.*
%{_bindir}/gcoder.*
%{_datadir}/pixmaps/pronsole.ico
%{_datadir}/applications/pronsole.desktop
%doc README* COPYING

%files -n pronterface
%{_bindir}/pronterface.*
%{_datadir}/pronterface
%{_datadir}/pixmaps/P-face.ico
%{_datadir}/applications/pronterface.desktop
%doc README* COPYING

%files -n plater -f plater.lang
%{_bindir}/plater.*
%{_datadir}/pixmaps/plater.ico
%{_datadir}/applications/plater.desktop
%doc README* COPYING

%changelog
* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-14.20121103git6fa47668f2
- Changed location of skeinforge from %{_datadir}/%{name}/
                                   to %{python_sitelib}/%{name}

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-13.20121103git6fa47668f2
- Do not download the desktop files from my GitHub

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-12.20121103git6fa47668f2
- Fixing a source mistake
- Redone, using setup.py now

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-11.20121103git6fa47668f2
- New upstream "version" (merge from experimetal)
- Commented macros in comments
- Playing a bit with attr

* Mon Oct 29 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-10-20120924gitb6935b93
- Switched generic names and names in desktop files
- Don't use rm, cp and ln -s macros

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-9-20120924gitb6935b93
- updated bash lounchers

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-8-20120924gitb6935b93
- ln -s skeinforge
- printrun requires exact version and release

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-7-20120924gitb6935b93
- New sources links

* Fri Sep 22 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-6-20120924gitb6935b93
- New commits, inlude the license

* Fri Sep 22 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-5-20120921gitdceaf26f
- launching scripts now pass the params

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-4-20120921gitdceaf26f
- Build gettext

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-3-20120921gitdceaf26f
- BuildRequires:  desktop-file-utils

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-2-20120921gitdceaf26f
- Language files correctly added

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-1-20120921gitdceaf26f
- New package
