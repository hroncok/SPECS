Name:           perl-XML-SAX-ExpatXS
Version:        1.33
Release:        2%{?dist}
Summary:        Perl SAX 2 XS extension to Expat parser
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-SAX-ExpatXS/
Source0:        http://www.cpan.org/authors/id/P/PC/PCIMPRICH/XML-SAX-ExpatXS-%{version}.tar.gz
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XML::SAX) >= 0.96
BuildRequires:  perl(Carp)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  expat-devel
Requires:       perl(XML::SAX) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
XML::SAX::ExpatXS is a direct XS extension to Expat XML parser. It
implements Perl SAX 2.1 interface. See http://perl-xml.sourceforge.net/perl-
sax/ for Perl SAX API description. Any deviations from the Perl SAX 2.1
specification are considered as bugs.

%prep
%setup -q -n XML-SAX-ExpatXS-%{version}
chmod -x ExpatXS.xs

%build
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/XML*
%{_mandir}/man3/*

%changelog
* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.33-2
- Removed BRs provided by perl package

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 1.33-1
- Specfile autogenerated by cpanspec 1.78 and revised.
