Name:           repsnapper
Version:        2.1.0
Release:        4%{?dist}
Summary:        RepRap control software

# repsnapper is GPLv2 as noted in licensing.txt
#
# arcball.cpp and arcball.h are
#      (C) 1999-2003 Tatewake.com and licensed under the MIT license
#      as noted in licensing.txt
#
# libreprap is MIT (C) Benjamin Saunders and others
#      as noted here https://github.com/Ralith/libreprap/issues/4#issuecomment-13059313
#
# Several functions in slicer/geometry.cpp are licensed with non stock MIT-like license
#      as noted in licensing.txt
#      I've asked Fedora Legal list
#
# Icon is CC-BY, infile metadata
License:        GPLv2 and MIT and CC-BY

URL:            https://github.com/timschmidt/%{name}
%global         commit 4f0ca972f5e0ef69d7a86fa3d1222c2482d9afd8
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/timschmidt/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}-icon.svg
Patch0:         %{name}-use-system-libs.patch
Patch1:         %{name}-icon.patch
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
BuildRequires:  amftools-devel
BuildRequires:  lmfit-devel
BuildRequires:  poly2tri-devel
BuildRequires:  desktop-file-utils

%description
RepSnapper is a host software for controlling the RepRap 3D printer.

%prep
%setup -qn %{name}-%{commit}

%patch0 -p1
rm -rf libraries/{clipper,vmmlib,amf,lmfit,poly2tri}

# Remove license information of bundled libs
rm -f licenses/{BSL-1.0.txt,LGPL-2.0.txt,vmmlib-license.txt}
grep -v VMMLib licensing.txt > licensing-no-vmmlib.txt && mv -f licensing-no-vmmlib.txt licensing.txt

%patch1 -p1

sed -i 's/Utility;/Graphics;/' %{name}.desktop.in
sed -i 's/_Name=%{name}/_Name=RepSnapper/' %{name}.desktop.in
sed -i 's/# Icon=%{name}/Icon=%{name}/' %{name}.desktop.in


%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 %{SOURCE1} \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%doc HACKING licensing.txt README.asciidoc TODO todo.txt licenses
%config(noreplace) %{_sysconfdir}/xdg/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png

%changelog
* Tue Feb 05 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Using new RepSnapper icon

* Thu Jan 31 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Using system vmmlib, amftools, lmfit, poly2tri
- Polished description a bit
- Change name in .desktop to RepSnapper
- Added comment about license
- Using %%config(noreplace)
- Added icons from #679273

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
