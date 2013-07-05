Name:           bitdht
Version:        0.2
Release:        1%{?dist}
Summary:        Distributed Hash Table library
License:        LGPLv3
URL:            http://bitdht.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-v%{version}-src-2010-10-31.tgz
# corrects missing include and modifies .pro file to generate shared lib
Patch0:         %{name}-build.patch
# corrects missing include in tests
Patch1:         %{name}-tests.patch
# allow example app to build with moved includes
Patch2:         %{name}-example-makefile.patch
BuildRequires:  qt-devel

%description
BitDHT is a LGPL'd general purpose C++ Distributed Hash Table library.
It is designed to take hassle out over creating your own DHT.
BitDHT is compatible with bitttorrent's DHT and can leverage this network
to bootstrap your own personal DHT.

%package devel
Summary: BitDHT development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for BitDHT.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{_qt4_qmake}
make %{?_smp_mflags}

%install
# No make install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}/%{name}/{%{name},udp,util}
cp -pP lib/* %{buildroot}/%{_libdir}/
cp -pP %{name}/*.h %{buildroot}/%{_includedir}/%{name}/%{name}
cp -pP %{name}/bdboot.txt %{buildroot}/%{_includedir}/%{name}/udp
cp -pP util/*.h %{buildroot}/%{_includedir}/%{name}/util

%if 0%{?with_tests}
# test appears to work only on good network
%check
cd tests
make %{?_smp_mflags}
LD_LIBRARY_PATH=../lib make regress
cd -
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.txt
%{_libdir}/*so.*

%files devel
%doc README.txt example
%{_includedir}/*
%{_libdir}/*so

%changelog
* Fri Jul 05 2013 Miro Hrončok <mhroncok@redhat.com> - 0.2-1
- New spec

