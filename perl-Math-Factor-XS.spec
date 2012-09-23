Name:           perl-Math-Factor-XS
Version:        0.40
Release:        1%{?dist}
Summary:        Factorize numbers and calculate matching multiplications
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Factor-XS/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-Factor-XS-%{version}.tar.gz
BuildRequires:  perl(boolean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(XSLoader)
Requires:       perl(Test::Pod) >= 1.14
Requires:       perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
Math::Factor::XS factorizes numbers by applying trial divisions.

%prep
%setup -q -n Math-Factor-XS-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
# Dirty hack for F17
%if 0%{?fedora} < 18
  sed -i 's/q{0.40}/q{0.38}/' Build
%endif
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes META.json README scripts
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 0.40-1
- Specfile autogenerated by cpanspec 1.78 and revised.