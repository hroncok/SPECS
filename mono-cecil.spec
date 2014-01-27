Name:           mono-cecil
Version:        0.9.5
Release:        1%{?dist}
Summary:        Library to generate and inspect programs and libraries in the ECMA CIL form
License:        MIT
URL:            http://www.mono-project.com/Cecil
Source0:        https://github.com/jbevain/cecil/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  mono(xbuild)

%description
Cecil is a library written by Jb Evain to generate and inspect programs and
libraries in the ECMA CIL format. It has full support for generics, and support
some debugging symbol format.

In simple English, with Cecil, you can load existing managed assemblies, browse
all the contained types, modify them on the fly and save back to the disk the
modified assembly.

Today it is used by the Mono Debugger, the bug-finding and compliance checking
tool Gendarme, MoMA, DB4O, as well as many other tools.

%prep
%setup -q -n cecil-%{version}

%build
xbuild Mono.Cecil.sln /p:Configuration=net_4_0_Release

%install
mkdir -p %{buildroot}/usr/lib/mono/gac/
cd bin/net_4_0_Release/
gacutil -i Mono.Cecil.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Mdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Pdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Rocks.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
cd -

%files
%doc NOTES.txt
/usr/lib/mono/gac/Mono.Cecil*
/usr/lib/mono/Mono.Cecil*

%changelog
* Mon Jan 27 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-1
- New package
