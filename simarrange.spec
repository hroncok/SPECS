%global commit d52382feb716621f9ac08d25a502420fc1d3c983
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global datestamp 20131019
%global relstring %{datestamp}git%{shortcommit}
Name:           simarrange
Version:        0.0
Release:        1.%{relstring}%{?dist}
Summary:        STL 2D plate packer with collision simulation
License:        AGPLv3+
URL:            https://github.com/kliment/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  admesh-devel
BuildRequires:  argtable-devel
BuildRequires:  opencv-devel
BuildRequires:  uthash-devel

%description
Simarrange is a program that simulates collisions between STL meshes in 2D in
order to generate tightly packed sets of parts. It takes a directory of STL
files as input and outputs STL files with combined plates of parts.
The parts are assumed to be in the correct printable orientation already.

%prep
%setup -qn %{name}-%{commit}

# bundling
rm utlist.h
rm admesh -rf

%build
# the build script is one line and would need patching, so just skip it
gcc %{optflags} simarrange.c -o ./%{name} -lm -lopencv_imgproc -lopencv_core \
    -lopencv_highgui -ladmesh -largtable2 -fopenmp -DPARALLEL

%install
install -Dpm0755 ./%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING Readme
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Tue Oct 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20131019gitd52382f
- New package


