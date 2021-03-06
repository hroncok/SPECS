Name:           perl-IO-Socket-PortState
Version:        0.03
Release:        2%{?dist}
Summary:        Perl extension for checking the open or closed status of a port
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/IO-Socket-PortState/
Source0:        http://www.cpan.org/authors/id/D/DM/DMUEY/IO-Socket-PortState-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
You can use it to check if a port is open or closed for a given host
and protocol.

%prep
%setup -q -n IO-Socket-PortState-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.03-2
- Adding missing BRs, as suggested by package reviewer (#974077)

* Thu Jun 13 2013 Miro Hrončok <mhroncok@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78 and revised
