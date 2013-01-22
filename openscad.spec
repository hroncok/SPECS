Name:           openscad
%global shortversion 2013.01
Version:        %{shortversion}.17
Release:        2%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
License:        GPLv2 with exceptions
Group:          Applications/Engineering
URL:            http://www.openscad.org/
Source0:        https://openscad.googlecode.com/files/%{name}-%{shortversion}.src.tar.gz
BuildRequires:  qt-devel >= 4.4
BuildRequires:  bison >= 2.4
BuildRequires:  flex >= 2.5.35
BuildRequires:  eigen2-devel >= 2.0.13
BuildRequires:  boost-devel >= 1.3.5
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  glew-devel >= 1.6
BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%prep
%setup -qn %{name}-%{shortversion}

%build
qmake-qt4 VERSION=%{shortversion} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
# manpage
mkdir -p %{buildroot}%{_mandir}/man1
cp doc/%{name}.1 %{buildroot}%{_mandir}/man1/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
cmake . -DGLEW_INCLUDE_DIR=/usr/include/GL/
make %{?_smp_mflags}
ctest -C All || :
cd -

# remove MCAD (separate package) after the tests
rm -rf /libraries/MCAD

%files
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%changelog
* Tue Jan 22 2013 Miro Hrončok <mhroncok@redhat.com> - 2013.01.17-2
- Using  source tarball
- Reffer to the shorter version in the app
- Run tests

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
