%global         githash  b6935b93
%global         snapshot 20120924git%{githash}
Name:           printrun
Version:        0.0
Release:        7.%{snapshot}%{?dist}
Summary:        RepRap printer interface and tools
License:        GPLv3+ # Ask author for LICENCE file
Group:          Applications/Engineering # Optional
URL:            https://github.com/kliment/Printrun
# git clone https://github.com/kliment/Printrun.git; cd Printrun
# git archive --format tar.gz dceaf26f > ../%{name}-%{snapshot}.tar.gz
# the command has a mistake :(
Source0:        %{name}-%{snapshot}.tar.gz

%global         additional https://raw.github.com/hroncok/RPMAdditionalSources/master/
# Bash runners
Source1:        %{additional}pronsole
Source2:        %{additional}pronterface
Source3:        %{additional}plater
# Desktop files
Source4:        %{additional}pronsole.desktop
Source5:        %{additional}pronterface.desktop
Source6:        %{additional}plater.desktop

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       pronterface
Requires:       pronsole
Requires:       plater

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
# build locales
cd locale
for FILE in *
  do msgfmt $FILE/LC_MESSAGES/plater.po -o $FILE/LC_MESSAGES/plater.mo || echo plater not there
     msgfmt $FILE/LC_MESSAGES/pronterface.po -o $FILE/LC_MESSAGES/pronterface.mo || echo pronterface not there
done
cd ..


%install
%{__rm} -rf 20cube_export.gcode locale/*.pot locale/*/LC_MESSAGES/*.po # removes stupid useless files and original .po files
mkdir -p %{buildroot}%{_datadir}/locale # /usr/share/locale
cp -ar locale/* %{buildroot}%{_datadir}/locale # copy compiled locales to that dir
%{__rm} -rf locale # remove original locale dir
mkdir -p %{buildroot}%{_datadir}/%{name} # /usr/share/printrun
%{__ln_s} -f ../locale/ %{buildroot}%{_datadir}/%{name}/ # the app expects the locale folder in here
cp -ar * %{buildroot}%{_datadir}/%{name} # copy everything to /usr/share/printrun
%{__rm} -rf %{buildroot}%{_datadir}/%{name}/README* # this will be in docs
%{__rm} -rf %{buildroot}%{_datadir}/%{name}/COPYING # this will be in docs
mkdir -p %{buildroot}%{_datadir}/pixmaps # /usr/share/pixmaps
%{__ln_s} ../%{name}/pronsole.ico %{buildroot}%{_datadir}/pixmaps # link the icons to pixmaps, so thay have the right location too
%{__ln_s} ../%{name}/plater.ico %{buildroot}%{_datadir}/pixmaps
%{__ln_s} ../%{name}/P-face.ico %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir} # /usr/bin
cp %{SOURCE1} %{buildroot}%{_bindir} # shell scripts to run the apps
cp %{SOURCE2} %{buildroot}%{_bindir}
cp %{SOURCE3} %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4} # desktop files
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE6}

%{find_lang} pronterface
%{find_lang} plater

%files
%doc README* COPYING

%files common -f pronterface.lang
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/locale/
%doc README*
%{_datadir}/%{name}/printcore.*
%{_datadir}/%{name}/stlview.*
%{_datadir}/%{name}/stltool.*
%{_datadir}/%{name}/__init__.*

%files -n pronsole
%{_datadir}/%{name}/pronsole.*
%attr(755,root,root) %{_bindir}/pronsole
%{_datadir}/pixmaps/pronsole.ico
%{_datadir}/applications/pronsole.desktop
%doc README* COPYING

%files -n pronterface
%{_datadir}/%{name}/pronterface.*
%{_datadir}/%{name}/P-face.*
%{_datadir}/%{name}/images
%{_datadir}/%{name}/bufferedcanvas.*
%{_datadir}/%{name}/calibrateextruder.*
%{_datadir}/%{name}/custombtn.txt
%{_datadir}/%{name}/gcview.*
%{_datadir}/%{name}/graph.*
%{_datadir}/%{name}/gviz.*
%{_datadir}/%{name}/projectlayer.*
%{_datadir}/%{name}/SkeinforgeQuickEditDialog.*
%{_datadir}/%{name}/xybuttons.*
%{_datadir}/%{name}/zbuttons.*
%{_datadir}/%{name}/zscaper.*
%attr(755,root,root) %{_bindir}/pronterface
%{_datadir}/pixmaps/P-face.ico
%{_datadir}/applications/pronterface.desktop
%doc README* COPYING

%files -n plater -f plater.lang
%{_datadir}/%{name}/plater.*
%attr(755,root,root) %{_bindir}/plater
%{_datadir}/pixmaps/plater.ico
%{_datadir}/applications/plater.desktop
%doc README* COPYING

%changelog
* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-7-20120924gitb6935b93
- New sources links

* Fri Sep 22 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-6-20120924gitb6935b93
- New commits, inlude the license

* Fri Sep 22 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-5-20120921gitdceaf26f
- launching scripts now pass the params

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-4-20120921gitdceaf26f
- Build gettext

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-3-20120921gitdceaf26f
- BuildRequires:	desktop-file-utils

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-2-20120921gitdceaf26f
- Language files correctly added

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-1-20120921gitdceaf26f
- New package
