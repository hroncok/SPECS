Name:           mono-cecil
Version:        0.9.5
%global commit 6d1b7d0bc02cea62aa7a950c049bd615a0ad4183
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20140924git%{shortcommit}
Release:        3.%{snapshot}%{?dist}
Summary:        Library to generate and inspect programs and libraries in the ECMA CIL form
License:        MIT
URL:            http://www.mono-project.com/Cecil
Source0:        https://github.com/jbevain/cecil/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch
BuildRequires:  mono(xbuild)
Requires:       mono-core

# TODO Remove once defined as standard macro
%global monodir /usr/lib/mono

%global configuration net_4_0_Release

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
%setup -qn cecil-%{commit}

%build
xbuild Mono.Cecil.sln /p:Configuration=%{configuration}

%install
mkdir -p %{buildroot}%{monodir}/gac/
cd bin/%{configuration}/
gacutil -i Mono.Cecil.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Mdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Pdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Rocks.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
cd -

%files
%doc NOTES.txt
%{monodir}/gac/Mono.Cecil*
%{monodir}/Mono.Cecil*

%changelog
* Sat Oct 25 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-3.20140924git6d1b7d0
- Updated

* Thu Feb 27 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-2.20131105git8425de4
- Define %%monodir
- Require mono-core for monodir/gac dependency
- Define %%configuration

* Mon Jan 27 2014 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-1
- New package
