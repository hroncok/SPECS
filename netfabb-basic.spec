Name:           netfabb-basic
Version:        4.9.5
Release:        1%{?dist}
Summary:        Freeware suite for STL editing
License:        Redistributable
URL:            http://www.netfabb.com/
%ifarch x86_64
Source0:        http://www.netfabb.com/download/netfabb_linux64.tar.gz
%endif
%ifarch i686
Source0:        http://www.netfabb.com/download/netfabb_linux.tar.gz
%endif
BuildRequires:  desktop-file-utils

%global debug_package %{nil}

%description
This is a Linux release of netfabb Studio Basic, a freeware suite for STL 
editing. We hope you will find this software useful and enjoy its 
functionality.

Please contribute to a further development by sending any questions, feedback
and bug reports to info@netfabb.com. Due to the diversity of environments, it
is impossible for us to test the Linux version on more than a few selected 
platforms.

So even if you don't experience any deeper problems, it would be very valuable 
for us to get to know your distribution and system configuration. The binary 
has been built on Debian Squeeze.

%prep
%setup -qn %{name}

# Don't copy doc, let RPM do it
# Don't install uninstall script
grep -v '/usr/share/doc' install.sh | grep -v uninstall.sh > install-fedora.sh

# Let's pretend, we are root
sed -i 's/id -u/echo 0/' install-fedora.sh

# Install to $ROOT/usr and not to /usr
sed -i 's|/usr|$ROOT/usr|g' install-fedora.sh

# But keep /usr in files
sed -i 's|Exec=$ROOT/usr|Exec=/usr|g' install-fedora.sh
sed -i 's|LD_LIBRARY_PATH=$ROOT/usr|LD_LIBRARY_PATH=/usr|g' install-fedora.sh
sed -i 's|echo exec $ROOT/usr|echo exec /usr|g' install-fedora.sh

%ifarch x86_64
# Use lib64 as it is a 64bit build
sed -i 's|/lib/|/lib64/|g' install-fedora.sh
%endif

chmod +x install-fedora.sh

%build
# nothing to do

%install
env ROOT=%{buildroot} ./install-fedora.sh

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README LICENSE changelog.gz
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*


%changelog
* Tue Mar 26 2013 Miro Hrončok <mhroncok@redhat.com> - 4.9.5-1
- Initial release.
