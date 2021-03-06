Name:           perl-ExtUtils-Typemaps-Default
Version:        1.01
Release:        3%{?dist}
Summary:        Set of useful typemaps
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-Typemaps-Default/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::Typemaps) >= 1.00
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(ExtUtils::Typemaps) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Filtering unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ExtUtils::Typemaps\\)$

%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps subclass that provides
a set of default mappings (in addition to what perl itself provides). These
default mappings are currently defined as the combination of the mappings
provided by the following typemap classes which are provided in this
distribution:

ExtUtils::Typemaps::ObjectMap
ExtUtils::Typemaps::STL
ExtUtils::Typemaps::Basic

%prep
%setup -q -n ExtUtils-Typemaps-Default-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jan 06 2013 Miro Hrončok <miro@hroncok.cz> - 1.01-3
- Removed deleting empty dirs
- Removed META.json from doc
- Filtered unversioned requires

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.01-2
- Removed BRs provided by perl package
- Removed perl autofilter

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 1.01-1
- New version.
- Longer description.

* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 1.00-1
- Specfile autogenerated by cpanspec 1.78 and revised.
