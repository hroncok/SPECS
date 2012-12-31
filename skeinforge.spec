Name:           skeinforge
Version:        12.03.14
Release:        10%{?dist}
Summary:        Converts 3D model into G-Code for RepRap
License:        AGPLv3
Group:          Applications/Engineering
URL:            http://fabmetheus.crsndoo.com/wiki/index.php/Skeinforge
Source0:        http://fabmetheus.crsndoo.com/files/50_reprap_python_beanshell.zip
# Asked author for LICENSE file - will be in next release
Source1:        http://www.gnu.org/licenses/agpl.txt

# Desktop file
Source2:        skeinforge.desktop
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
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
cp -a %{SOURCE1} license.txt

%build

%install
rm -rf models terminal.sh test.stl %{name}_application/terminal.sh %{name}_application/test.stl # removes stupid useless files
mkdir -p %{buildroot}%{python_sitelib}/%{name}
cp -ar * %{buildroot}%{python_sitelib}/%{name}
rm -f %{python_sitelib}/%{name}/license.txt
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2} # desktop file

%files
%doc license.txt
%{python_sitelib}/%{name}
%{_datadir}/applications/skeinforge.desktop
%exclude %{python_sitelib}/%{name}/documentation/

%files      doc
%{python_sitelib}/%{name}/documentation/

%changelog
* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-10
- Changed location of skeinforge from %{_datadir}/%{name}/
                                   to %{python_sitelib}/%{name}

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-9
- Do not download the desktop file from my GitHub.

* Mon Oct 29 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-8
- Added desktop file
- Don't use macros for rm and cp
- Removed license file from doc package

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-7
- Do not install directly to printrun dir

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> - 12.03.14-6
- Include license file

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
