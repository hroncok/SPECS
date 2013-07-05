Name:           openpgpsdk
Version:        0.9
Release:        1%{?dist}
Summary:        x
License:        ALV 2.0
URL:            http://openpgp.nominet.org.uk
Source0:        %{url}/downloads/%{name}-%{version}.tgz
Patch0:         %{name}-sharedlib.patch
Patch1:         %{name}-multidef.patch

BuildRequires:  CUnit-devel

%description
x

%package devel
Summary: x development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for x.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
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
* Fri Jul 05 2013 Miro Hrončok <mhroncok@redhat.com>
- New package

