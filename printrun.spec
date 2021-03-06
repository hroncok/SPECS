%global commit 71e5da009ae8de5e09cbb6dabf46a90cd2e8a62c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20130123git%{shortcommit}
Name:           printrun
Version:        0.0
Release:        22.%{snapshot}%{?dist}
Summary:        RepRap printer interface and tools
License:        GPLv3+
Group:          Applications/Engineering
URL:            https://github.com/kliment/Printrun
Source0:        https://github.com/kliment/Printrun/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

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
Requires:       pyserial

%description    common
Printrun is a set of G-code sending applications for RepRap.
This package contains common files.

###############################################

%package     -n pronsole
Summary:        CLI interface for RepRap
Requires:       %{name}-common = %{version}-%{release}
Requires:       skeinforge

%description -n pronsole
Pronsole is a featured command line G-code sender.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

###############################################

%package     -n pronterface
Summary:        GUI interface for RepRap
Requires:       wxPython
Requires:       pronsole = %{version}-%{release}

%description -n pronterface
Pronterface is a featured G-code sender with graphical user interface.
It controls the ReRap printer and integrates skeinforge.
It is a part of Printrun.

###############################################

%package     -n plater
Summary:        RepRap STL plater
Requires:       wxPython
Requires:       %{name}-common = %{version}-%{release}

%description -n plater
Plater is a GUI tool to prepare printing plate from STL files for ReRap.
It is a part of Printrun.

###############################################


%prep
%setup -qn Printrun-%{commit}

# use launchers for skeinforge
sed -i 's|python skeinforge/skeinforge_application/skeinforge.py|skeinforge|' pronsole.py
sed -i 's|python skeinforge/skeinforge_application/skeinforge_utilities/skeinforge_craft.py|skeinforge-craft|' pronsole.py

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

%files common
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

%files -n pronterface -f pronterface.lang
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
* Wed Jan 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-22.20130123git71e5da0
- Pull request merged
- Updated to new commit
- Removed pacth (no longer needed)

* Wed Jan 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-21.20130113git5897fbc
- Handle UTF-8 encode better in patch

* Wed Jan 23 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-20.20130113git5897fbc
- Removing UTF-8 removal from patch

* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-19.20130113git5897fbc
- Removed run-time deps, that are resolved automatically

* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-18.20130113git5897fbc
- Added patch from my pull request

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-17.20130113git5897fbc
- New "version" (bugfix)

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-16.20130113git094dffa
- New upstream "version", where everything is GPLv3+
- pronsole.ico and gcoder.py now part of setup.py
- Skeinforge path changing moved from %%install to %%prep
- Commented macros in changelog
- Use skeinforge launchers in default settings
- Pronterface lang moved from common to pronterface, is not needed by pronsole any more

* Wed Jan 09 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-15.20121103git6fa4766
- Updated to respect new GitHub rule

* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-14.20121103git6fa47668f2
- Changed location of skeinforge from %%{_datadir}/%%{name}/
                                   to %%{python_sitelib}/%%{name}

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
