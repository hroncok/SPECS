Name:           poly2tri
Version:        0.0
%global         rev acf81f1f1764
%global         date 20120407
%global         snapshot %{date}hg%{rev}
Release:        4.%{snapshot}%{?dist}
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD
URL:            https://code.google.com/p/%{name}
# hg clone %%{url}
# rm -rf %%{name}/.hg
# tar -pczf %%{name}-%%{rev}.tar.gz %%{name}
Source0:        %{name}-%{rev}.tar.gz
# The Makefile was created for purposes of this package
# Upstream provides WAF, but it builds example apps and not the library
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

iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
touch -r AUTHORS AUTHORS.conv && \
mv AUTHORS.conv AUTHORS

%build
cd %{name}
CFLAGS="%{optflags}" make %{?_smp_mflags}
cd -

%install
install -Dpm0755 %{name}/lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so.1.0
ln -s lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so

for H in %{name}/*/*.h %{name}/*.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
* Wed Mar 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-4.20120407hgacf81f1f1764
- Using soname version 1.0
- Corrected Makefile to actually produce the library with soname version 1.0
- Added comment about the Makefile

* Wed Mar 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-3.20120407hgacf81f1f1764
- Using soname version 1.0.0 as upstream suggests so: http://code.google.com/p/poly2tri/issues/detail?id=66#c1

* Thu Mar 07 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-2.20120407hgacf81f1f1764
- Preserve AUTHORS timestamp
- Use %%{optflags}
- Add a comment about Makefile
- Added doc to -devel package

* Mon Feb 04 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20120407hgacf81f1f1764
- Started
