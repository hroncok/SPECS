%{?mingw_package_header}
Name:           mingw-admesh
Version:        0.98.0
Release:        1%{?dist}
Summary:        MinGW compiled ADMesh

License:        GPLv2+

URL:            http://github.com/admesh/admesh/
Source0:        http://github.com/admesh/admesh/releases/download/v%{version}/admesh-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc

%description
MinGW compiled ADMesh. ADMesh is a program for diagnosing and/or repairing
commonly encountered problems with STL (STereo Lithography) data files.


%package -n mingw32-admesh
Summary:       MinGW compiled ADMesh for the Win32 target

%description -n mingw32-admesh
MinGW compiled ADMesh for the Win32 target.

ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.

%package -n mingw32-admesh-static
Summary:       Static version of the MinGW Win32 compiled ADMesh
Requires:      mingw32-admesh = %{version}-%{release}

%description -n mingw32-admesh-static
Static version of the MinGW compiled ADMesh for the Win32 target.

ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.

# Win64
%package -n mingw64-admesh
Summary:       MinGW compiled ADMesh for the Win64 target

%description -n mingw64-admesh
MinGW compiled ADMesh for the Win64 target.

ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.

%package -n mingw64-admesh-static
Summary:       Static version of the MinGW Win64 compiled ADMesh
Requires:      mingw64-admesh = %{version}-%{release}

%description -n mingw64-admesh-static
Static version of the MinGW compiled ADMesh for the Win64 target.

ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.


%{?mingw_debug_package}


%prep
%setup -q -n admesh-%{version}


%build
%mingw_configure --enable-static
%mingw_make %{?_smp_mflags} LIBTOOLFLAGS="-v"


%install
%mingw_make_install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{mingw64_datadir}
rm -rf %{buildroot}%{mingw32_datadir}

# Libtool files don't need to be bundled
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-admesh
%doc ChangeLog ChangeLog.old COPYING README.md AUTHORS
%doc admesh-doc.txt block.stl
%{mingw32_bindir}/libadmesh-1.dll
%{mingw32_bindir}/admesh.exe
%{mingw32_includedir}/admesh/
%{mingw32_libdir}/libadmesh.dll.a
%{mingw32_libdir}/pkgconfig/libadmesh.pc

%files -n mingw32-admesh-static
%doc COPYING AUTHORS
%{mingw32_libdir}/libadmesh.a

# Win64
%files -n mingw64-admesh
%doc ChangeLog ChangeLog.old COPYING README.md AUTHORS
%doc admesh-doc.txt block.stl
%{mingw64_bindir}/libadmesh-1.dll
%{mingw64_bindir}/admesh.exe
%{mingw64_includedir}/admesh/
%{mingw64_libdir}/libadmesh.dll.a
%{mingw64_libdir}/pkgconfig/libadmesh.pc

%files -n mingw64-admesh-static
%doc COPYING AUTHORS
%{mingw64_libdir}/libadmesh.a

%changelog
* Tue Jul 29 2014 Miro Hrončok <mhroncok@redhat.com> - 0.98.0-1
- Initial package
