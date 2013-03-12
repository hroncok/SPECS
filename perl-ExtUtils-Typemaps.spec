Name:           perl-ExtUtils-Typemaps
Version:        3.18
Release:        5%{?dist}
Summary:        Reads, modifies, creates and writes Perl XS typemap files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-ParseXS/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
ExtUtils::Typemaps can read, modify, create and write Perl XS typemap files.

The module is not entirely round-trip safe: For example it currently simply
strips all comments. The order of entries in the maps is, however, preserved.

We check for duplicate entries in the typemap, but do not check for missing
TYPEMAP entries for INPUTMAP or OUTPUTMAP entries since these might be hidden
in a different typemap.

%prep
%setup -q -n ExtUtils-ParseXS-%{version}
# Remove ExtUtils::ParseXS parts from this package, keep the rest
# This means ExtUtils::Typemaps and ExtUtils::ParseXS::* stay
rm -f lib/ExtUtils/ParseXS.* lib/ExtUtils/xsubpp

# Modifiy Makefile.PL to successfully compile without removed parts
sed -i 's/ExtUtils::ParseXS/ExtUtils::Typemaps/' Makefile.PL
sed -i 's/ParseXS.pm/Typemaps.pm/' Makefile.PL
sed -i "s|ABSTRACT_FROM  => 'lib/ExtUtils/ParseXS.pod',||" Makefile.PL
sed "/lib\/ExtUtils\/xsubpp/d" Makefile.PL > Makefile.PL.tmp && mv -f Makefile.PL.tmp Makefile.PL

# Remove ExtUtils::ParseXS specific tests, keep others
for FILE in t/*.t; do
  grep -q "ExtUtils::ParseXS::" $FILE || grep -q "ExtUtils::Typemaps" $FILE || rm -f $FILE
done
rm -f t/002-more.t t/114-blurt_death_Warn.t

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes META.json README
#%%{perl_vendorlib}/auto/*
%{perl_vendorlib}/ExtUtils/ParseXS
%{perl_vendorlib}/ExtUtils/Typemaps*
%{_mandir}/man3/*

%changelog
* Mon Feb 18 2013 Miro Hrončok <mhroncok@redhat.com> - 3.18-5
- More tests testing ParseXS removed

* Fri Feb 08 2013 Miro Hrončok <mhroncok@redhat.com> - 3.18-4
- %%{_perl} to perl
- Updated comments
- Updated bogus date in %%changelog
- %%{perl_vendorlib}/ExtUtils/ParseXS* - removed asterisk, it is 1 dir
- Remove tests in much more cooler way

* Fri Jan 04 2013 Miro Hrončok <miro@hroncok.cz> - 3.18-3
- Forked from perl-ExtUtils-ParseXS
- Removed ExtUtils::ParseXS module and tests
- Removed BRs no longer needed

* Thu Dec 06 2012 Miro Hrončok <miro@hroncok.cz> - 3.18-2
- Added missing BR for tests
- Removed deleting empty dirs
- Replaced obsoleted PERL_INSTALL_ROOT with DESTDIR
- Updated %%files to prevent duplicity

* Mon Nov 19 2012 Miro Hrončok <miro@hroncok.cz> - 3.18-1
- New release

* Mon Nov 19 2012 Miro Hrončok <miro@hroncok.cz> - 3.15-12
- Removed useless Requires and BR
- Removed perl autofilter

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 3.15-11
- Removed BRs provided by perl package

* Fri Sep 28 2012 Miro Hrončok <miro@hroncok.cz> 3.15-10
- Release changed to 10, so i can update.

* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 3.15-1
- Specfile autogenerated by cpanspec 1.78.
