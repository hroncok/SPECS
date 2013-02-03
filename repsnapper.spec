Name:           repsnapper
Version:        2.1.0
Release:        3%{?dist}
Summary:        RepRap control software
License:        GPLv2
URL:            https://github.com/timschmidt/%{name}
%global         commit 4f0ca972f5e0ef69d7a86fa3d1222c2482d9afd8
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/timschmidt/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         %{name}-use-system-libs.patch
BuildRequires:  gtkmm24-devel
BuildRequires:  gtkglext-devel
BuildRequires:  cairomm-devel
BuildRequires:  glibmm24-devel
BuildRequires:  glib2-devel
BuildRequires:  libxml++-devel
BuildRequires:  libzip-devel
BuildRequires:  freeglut-devel
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  polyclipping-devel >= 4.6.3
BuildRequires:  vmmlib-devel
BuildRequires:  desktop-file-utils

%description
RepSnapper is a host software for controlling the RepRap 3D printer.

%prep
%setup -qn %{name}-%{commit}

%patch0 -p1
rm -rf libraries/clipper/
rm -rf libraries/vmmlib/
rm -rf libraries/amf/
rm -rf libraries/lmfit/

sed -i 's/Utility;/Graphics;/' %{name}.desktop.in
sed -i 's/_Name=repsnapper/_Name=Repsnapper/' %{name}.desktop.in

%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc HACKING licensing.txt README.asciidoc TODO todo.txt licenses
%config %{_sysconfdir}/xdg/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.ui


%changelog
* Thu Jan 31 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Using system vmmlib, amftools, lmfit
- Polished description a bit

* Thu Jan 30 2013 Volker Fröhlich <volker27@gmx.at> - 2.1.0-2
- Correct patch to link polyclipping
- Make build verbose

* Tue Jan 29 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-1
- Chnaged source to respect GitHub rule
- Dropped %%{?_isa} from BRs
- Dropped group
- Added things to %%doc
- desktop-file-validate
- Using %%{name} macro in %%files
- Changing desktop file category to Multimedia, as at all others RepRap tools
- Using system clipper/polyclipping

* Wed Oct 24 2012 Alon Levy <alevy@redhat.com> - 2.1.0b02-3
- added missing dependencies for mock build

* Tue Oct 23 2012 Alon Levy <alevy@redhat.com> - 2.1.0b02-2
- Address review comments

* Mon Oct 22 2012 Alon Levy <alevy@redhat.com> - 2.1.0b02-1
- Initial spec file submitted for review
