Name:           CuraEngine
Version:        13.06.3
Release:        1%{?dist}
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPLv3
URL:            https://github.com/Ultimaker/%{name}
Source0:        %{url}/archive/%{version}.tar.gz
#%%if 0%%{?fedora} > 18
Patch0:         %{name}-clipper51x.patch
#%%endif
BuildRequires:  polyclipping-devel

%description
%{name} is a C++ console application for 3D printing G-code generation. It has
been made as a better and faster alternative to the old Skeinforge engine.

This is just a console application for G-code generation. For a full graphical
application look at cura with is the graphical frontend for %{name}.

%prep
%setup -q
%if 0%{?fedora} > 18
%patch0 -p1
%endif

# bundled clipper
rm -rf clipper
sed -i 's|#include "clipper/clipper.hpp"|#include <polyclipping/clipper.hpp>|' utils/intpoint.h
sed -i 's|$(CC)|$(CC) $(LIBS)|g' Makefile
sed -i 's| clipper/clipper.cpp||g' Makefile

# update version in main.spp
sed -i 's|#define VERSION "1.0"|#define VERSION "%{version}"|' main.cpp

%build
LIBS="-lpolyclipping" CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
install -Dpm0755 %{name} %{buildroot}/%{_bindir}/%{name}

%check
#make tests - fetches models form web, some of them returns 404
for MODEL in wolt woltBaselin woltNotFlat wolt_scaled200Perc wolt_smoothingOn; do
  ./%{name} -v -o ./testcase_models/${MODEL}.gcode ./testcase_models/${MODEL}.stl
done

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Sun Jun 23 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-1
- New package
