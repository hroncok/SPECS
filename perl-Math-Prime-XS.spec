Name:           perl-Math-Prime-XS
Version:        0.26
Release:        4%{?dist}
Summary:        Detect and calculate prime numbers with deterministic tests
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Prime-XS/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-Prime-XS-%{version}.tar.gz
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Test::Pod) >= 1.14
Requires:       perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
Math::Prime::XS detects and calculates prime numbers by either applying
Modulo operator division, the Sieve of Eratosthenes, a Summation
calculation or Trial division.

%prep
%setup -q -n Math-Prime-XS-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test


%files
%doc Changes devel META.json README xt
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.26-4
- Removed BRs provided by perl package

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 0.26-3
- Rebuilding for 32bit, no spec changes.

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 0.26-2
- Removed useless require.

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 0.26-1
- Specfile autogenerated by cpanspec 1.78 and revised.
