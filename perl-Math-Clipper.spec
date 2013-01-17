Name:           perl-Math-Clipper
Version:        1.17
Release:        2%{?dist}
Summary:        Perl wrapper around Clipper library
License:        Boost
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Clipper/
Source0:        http://www.cpan.org/authors/id/A/AA/AAR/Math-Clipper-%{version}.tar.gz
Patch0:         %{name}-1.16-1.no-c-sources.patch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 0.05
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.10
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  polyclipping-devel >= 5.0.3
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
Perl module Math::Clipper is a wrapper around a Clipper library
that implements polygon clipping.

%prep
%setup -q -n Math-Clipper-%{version}
%patch0 -p1
rm -f src/clipper.{c,h}pp

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 1.17-2
- %%{__perl} to perl
- dropped perl(Module::Build) BR

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 1.17-1
- New release
- Wants newer polyclipping

* Thu Jan 03 2013 Miro Hrončok <miro@hroncok.cz> - 1.16-2
- Removed META.json and xsp from doc
- Specified version for polyclipping-devel BR
- Specified version for perl(Module::Build::WithXSpp) BR
- Removed perl(ExtUtils::XSpp) BR
- Added BRs perl(XSLoader) and perl(constant)

* Fri Dec 28 2012 Miro Hrončok <miro@hroncok.cz> - 1.16-1
- New version
- Removed boundled C clipper and using the distribution one
- Removed no longer needed dos2unix

* Mon Dec 17 2012 Miro Hrončok <miro@hroncok.cz> - 1.15-1
- New version
- Added perl(Config) and perl(Exporter) to BRs
- Removed deleting empty directories
- using dos2unix instead of sed

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.14-2
- Removed BRs provided by perl package

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 1.14-1
- New version.

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 1.09-2
- Rebuilding for 32bit, no spec changes.

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 1.09-1
- Specfile autogenerated by cpanspec 1.78 and revised.
