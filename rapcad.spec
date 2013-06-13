Name:           rapcad
Version:        0.9.0
Release:        1%{?dist}
# COPYING contains a linking exception for CGAL
License:        GPLv3+
Summary:        Rapid prototyping CAD IDE for 3D printing machines
Url:            http://rapcad.org/
Group:          Productivity/Graphics/CAD
Source:         http://git.rapcad.org/cgit.cgi/rapcad/snapshot/%{name}-%{version}.tar.gz
BuildRequires:  flex >= 2.5.35
BuildRequires:  gcc-c++
BuildRequires:  boost-devel >= 1.3.5
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  CGAL-devel >= 3.6
#BuildRequires:  libdxflib-devel-static
BuildRequires:  byacc
BuildRequires:  qt-devel >= 4.4
#BuildRequires:  desktop-file-utils

%description
RapCAD is the Rapid prototyping CAD IDE for RepRap and RepStrap 3D printing
machines.

%prep
%setup -q

%build
qmake-qt4 "CONFIG+=official"
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%doc doc licence.text COPYING README VERSION
%{_bindir}/rapcad

%changelog
* Tue Jan 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-1
- New package
