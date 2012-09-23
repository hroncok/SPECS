Name:           perl-Math-NumSeq
Version:        51
Release:        1%{?dist}
Summary:        Number sequences
License:        GPLv3+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-NumSeq/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-NumSeq-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.004
BuildRequires:  perl(constant)
BuildRequires:  perl(constant::defer) >= 1
BuildRequires:  perl(warnings)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Factor::XS) >= 0.40
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::Prime::XS) >= 0.23
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::ConsistentVersion)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::YAML::Meta)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Math::Symbolic)
BuildRequires:  perl(Math::Expression::Evaluator)
BuildRequires:  perl(Language::Expr)
BuildRequires:  perl(Language::Expr::Compiler::Perl)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(SDBM_File)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
Requires:       perl(File::HomeDir)
Requires:       perl(Module::Load)
Requires:       perl(Math::Trig)
Requires:       perl(Math::Symbolic)
Requires:       perl(Math::Expression::Evaluator)
Requires:       perl(Language::Expr)
Requires:       perl(Language::Expr::Compiler::Perl)
Requires:       perl(SDBM_File)
Requires:       perl(File::Temp)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
This is a base class for some number sequences. Sequence objects can
iterate through values and some sequences have random access and/or
predicate test.

%prep
%setup -q -n Math-NumSeq-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING
#%{perl_vendorlib}/auto/*
%{perl_vendorlib}/Math/*
%{_mandir}/man3/*

%changelog
* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 51-1
- Specfile autogenerated by cpanspec 1.78 and revised.
