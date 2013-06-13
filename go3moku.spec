Name:           go3moku
%global commit 12058be8926fde28c77f9063d7d9496303bcdb76
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20130430git%{shortcommit}
Version:        0.0
Release:        1.%{snapshot}%{?dist}
Summary:        Three-dimensional gomoku game

License:        ISC
URL:            https://github.com/hroncok/Go3moku
Source0:        https://github.com/hroncok/Go3moku/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils

BuildRequires:  java-devel
BuildRequires:  ant

Requires:       jpackage-utils
Requires:       java

%description
Go3moku is a 3D tic-tac-toe game. It offers human to human, as well human to
computer or computer to computer gameplay. It has not many features, but works.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qn Go3moku-%{commit}

%build
ant

%install

mkdir -p %{buildroot}%{_javadir}
cp -p dist/Go3moku.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp dist/javadoc %{buildroot}%{_javadocdir}/%{name}

%files
%doc README.md COPYING
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Apr 30 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20130430git12058be
- New package

