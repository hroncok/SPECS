Name:           perl-ExtUtils-ParseXS
Version:        3.15
Release:        12%{?dist}
Summary:        Converts Perl XS code into C code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-ParseXS/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(ExtUtils::CBuilder)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       xsubpp = %{version}

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and creates
the glue necessary to let Perl access those functions. The compiler uses
typemaps to determine how to map C function parameters and variables to
Perl values.

%prep
%setup -q -n ExtUtils-ParseXS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# wrong shebang correction
sed -i 's|#!perl|#!/usr/bin/perl|' %{buildroot}%{perl_vendorlib}/ExtUtils/xsubpp

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes META.json README
#%%{perl_vendorlib}/auto/*
%{perl_vendorlib}/ExtUtils*
%attr(755,root,root) %{perl_vendorlib}/ExtUtils/xsubpp
%{_mandir}/man1/*
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/*

%changelog
* Mon Nov 19 2012 Miro Hrončok <miro@hroncok.cz> - 3.15-12
- Removed useless Requires and BR
- Removed perl autofilter

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 3.15-11
- Removed BRs provided by perl package

* Tue Sep 28 2012 Miro Hrončok <miro@hroncok.cz> 3.15-10
- Release changed to 10, so i can update.

* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 3.15-1
- Specfile autogenerated by cpanspec 1.78.
