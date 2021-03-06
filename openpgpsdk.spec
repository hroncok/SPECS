Name:           openpgpsdk
Version:        0.9
Release:        1%{?dist}
Summary:        OpenPGP library
License:        ASL 2.0
URL:            http://openpgp.nominet.org.uk
Source0:        %{url}/downloads/%{name}-%{version}.tgz
Patch0:         %{name}-sharedlib.patch
Patch1:         %{name}-multidef.patch
Patch2:         %{name}-c++-compat.patch

BuildRequires:  bzip2-devel
BuildRequires:  CUnit-devel
BuildRequires:  gnupg
BuildRequires:  openssl-devel

%description
The OpenPGP SDK project provides an open source library, written in C,
which implements the OpenPGP specification.

%package devel
Summary: OpenPGP SDK development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for x.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i 's|-Wall -Werror -W -g|%{optflags}|g' configure
sed -i 's|-Wall -Werror -g|%{optflags}|g' src/app/Makefile.template tests/Makefile.template

%build
./configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cp -prP include/* %{buildroot}%{_includedir}
cp -p lib/libops.so.1.0 %{buildroot}%{_libdir}
ln -s libops.so.1.0 %{buildroot}%{_libdir}/libops.so
ln -s libops.so.1.0 %{buildroot}%{_libdir}/libops.so.1

%check
cd tests
# tests will fail due to new gnupg
# http://openpgp.nominet.org.uk/pipermail/openpgpsdk-dev/2010-May/000238.html
LD_LIBRARY_PATH=../lib ./tests | :
cd -

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc Licence
%{_libdir}/*so.*

%files devel
%doc Licence
%{_includedir}/*
%{_libdir}/*so

%changelog
* Fri Jul 05 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9-1
- New package

