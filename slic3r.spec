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
BuildRequires:  perl(Module::Build)
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

%{_mandir}/man1/*

%changelog
* Thu Oct 04 2012 Miro Hrončok <miro@hroncok.cz> 0.9.3-1
- New package
