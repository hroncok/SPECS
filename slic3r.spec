Name:           slic3r
Version:        0.9.7
Release:        3%{?dist}
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPLv3 and CC-BY
# Images are CC-BY, code is AGPLv3
Group:          Applications/Engineering
URL:            http://slic3r.org/
%global commit 452b62e53d449ebfca00922f7cc3319f291f0afb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/alexrj/Slic3r/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Bash runners
Source1:        %{name}
# Desktop files
Source2:        %{name}.desktop
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Math::Clipper) >= 1.14
BuildRequires:  perl(Moo) >= 0.091009
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Math::ConvexHull) >= 1.0.4
BuildRequires:  perl(Math::ConvexHull::MonotoneChain)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::ExpatXS)
BuildRequires:  perl(Math::PlanePath)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SVG)
BuildRequires:  perl(parent)
BuildRequires:  perl(Wx)
BuildRequires:  perl(Boost::Geometry::Utils)
BuildRequires:  perl(Math::Geometry::Voronoi)
BuildRequires:  perl(Growl::GNTP)
BuildRequires:  perl(Net::DBus)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  desktop-file-utils
Requires:       perl(XML::SAX)
Requires:       perl(Growl::GNTP)
Requires:       perl(Net::DBus)
Requires:       perl(Math::Clipper) >= 1.14
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# There is no such module on CPAN and it works like a charm without it
%filter_from_requires /perl(Wx::Dialog)/d
# This is provided by XML::SAX (but not stated there)
%filter_from_requires /perl(XML::SAX::PurePerl)/d
%filter_setup

%{?perl_default_filter} # Filters (not)shared c libs

%description
Slic3r is a G-code generator for 3D printers. It's compatible with RepRaps,
Makerbots, Ultimakers and many more machines.
See the project homepage at slic3r.org and the documentation on the Slic3r wiki
for more information.

%prep
%setup -qn Slic3r-%{commit}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp %{SOURCE1} %{buildroot}%{_bindir}
mv -f %{buildroot}%{_bindir}/%{name}.pl %{buildroot}%{_datadir}/%{name}
cp -ar var %{buildroot}%{_datadir}/%{name}
ln -s ../%{name}/var/Slic3r.ico %{buildroot}%{_datadir}/pixmaps/%{name}.ico
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc MANIFEST README.markdown
%attr(755,root,root) %{_bindir}/%{name}
%{perl_vendorlib}/Slic3r*
%{_datadir}/pixmaps/%{name}.ico
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man3/*

%changelog
* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-3
- Updated source to respect GitHub rule
- Dropped mkdir, ln -s, cp, mv, perl macros
- Reorganized %%install section a bit
- Added version to Require perl(Math::Clipper)

* Sat Jan 05 2013 Miro Hrončok <miro@hroncok.cz> - 0.9.7-2
- Added Require perl(Math::Clipper)

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.9.7-1
- New version
- Do not download additional sources from GitHub
- Removed deleting empty directories

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.9.5-2
- Removed BRs provided by perl package

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 0.9.5-1
- New version
- Requires perl(Math::Clipper) >= 1.14
- Requires perl(Math::ConvexHull::MonotoneChain)
- Requires perl(XML::SAX::ExpatXS)

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 0.9.3-1
- New package
