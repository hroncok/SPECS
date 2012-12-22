Name:           perl-Math-Geometry-Voronoi
Version:        1.3
Release:        7%{?dist}
Summary:        Compute Voronoi diagrams from sets of points
License:        (GPL+ or Artistic) and MIT
# Perl module is licensed as Perl, underlaying C code is MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Geometry-Voronoi/
Source0:        http://www.cpan.org/authors/id/S/SA/SAMTREGAR/Math-Geometry-Voronoi-%{version}.tar.gz
Source1:        Math-Geometry-Voronoi-license-mail1.txt
Source2:        Math-Geometry-Voronoi-license-mail2.txt
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  dos2unix
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
This module computes Voronoi diagrams from a set of input points.

%prep
%setup -q -n Math-Geometry-Voronoi-%{version}
cp -p %{SOURCE1} license-mail1.txt
cp -p %{SOURCE2} license-mail2.txt
dos2unix *.c
chmod -x *.c *.h

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
# Get the license from the e-mail
tail -22 license-mail1.txt | head -20 | base64 -d | dos2unix > C-LICENSE

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}%{perl_vendorarch}/Math/Geometry/leak-test.pl

%check
make test

%files
%doc Changes C-LICENSE README license-mail*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Sat Dec 22 2012 Miro Hrončok <miro@hroncok.cz> - 1.3-7
- Changed %%{__perl} to perl
- Added BR: perl(base)
- Changed BR perl(Class::Accessor) to perl(Class::Accessor::Fast)
- Recoded newlines: C-LICENCE, second mail and *.c
- Removed executable perms from sources and group write perms from e-mails

* Mon Dec 17 2012 Miro Hrončok <miro@hroncok.cz> - 1.3-6
- Removed accidentally added BRs

* Mon Dec 17 2012 Miro Hrončok <miro@hroncok.cz> - 1.3-5
- Removed directly listed Requires
- Removed glibc-devel BR

* Mon Dec 17 2012 Miro Hrončok <miro@hroncok.cz> - 1.3-4
- Added BRs again.
- Added e-mails about the license and adapted the spec
- PERL_INSTALL_ROOT changed to DESTDIR
- Removed deleting empty directories

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.3-3
- Removed BRs provided by perl package

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 1.3-2
- Rebuilding for 32bit, no spec changes.

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 1.3-1
- Specfile autogenerated by cpanspec 1.78 and revised.
