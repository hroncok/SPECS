Name:           opentk
Version:        0.0
%global         snapshot 20120523svn3125
Release:        2.%{snapshot}%{?dist}
Summary:        C# library that wraps OpenGL, OpenCL and OpenAL
# See License.txt for more information
License:        MIT and BSD
URL:            http://www.opentk.com/
# svn export https://%%{name}.svn.sourceforge.net/svnroot/%%{name}/trunk %%{name}
# tar czf %%{name}-%%{snapshot}.tar.gz %%{name}
Source0:        %{name}-%{snapshot}.tar.gz
BuildArch:      noarch
BuildRequires:  mono(xbuild)
BuildRequires:  mono(gacutil)

%description
The Open Toolkit is an advanced, low-level C# library that wraps OpenGL, OpenCL
and OpenAL. It is suitable for games, scientific applications and any other
project that requires 3d graphics, audio or compute functionality.

%prep
%setup -q -n %{name}
cd Documentation
iconv -f iso8859-1 -t utf-8 License.txt > License.txt.conv && mv -f License.txt.conv License.txt
cd -

%build
export LANG=en_US.utf8 # Otherwise there are errors
xbuild OpenTK.sln /p:Configuration=Release

%install
mkdir -p %{buildroot}/usr/lib/mono/gac/
gacutil -i Binaries/OpenTK/Release/OpenTK.dll -f -package %{name} -root %{buildroot}/usr/lib
gacutil -i Binaries/OpenTK/Release/OpenTK.GLControl.dll -f -package %{name} -root %{buildroot}/usr/lib

%files
%doc Documentation/*[^.csproj]
/usr/lib/mono/gac/OpenTK*
/usr/lib/mono/opentk

%changelog
* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-2.20120523svn3125
- The package now owns /usr/lib/mono/opentk directory

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-1.20120523svn3125
- First try
