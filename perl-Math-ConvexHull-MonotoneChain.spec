Name:           perl-Math-ConvexHull-MonotoneChain
Version:        0.01
Release:        3%{?dist}
Summary:        Monotone chain algorithm for finding a convex hull in 2D
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-ConvexHull-MonotoneChain/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/Math-ConvexHull-MonotoneChain-%{version}.tar.gz
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(XSLoader)

%{?perl_default_filter} # Filters (not)shared c libs

%description
This is somewhat experimental still.

This (XS) module optionally exports a single function C<convex_hull>
which calculates the convex hull of the input points and returns it.
The algorithm is C<O(n log n)> due to having to sort the input list,
but should be somewhat faster than a plain Graham's scan (also C<O(n log n)>)
in practice since it avoids polar coordinates.

%prep
%setup -q -n Math-ConvexHull-MonotoneChain-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes META.json
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.01-3
- PERL_INSTALL_ROOT changed to DESTDIR
- Removed the deleting empty directories
- Removed Andrew from summary
- Added BR Exporter back

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.01-2
- Removed BRs provided by perl package

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 0.01-1
- Specfile autogenerated by cpanspec 1.78 and revised.
