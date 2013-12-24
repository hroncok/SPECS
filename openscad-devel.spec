Name:           openscad
%global shortversion 2013.12
%global commit 6938ae2dfde578e3980d077adefb86a4bdbd9df1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gittag 20131217git%{shortcommit}
Version:        %{shortversion}
Release:        0.4.%{gittag}%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
License:        GPLv2 with exceptions and CC0
Group:          Applications/Engineering
URL:            http://www.openscad.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        MCAD-master.zip
BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  Xvfb
BuildRequires:  bison >= 2.4
BuildRequires:  boost-devel >= 1.3.5
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-devel
BuildRequires:  flex >= 2.5.35
BuildRequires:  glew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  mesa-dri-drivers
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  procps-ng
BuildRequires:  python2
BuildRequires:  qt-devel >= 4.4

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%prep
%setup -qa1 -Tcn %{name}-%{commit}/libraries
mv MCAD{-master,}
%setup -Dqn %{name}-%{commit}

%build
qmake-qt4 VERSION=%{shortversion} PREFIX=%{_prefix}
make %{?_smp_mflags}

# tests
cd tests
cmake .
make %{?_smp_mflags}
cd -

%install
make install INSTALL_ROOT=%{buildroot}
# manpage
mkdir -p %{buildroot}%{_mandir}/man1
cp doc/%{name}.1 %{buildroot}%{_mandir}/man1/

# appdata
mkdir -p %{buildroot}%{_datadir}/appdata
cp *.appdata.xml %{buildroot}%{_datadir}/appdata/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} -C All || : # let the tests fail, as they probably won't work in Koji
cat sysinfo.txt
cat Testing/Temporary/LastTest.log
cd -

# remove MCAD (separate package) after the tests
rm -rf %{buildroot}%{_datadir}/%{name}/libraries/MCAD

%files
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%changelog
* Mon Dec 23 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.4.20131217git6938ae2
- Include appdata in the RPM

* Thu Dec 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.3.20131217git6938ae2
- Development version

* Tue Dec 17 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.2.20131215gite64bf96
- Development version
- Added BRs for virtual framebuffer

* Tue Oct 29 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.10-0.1.20131029git8aa749f
- Development version

* Fri Jun 07 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.06-0.1rc1
- New version RC

* Sun Jan 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-3
- Use Xvfb

* Tue Jan 22 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-2
- Using  source tarball
- Reffer to the shorter version in the app
- Run tests
- Added patch so test will compile
* Sat Jan 19 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-1
- New stable release 2013.01
- Updated to respect GitHub rule

* Tue Jan 08 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.08-1
- New version

* Sun Jan 06 2013 Miro Hrončok <miro@hroncok.cz> - 2013.01.05-1
- New version

* Thu Dec 06 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-5
- Separated MCAD

* Mon Dec 03 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-4
- Removed useless gziping

* Sun Dec 02 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-3
- Added manpage

* Fri Nov 23 2012 Miro Hrončok <miro@hroncok.cz> - 2012.10.31-2
- Commented macros in comments
- Fully versioned dependency of the main package
- added desktop-file-validate

* Wed Oct 31 2012 Miro Hrončok <miro@hroncok.cz> 2012.10.31-1
- New version
- Solved 2 MLCAD files license issues
- Using full date version

* Mon Oct 08 2012 Miro Hrončok <miro@hroncok.cz> 2012.10-1
- New version.

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 2012.08-1
- New package.
