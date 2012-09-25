Name:           perl-Lingua-EN-Numbers-Easy
Version:        2009110701
Release:        1%{?dist}
Summary:        Hash access to Lingua::EN::Numbers objects
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Lingua-EN-Numbers-Easy/
Source0:        http://www.cpan.org/authors/id/A/AB/ABIGAIL/Lingua-EN-Numbers-Easy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Lingua::EN::Numbers) >= 1.01
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
Lingua::EN::Numbers is a module that translates numbers to English words.
Unfortunately, it has an object oriented interface, which makes it hard to
interpolate them in strings. Lingua::EN::Numbers::Easy translates numbers
to words using a tied hash, which can be interpolated.

%prep
%setup -q -n Lingua-EN-Numbers-Easy-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 2009110701-1
- Specfile autogenerated by cpanspec 1.78.
