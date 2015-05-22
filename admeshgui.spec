Name:           admeshgui
%global         camelname ADMeshGUI
Version:        1.0
Release:        1%{?dist}
Summary:        STL viewer and manipulation tool
License:        AGPLv3
URL:            https://github.com/vyvledav/%{camelname}
Source0:        https://github.com/vyvledav/%{camelname}/archive/v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libadmesh) >= 0.98.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.4
BuildRequires:  pkgconfig(Qt5Gui) >= 5.4
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.4
BuildRequires:  pkgconfig(Qt5Svg) >= 5.4
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(Qt5) >= 5.4
BuildRequires:  stlsplit-devel

Requires:       hicolor-icon-theme

Provides:       %{camelname}%{_isa} = %{version}-%{release}
Provides:       %{camelname} = %{version}-%{release}

%description
Extension for ADMesh tool in the form of graphical user interface. ADMesh tool
allows to manipulate and repair 3D models in the STL format. This graphical
user interface allows the user to view the model in 3D viewer, to perform
selected actions and to get visual feedback of those.

%prep
%setup -qn %{camelname}-%{version}
sed -i 's|/usr/|$$INSTALL_ROOT/usr/|g' %{camelname}.pro

%build
qmake-qt5
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%post
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%license LICENSE LOGO-LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri May 22 2015 Miro Hrončok <mhroncok@redhat.com> - 1.0-1
- Initial package
