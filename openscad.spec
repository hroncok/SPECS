Name:           openscad
Version:        2012.08
Release:        1%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
License:        GPLv2 # Check the Exception
Group:          Applications/Engineering # Optional
URL:            http://www.openscad.org/
# openscad commit hash 3b6f16605c
#     MCAD commit hash fa265644af
# git clone git://github.com/openscad/openscad.git; cd openscad
# git archive --format tar.gz > ../%{name}-%{version}.tar.gz
# git submodule init; git submodule update; cd libraries/MCAD/
# git archive --format tar.gz > ../../../%{name}-MCAD-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-MCAD-%{version}.tar.gz
BuildRequires:  qt-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  eigen2-devel
BuildRequires:  boost-devel
BuildRequires:  mpfr-devel
BuildRequires:  gmp-devel
BuildRequires:  glew-devel
BuildRequires:  CGAL-devel
BuildRequires:  opencsg-devel
#Requires:       eigen2
#Requires:       boost
#Requires:       mpfr
#Requires:       gmp
#Requires:       glew
#Requires:       CGAL
#Requires:       opencsg

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modelling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

###############################################

%package        MCAD
Summary:        OpenSCAD Parametric CAD Library
License:        LGPLv2 # And loads of other!
Requires:       %{name}

%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

###############################################

%prep
%setup -cq
# We don't want a version with today date
#sed -i s/'$$system(date "+%Y.%m.%d")'/'"%{version}"'/ version.pri

%build
qmake-qt4 VERSION=%{version} PREFIX=%{_exec_prefix}
make %{?_smp_mflags}

%install
%{__make} install INSTALL_ROOT=%{buildroot}

%files
%doc COPYING README.md RELEASE_NOTES

%changelog
* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 2012.08-1
- New package.
