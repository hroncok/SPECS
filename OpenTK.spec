Name:           OpenTK
Version:        0.0
%global         snapshot 20130108svn3126
Release:        4.%{snapshot}%{?dist}
Summary:        C# library that wraps OpenGL, OpenCL and OpenAL
# See License.txt for more information
License:        MIT and BSD
URL:            http://www.opentk.com/
# svn export https://opentk.svn.sourceforge.net/svnroot/opentk/trunk opentk
# tar czf %%{name}-%%{snapshot}.tar.gz opentk
Source0:        %{name}-%{snapshot}.tar.gz
BuildArch:      noarch
BuildRequires:  mono(xbuild)
BuildRequires:  mono(gacutil)

%description
The Open Toolkit is an advanced, low-level C# library that wraps OpenGL, OpenCL
and OpenAL. It is suitable for games, scientific applications and any other
project that requires 3d graphics, audio or compute functionality.

%prep
%setup -q -n opentk
cd Documentation
iconv -f iso8859-1 -t utf-8 License.txt > License.txt.conv && mv -f License.txt.conv License.txt
cd -

%build
export LANG=en_US.utf8 # Otherwise there are errors
xbuild %{name}.sln /p:Configuration=Release

%install
mkdir -p %{buildroot}/usr/lib/mono/gac/
gacutil -i Binaries/OpenTK/Release/%{name}.dll -f -package %{name} -root %{buildroot}/usr/lib
gacutil -i Binaries/OpenTK/Release/%{name}.Compatibility.dll -f -package %{name} -root %{buildroot}/usr/lib
gacutil -i Binaries/OpenTK/Release/%{name}.GLControl.dll -f -package %{name} -root %{buildroot}/usr/lib

%files
%doc Documentation/*[^.csproj]
/usr/lib/mono/gac/%{name}*
/usr/lib/mono/%{name}

%changelog
* Thu Jan 10 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-4.20130108svn3126
- New revision

* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-3.20120523svn3125
- Renamed from opentk to OpenTK

* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-2.20120523svn3125
- The package now owns /usr/lib/mono/OpenTK directory

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 0.0-1.20120523svn3125
- First try
