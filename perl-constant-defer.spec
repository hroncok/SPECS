Name:           perl-constant-defer
Version:        5
Release:        1%{?dist}
Summary:        Constant subs with deferred value calculation
License:        GPLv3+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/constant-defer/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/constant-defer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(Test::DistManifest)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Pod::Simple::HTML)
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Smart::Comments)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Glib)
BuildRequires:  perl(B)
BuildRequires:  perl(B::Utils)
BuildRequires:  perl(Devel::Peek)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       perl(Carp)
# in inc   (ask if needed here)
Requires:       perl(Pod::Simple::HTML)
# in devel (ask if needed here)
Requires:       perl(Scalar::Util)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::Dump)
Requires:       perl(Devel::FindRef)
Requires:       perl(Attribute::Handlers)
Requires:       perl(Smart::Comments)
Requires:       perl(FindBin)
Requires:       perl(Test::NoWarnings)
Requires:       perl(POSIX)
Requires:       perl(Sub::Identify)
Requires:       perl(Glib)
Requires:       perl(B::Utils)
Requires:       perl(B)
Requires:       perl(Devel::Peek)

%{?perl_default_filter} # Filters (not)shared c libs

%description
constant::defer creates a subroutine which on the first call runs given
code to calculate its value, and on the second and subsequent calls just
returns that value, like a constant. The value code is discarded once run,
allowing it to be garbage collected.

%prep
%setup -q -n constant-defer-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 5-1
- Specfile autogenerated by cpanspec 1.78 and revision made.
