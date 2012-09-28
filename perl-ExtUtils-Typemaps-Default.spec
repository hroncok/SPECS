Name:           perl-ExtUtils-Typemaps-Default
Version:        1.00
Release:        1%{?dist}
Summary:        Set of useful typemaps
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-Typemaps-Default/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::Typemaps) >= 1.00
BuildRequires:  perl(Module::Build)
Requires:       perl(ExtUtils::Typemaps) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps subclass that provides
a set of default mappings (in addition to what perl itself provides). These
default mappings are currently defined as the combination of the mappings
provided by the following typemap classes which are provided in this
distribution:

%prep
%setup -q -n ExtUtils-Typemaps-Default-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 1.00-1
- Specfile autogenerated by cpanspec 1.78 and revised.
