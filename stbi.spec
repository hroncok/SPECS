Name:           stbi
%global soname  lib%{name}
%global srcname stb_image
Version:        1.33
Release:        1%{?dist}
Summary:        JPEG/PNG reader
License:        Public Domain
URL:            http://nothings.org/%{srcname}.c
Source0:        %{url}
BuildRequires:  dos2unix

%description
Public Domain JPEG/PNG reader. Primarily of interest to game developers and
other people who can avoid problematic images and only need the trivial
interface.

%package devel
Summary: JPEG/PNG reader development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -Tc
head -62 %{SOURCE0} > README
head -184 %{SOURCE0} | tail -112 >> README
 
head -65 %{SOURCE0} | tail -2 > %{srcname}.h
head -332 %{SOURCE0} | tail -146 >> %{srcname}.h

echo '#include "stb_image.h"' > %{srcname}.c
head -4586 %{SOURCE0} | tail -4254 >> %{srcname}.c

tail -86 %{SOURCE0} > CHANGES

dos2unix *

%build
gcc -O2 -g -pipe -Wall -I. -fPIC -c %{srcname}.c
gcc -O2 -g -pipe -Wall -I. -shared -Wl,-soname,%{soname}.so.1 %{srcname}.o -o %{soname}.so.1.0.0


%install
install -Dpm0755 %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so.1.0.0
ln -s %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so.1
ln -s %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so
install -Dpm0644 %{srcname}.h %{buildroot}%{_includedir}/%{srcname}.h

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README CHANGES
%{_libdir}/%{soname}.so.*

%files devel
%{_libdir}/%{soname}.so
%{_includedir}/*

%changelog
* Sat Feb 02 2013 Miro Hrončok <mhroncok@redhat.com> - 1.33-1
- Started

