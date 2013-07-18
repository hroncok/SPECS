Name:           perl-Wx-GLCanvas
Version:        0.09
Release:        2%{?dist}
Summary:        Interface to wxWidgets' OpenGL canvas
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Wx-GLCanvas/
Source0:        http://www.cpan.org/authors/id/M/MB/MBARBON/Wx-GLCanvas-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl(Alien::wxWidgets)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Wx::build::MakeMaker) >= 0.16
BuildRequires:  wxGTK-devel

%if 0%{?with_tests}
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NeedsDisplay)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Wx)
BuildRequires:  perl(Wx::ScrolledWindow)
BuildRequires:  xorg-x11-server-Xvfb
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
A wrapper for wxWidgets' wxGLCanvas, used to display OpenGL graphics.

%prep
%setup -q -n Wx-GLCanvas-%{version}
rm -rf wx

chmod -x Changes README.txt

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -I/usr/include/wx-2.8"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%if 0%{?with_tests}
%check
DISPLAY=:0.0 make test
%endif

%files
%doc Changes README.txt
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Wx*
%{_mandir}/man3/*

%changelog
* Thu Jul 04 2013 Miro Hrončok <mhroncok@redhat.com> - 0.09-2
- Redone BRs

* Tue Jun 25 2013 Miro Hrončok <mhroncok@redhat.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78 and revised
