Name:           netfabb-basic
Version:        5.0.1
Release:        1%{?dist}
Summary:        Freeware suite for STL editing
License:        Redistributable
URL:            http://www.netfabb.com/
# keep both sources in the SRPM
# both files are downloaded from http://www.netfabb.com/downloadcenter.php?basic=1
# and have no public tarball urls
Source0:        %{name}_%{version}_linux32.tar.gz
Source1:        %{name}_%{version}_linux64.tar.gz
BuildRequires:  desktop-file-utils

ExclusiveArch:  %{ix86} x86_64
%global debug_package %{nil}

%description
netfabb Basic is a free (as in free beer) software for 3D Printing
and the STL file format. Numerous tools allow all steps of the fabrication
process: editing, repairing, positioning, slicing and exporting triangulated
CAD data. For professional use, the author offers commercial support and
additional modules.

%prep

%ifarch %{ix86}
%setup -qn %{name} -b0
%endif

%ifarch x86_64
%setup -qn %{name} -b1
%endif

%build
# nothing to do

%install
# the workflow is copied from install.sh, but we will not run it, as it doesn't respect the buildroot
# there are also several changes to make things more OK

# create directories
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
for res in 16 22 24 32 48 128; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps
done
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/pixmaps

# binary and libraries
cp -p netfabb %{buildroot}%{_bindir}/%{name}
cp -p *.so.* %{buildroot}%{_libdir}

# desktopfile
export DESKTOPFILE=%{buildroot}%{_datadir}/applications/%{name}.desktop
echo "[Desktop Entry]">${DESKTOPFILE}
echo "Type=Application">>${DESKTOPFILE}
echo "Version=1.0">>${DESKTOPFILE}
echo "Name=netfabb Basic">>${DESKTOPFILE}
echo "GenericName=STL-Viewer">>${DESKTOPFILE}
echo "GenericName[de]=STL-Betrachter">>${DESKTOPFILE}
echo "Comment=View and repair STL files">>${DESKTOPFILE}
echo "Comment[de]=STL Dateien betrachten und reparieren">>${DESKTOPFILE}
echo "Icon=%{name}">>${DESKTOPFILE}
echo "TryExec=%{_bindir}/%{name}">>${DESKTOPFILE}
echo "Exec=%{_bindir}/%{name} %U">>${DESKTOPFILE}
echo "Terminal=false">>${DESKTOPFILE}
echo "MimeType=application/netfabb;application/sla;application/x-3ds;model/mesh;image/x-3ds;model/x3d+xml;model/x3d+binary;">>${DESKTOPFILE}
echo "Categories=Graphics;3DGraphics;Viewer;">>${DESKTOPFILE}
echo "StartupNotify=true">>${DESKTOPFILE}

# man and icons
cp -p man/%{name}.1.gz %{buildroot}%{_mandir}/man1
cp -p icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
for res in 16 22 24 32 48 128; do
  cp -p icons/%{name}${res}.png %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/%{name}.png
done
cp -p icons/%{name}48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :

%postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :

%files
%doc README LICENSE changelog.gz Examples
%attr(0755, root, root) %{_bindir}/%{name}
%attr(0755, root, root) %{_libdir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*


%changelog
* Tue Dec 31 2013 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-1
- New version

* Tue Mar 26 2013 Miro Hrončok <mhroncok@redhat.com> - 4.9.5-1
- Initial release
