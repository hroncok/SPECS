Name:           skeinforge
Version:        12.03.14
Release:        5%{?dist}
Summary:        Converts 3D model into G-Code for RepRap
License:        AGPLv3 # Ask author for LICENCE file - will be in next release
Group:          Applications/Engineering # Optional
URL:            http://fabmetheus.crsndoo.com/wiki/index.php/Skeinforge
Source0:        http://fabmetheus.crsndoo.com/files/50_reprap_python_beanshell.zip

BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       python2
Requires:       tkinter

%description
Skeinforge is a tool chain composed of Python scripts that converts your
3D model into G-Code instructions for RepRap.

%package        doc
Requires:       %{name} = %{version}-%{release}
Summary:        Documentation for %{name}

%description    doc
Skeinforge is a tool chain composed of Python scripts that converts your
3D model into G-Code instructions for RepRap.
This is the documentation.


%prep
%setup -cq


%build


%install
%{__rm} -rf models terminal.sh test.stl %{name}_application/terminal.sh %{name}_application/test.stl # removes stupid useless files
mkdir -p %{buildroot}%{_datadir}/printrun/%{name}
cp -ar * %{buildroot}%{_datadir}/printrun/%{name}


%files
%dir %{_datadir}/printrun/
%{_datadir}/printrun/%{name}/
%exclude %{_datadir}/printrun/%{name}/documentation/

%files      doc
%{_datadir}/printrun/%{name}/documentation/

%changelog
* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-5
- Noarch

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-4
- Owns %{_datadir}/printrun/

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-3
- Splited documentation

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-2
- Added tkinter and python2 to requires

* Fri Sep 21 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-1
- New package
