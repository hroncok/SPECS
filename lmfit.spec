Name:           lmfit
Version:        3.5
Release:        1%{?dist}
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

%build
%{configure}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.la %{buildroot}%{_mandir}/html %{buildroot}%{_bindir}/*

%check
rm -rf demo/.libs demo/*.o # compiled examples

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
* Sun Feb 03 2013 Miro Hrončok <mhroncok@redhat.com> - 3.5-1
- Initial package
