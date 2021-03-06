%global real_name gnome-colors

Name: gnome-colors-icon-theme
Summary: GNOME-Colors icon theme
Version: 5.5.1
Release: 6%{?dist}
Url: http://code.google.com/p/gnome-colors
Source0: http://%{real_name}.googlecode.com/files/%{real_name}-src-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Requires: gnome-icon-theme
BuildRequires: icon-naming-utils >= 0.8.7
BuildRequires: inkscape
BuildRequires: ImageMagick

%description
The GNOME-Colors is a project that aims to make the GNOME desktop as 
elegant, consistent and colorful as possible.

The current goal is to allow full color customization of themes, icons, 
GDM logins and splash screens. There are already seven full color-schemes 
available; Brave (Blue), Human (Orange), Wine (Red), Noble (Purple), Wise 
(Green), Dust (Chocolate) and Illustrious (Pink). An unlimited amount of 
color variations can be rebuilt and recolored from source, so users need 
not stick to the officially supported color palettes.

GNOME-Colors is mostly inspired/based on Tango, GNOME, Elementary, 
Tango-Generator and many other open-source projects. More information 
can be found in the AUTHORS file.

%prep
%setup -q -c %{real_name}--icon-theme-%{version}
# link the start-here icon to the Fedora icon
for dir in gnome-colors-common/*/places; do
  cd $dir
  ln -sf ../apps/fedora-logo-icon.* start-here.*
  cd -
done
# change name from GNOME -> GNOME-Colors
rename 'gnome' '%{real_name}' themes/*
sed -i -e 's/GNOME/GNOME-Colors/' themes/*

%build
make %{?_smp_mflags}

%install
%{make_install}

%post
for dir in /usr/share/icons/gnome-*; do
  /bin/touch --no-create %{_datadir}/icons/$dir &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
  for dir in /usr/share/icons/gnome-*; do
    /bin/touch --no-create %{_datadir}/icons/$dir &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$dir &>/dev/null || :
  done
fi

%posttrans
for dir in /usr/share/icons/gnome-*; do
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$dir &>/dev/null || :
done

%files
%doc COPYING AUTHORS README ChangeLog
%{_datadir}/icons/gnome-colors-common/
%{_datadir}/icons/gnome-colors-brave/
%{_datadir}/icons/gnome-colors-carbonite/
%{_datadir}/icons/gnome-colors-dust/
%{_datadir}/icons/gnome-colors-human/
%{_datadir}/icons/gnome-colors-illustrious/
%{_datadir}/icons/gnome-colors-noble/
%{_datadir}/icons/gnome-colors-tribute/
%{_datadir}/icons/gnome-colors-wine/
%{_datadir}/icons/gnome-colors-wise/

%changelog
* Fri Oct 18 2013 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-6
- Use %%global instead of %%define
- Use %%{make_install}
- Use icon cache scriplets form wiki

* Sun Sep 01 2013 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-5
- Link the start-here icon to the Fedora icon

* Fri Aug 30 2013 Miro Hrončok <mhroncok@redhat.com> - 5.5.1-4
- Removed BuildRoot definition and Group
- Removed %%clean section
- Removed rm -rf form %%install
- Removed %%defattr from %%files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 18 2009 Michal Nowak <mnowak@redhat.com> - 5.5.1-1
- 5.5.1

* Tue Aug  4 2009 Michal Nowak <mnowak@redhat.com> - 5.3-1
- 5.3
- Requires: gnome-icon-theme

* Mon Aug  3 2009 Michal Nowak <mnowak@redhat.com> - 5.2.2-1
- initial packaging

