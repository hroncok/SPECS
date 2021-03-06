Name:           perl-Boost-Geometry-Utils
Version:        0.06
Release:        1%{?dist}
Summary:        Boost::Geometry::Utils Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Boost-Geometry-Utils/
Source0:        http://www.cpan.org/authors/id/A/AA/AAR/Boost-Geometry-Utils-%{version}.tar.gz
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Typemaps::Default)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::WithXSpp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter} # Filters (not)shared c libs

%description
Boost::Geometry::Utils Perl module

%prep
%setup -q -n Boost-Geometry-Utils-%{version}

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
%doc CHANGES LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Boost*
%{_mandir}/man3/*

%changelog
* Wed Apr 03 2013 Miro Hrončok <mhroncok@redhat.com> - 0.06-1
- New upstream release

* Fri Jan 18 2013 Miro Hrončok <mhroncok@redhat.com> - 0.05-6
- Added back:  perl(ExtUtils::Typemaps::Default)

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.05-5
- Dropped perl macro in MODULE_COMPAT
- Removed src and xsp from %%doc
- Dropped converting src to UTF-8
- Dropped converting newlines and dos2unix BR
- Dropped BRs: perl(ExtUtils::Typemaps::Default)
               perl(ExtUtils::XSpp)
               perl(Module::Build)
- Added BRs:   perl(File::Temp)
               perl(Exporter)
               perl(XSLoader)

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.05-4
- Using dos2unix instead of sed
- Removed deleting empty dirs
- Dropped perl macro

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.05-3
- Removed BRs provided by perl package

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 0.05-2
- Rebuilding for 32bit, no spec changes.

* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
