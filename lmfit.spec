Name:           lmfit
Version:        3.5
Release:        2%{?dist}
Summary:        Levenberg-Marquardt least-squares minimization and curve fitting
# software is BSD, documentation is CC-BY
License:        BSD and CC-BY
URL:            http://joachimwuttke.de/%{name}/
Source0:        http://joachimwuttke.de/src/%{name}-%{version}.tgz

%description
C/C++ library for Levenberg-Marquardt least-squares minimization and curve
fitting

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q
cp -ra demo _demo

%build
%{configure} --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_mandir}/html %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/*.la
rm -rf demo
mv -f _demo demo

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING CHANGELOG man/lmfit.html demo
%{_libdir}/*so.*
%{_mandir}/man3/*

%files devel
%{_includedir}/*
%{_libdir}/*so

%changelog
* Mon Feb 04 2013 Miro Hrončok <mhroncok@redhat.com> - 3.5-2
- Do not package demo binaries to %%doc
- Added --disable-static to configure

* Sun Feb 03 2013 Miro Hrončok <mhroncok@redhat.com> - 3.5-1
- Initial package
