Name:           openscad
%global shortversion %(date +%Y).%(date +%m)
Version:        %{shortversion}
Release:        0.10.20140628git9fdc44b0%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
License:        GPLv2 with exceptions and CC0
Group:          Applications/Engineering
URL:            http://www.openscad.org/
Source0:        openscad-devel-9fdc44b0.tar
Source1:        MCAD-master.zip
BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  Xvfb
BuildRequires:  bison >= 2.4
BuildRequires:  boost-devel >= 1.35
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-devel
BuildRequires:  flex >= 2.5.35
BuildRequires:  freetype-devel >= 2.4
BuildRequires:  fontconfig-devel >= 2.10
BuildRequires:  glew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  harfbuzz-devel >= 0.9.19
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
%setup -qa1 -Tcn %{name}-devel/libraries
mv MCAD{-master,}
%setup -Dqn %{name}-devel

%build
qmake-qt4 VERSION=%{shortversion} PREFIX=%{_prefix}
make %{?_smp_mflags}

# tests
cd tests
OPENSCAD_UPLOAD_TESTS=yes cmake .
make %{?_smp_mflags}
cd -

%install
make install INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} -C All || : # let the tests fail, as they probably won't work in Koji
cd -

# remove MCAD (separate package) after the tests
rm -rf %{buildroot}%{_datadir}/%{name}/libraries/MCAD

%files
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%if 0%{?fedora} < 21
%{_datadir}/appdata
%else
%{_datadir}/appdata/*.xml
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%changelog
* Sat Jun 28 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.10.20140628git9fdc44b0
- Update to git: 9fdc44b0

* Wed Jun 25 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.9.20140625gitd9fda460
- Update to git: d9fda460

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.06-0.8.20140623git681f03a2
- Update to git: 681f03a2

* Wed Jun 18 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.7.20140618git48e1d6a5
- Update to git: 48e1d6a5

* Tue Jun 10 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.6.20140610git05e2a1ed
- Update to git: 05e2a1ed

* Sun Jun 08 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.5.20140608gitdb22a019
- Update to git: db22a019

* Fri Jun 06 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.4.20140606gitacd6cb1a
- Update to git: acd6cb1a

* Wed Jun 04 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.3.20140604git78803bfe
- Update to git: 78803bfe

* Fri May 30 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.2.20140530gitca3ff7cf
- Update to git: ca3ff7cf

* Thu May 29 2014 Miro Hrončok <mhroncok@redhat.com> - %{shortversion}-0.1.20140529git380af79b
- Update to git: 380af79b

* Mon Mar 03 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.03-0.1.201400303git8635e94
- Latest RC

* Fri Feb 28 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.4.20140228gitb2fbad4
- 2014.03 RC new commits

* Thu Feb 27 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.3.20140227gitbc86c49
- 2014.03 RC new commits

* Wed Feb 26 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.2.20140225git341571c
- 2014.03 RC

* Sat Feb 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.02-0.1.20140222git6867c50
- New commit

* Wed Jan 29 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01-0.3.20140127git41f4575
- New commit
- Upload test results
- Don't cat the results to the log

* Mon Jan 27 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01-0.2.20140124gitd9432d7
- New commit

* Sun Jan 12 2014 Miro Hrončok <mhroncok@redhat.com> - 2014.01-0.1.20140108gite6bfee0
- New commit
- New month

* Mon Dec 30 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.6.20131229gitbf19347
- New commit

* Tue Dec 24 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.12-0.5.20131223git41ab9e8
- New commit
- Manpage and appdata now installed with make install

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
