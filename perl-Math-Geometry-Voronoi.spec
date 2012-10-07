Name:           perl-Math-Geometry-Voronoi
Version:        1.3
Release:        2%{?dist}
Summary:        Compute Voronoi diagrams from sets of points
License:        GPL+ or Artistic
# TODO contact Steve and Derek about the license
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Geometry-Voronoi/
Source0:        http://www.cpan.org/authors/id/S/SA/SAMTREGAR/Math-Geometry-Voronoi-%{version}.tar.gz
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  glibc-devel
Requires:       perl(Class::Accessor)
Requires:       perl(List::Util)
Requires:       perl(Params::Validate)
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
This module computes Voronoi diagrams from a set of input points. Info on
Voronoi diagrams can be found here:

%prep
%setup -q -n Math-Geometry-Voronoi-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 1.3-2
- Rebuilding for 32bit, no spec changes.

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 1.3-1
- Specfile autogenerated by cpanspec 1.78 and revised.
