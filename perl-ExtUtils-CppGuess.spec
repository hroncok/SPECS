Name:           perl-ExtUtils-CppGuess
Version:        0.07
Release:        1%{?dist}
Summary:        Guess C++ compiler and flags
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-CppGuess/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-CppGuess-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
ExtUtils::CppGuess attempts to guess the system's C++ compiler that is
compatible with the C compiler that your perl was built with.

%prep
%setup -q -n ExtUtils-CppGuess-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
#%%{perl_vendorlib}/auto/*
%{perl_vendorlib}/ExtUtils*
%{_mandir}/man3/*

%changelog
* Mon Oct 01 2012 Miro Hrončok <miro@hroncok.cz> 0.07-1
- Specfile autogenerated by cpanspec 1.78 and revised.
