Name:           stlsplit
Version:        1.1
Release:        1%{?dist}
Summary:        Split STL file to more files - one shell each
License:        AGPLv3+
Group:          Applications/Engineering
URL:            http://github.com/admesh/stlsplit/
Source0:        https://github.com/admesh/stlsplit/archive/v%{version}.tar.gz
BuildRequires:  admesh-devel >= 0.98
BuildRequires:  premake

%description
stlsplit receives one STL file and splits it to several files -
one shell a file.

%package devel
Summary:        Development files for the %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This tool receives one STL file and splits it to several files -
one shell a file.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%prep
%setup -q

%build
premake4 gmake
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' lib.make
CFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}

%install
install -Dpm 755 build/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 755 build/lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so
install -Dpm 644 %{name}.h %{buildroot}%{_includedir}/%{name}.h

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.1

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%changelog
* Fri Apr 24 2015 Miro Hrončok <mhroncok@redhat.com> - 1.1-1
- Initial package
