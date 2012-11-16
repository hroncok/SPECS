Name:           slic3r
Version:        0.9.5
Release:        1%{?dist}
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPLv3 and CC-BY
# Images are CC-BY, code is AGPLv3
Group:          Applications/Engineering
URL:            http://slic3r.org/
# git clone git://github.com/alexrj/Slic3r.git && cd Slic3r
# git archive %{version} --format tar.gz > ../%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

%global         additional https://raw.github.com/hroncok/RPMAdditionalSources/master/
# Bash runners
Source1:        %{additional}%{name}
# Desktop files
Source2:        %{additional}%{name}.desktop

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
BuildRequires:  desktop-file-utils
Requires:       perl(XML::SAX)
Requires:       perl(Growl::GNTP)
Requires:       perl(Net::DBus)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# There is no such module on CPAN and it works like a charm without it
%filter_from_requires /perl(Wx::Dialog)/d
# This is provided by XML::SAX (but not statet there)
%filter_from_requires /perl(XML::SAX::PurePerl)/d
%filter_setup

%{?perl_default_filter} # Filters (not)shared c libs

%description
Slic3r is a G-code generator for 3D printers. It's compatible with RepRaps,
Makerbots, Ultimakers and many more machines.
See the project homepage at slic3r.org and the documentation on the Slic3r wiki
for more information.

%prep
%setup -cq

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{__mkdir} -p %{buildroot}%{_datadir}/%{name}
%{__cp} %{SOURCE1} %{buildroot}%{_bindir}
%{__mv} -f %{buildroot}%{_bindir}/%{name}.pl %{buildroot}%{_datadir}/%{name}
%{__cp} -ar var %{buildroot}%{_datadir}/%{name}
%{__mkdir} -p %{buildroot}%{_datadir}/pixmaps # /usr/share/pixmaps
%{__ln_s} ../%{name}/var/Slic3r.ico %{buildroot}%{_datadir}/pixmaps/%{name}.ico
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2} # desktop file

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
* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 0.9.5-1
- New version
- Requires perl(Math::Clipper) >= 1.14
- Requires perl(Math::ConvexHull::MonotoneChain)
- Requires perl(XML::SAX::ExpatXS)

* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 0.9.3-1
- New package
