Name:           slic3r
Version:        0.9.3
Release:        1%{?dist}
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPLv3 and CC-BY
Group:          Applications/Engineering
URL:            http://slic3r.org/
# git clone git://github.com/alexrj/Slic3r.git && cd Slic3r
# git archive %{version} --format tar.gz > ../%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(constant)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Math::Clipper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moo) >= 0.091009
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Math::ConvexHull) >= 1.0.4
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(Math::PlanePath)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SVG)
BuildRequires:  perl(parent)
BuildRequires:  perl(Wx)
BuildRequires:  perl(Boost::Geometry::Utils)
BuildRequires:  perl(Math::Geometry::Voronoi)
BuildRequires:  perl(Growl::GNTP)
BuildRequires:  perl(Net::DBus)
Requires:       perl(XML::SAX)
Requires:       perl(Growl::GNTP)
Requires:       perl(Net::DBus)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

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

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc MANIFEST README.markdown
%{_bindir}/%{name}.pl
%{perl_vendorlib}/Slic3r*
%{_mandir}/man3/*

%changelog
* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 0.9.3-1
- New package
