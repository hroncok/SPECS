Name:           poly2tri
Version:        0.0
%global         rev acf81f1f1764
%global         date 20120407
%global         snapshot %{date}hg%{rev}
Release:        1.%{snapshot}%{?dist}
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD
URL:            https://code.google.com/p/%{name}
# hg clone %%{url}
# rm -rf %%{name}/.hg
# tar -pczf %%{name}-%%{rev}.tar.gz %%{name}
Source0:        %{name}-%{rev}.tar.gz
Source1:        %{name}-Makefile
BuildRequires:  mesa-libGL-devel

%description
Library based on the paper "Sweep-line algorithm for constrained Delaunay
triangulation" by V. Domiter and and B. Zalik.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -qn %{name}
cp %{SOURCE1} %{name}/Makefile
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS

%build
cd %{name}
make %{?_smp_mflags}
cd -

%install
install -Dpm0755 %{name}/lib%{name}.so.0.0.0 %{buildroot}%{_libdir}/lib%{name}.so.0.0.0
ln -s lib%{name}.so.0.0.0 %{buildroot}%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0.0.0 %{buildroot}%{_libdir}/lib%{name}.so

for H in %{name}/*/*.h %{name}/*.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
* Mon Feb 04 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20120407hgacf81f1f1764
- Started
