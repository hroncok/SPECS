Name:           perl-Lingua-EN-Numbers
Version:        1.04
Release:        2%{?dist}
Summary:        Turn "407" into "four hundred and seven", etc
License:        GPLv2
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Lingua-EN-Numbers/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/Lingua-EN-Numbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Lingua::EN::Numbers turns numbers into English text. It exports (upon
request) two functions, num2en and num2en_ordinal. Each takes a scalar
value and returns a scalar value. The return value is the English text
expressing that number; or if what you provided wasn't a number, then they
return undefined.

%prep
%setup -q -n Lingua-EN-Numbers-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.04-2
- Removed BRs provided by perl package
- Removed perl autofilter
- Added Test::More

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 1.04-1
- Specfile autogenerated by cpanspec 1.78.
