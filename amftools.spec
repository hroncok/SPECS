Name:           amftools
Version:        0.0
%global         svn svn32
%global         snapshot 20121220%{svn}
Release:        2.%{snapshot}%{?dist}
Summary:        AMF file library
# License is in files
License:        LGPLv3+
URL:            https://sourceforge.net/projects/%{name}/
# svn export svn://svn.code.sf.net/p/%%{name}/code/trunk %%{name}
# tar -pczf %%{name}-%%{svn}.tar.gz %%{name}
Source0:        %{name}-%{svn}.tar.gz
Source1:        %{name}-Makefile
BuildRequires:  mesa-libGL-devel, libzip-devel, muParser-devel, stbi-devel, rapidxml-devel

%description
C++ tools for implementing AMF file format for the interchange of geometry
for 3D printing (additive manufacturing).

%package devel
Summary: AMF tools development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for AMF tools.

%prep
%setup -qn %{name}
cp %{SOURCE1} Makefile

# Bundling
rm -rf */muparser */stb_image include/rapidxml */zip
sed -i 's|muparser/muParser.h|muParser.h|g' include/Equation.h
sed -i 's|stb_image/stb_image.h|stb_image.h|g' src/SimpleImage.cpp
sed -i 's|rapidxml/||g' include/XmlStream.h src/XmlStream.cpp

%build
make %{?_smp_mflags}

%install
install -Dpm0755 libamf.so.0.0 %{buildroot}%{_libdir}/libamf.so.0.0
ln -s libamf.so.0.0 %{buildroot}%{_libdir}/libamf.so.0
ln -s libamf.so.0.0 %{buildroot}%{_libdir}/libamf.so
mkdir -p %{buildroot}%{_includedir}
cp -arp include %{buildroot}%{_includedir}/amf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libamf.so.*

%files devel
%{_libdir}/libamf.so
%{_includedir}/amf

%changelog
* Wed Apr 24 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-2.20121220svn32
- Soname version 0.0.0 -> 0.0
- Removing include/zip in %%prep, as it works fine
- Added -lmuparser to Makefile

* Fri Feb 01 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20121220svn32
- Started

