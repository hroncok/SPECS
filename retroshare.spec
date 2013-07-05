Name:           retroshare
%global numeric 0.5.4
Version:        %{numeric}e
Release:        1%{?dist}
License:        GPLv2+ and GPLv3+ and LGPLv2 and LGPLv2+ and LGPLv3
# see licenses
Summary:        Secure chat and file sharing
URL:            http://retroshare.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/RetroShare-v%{version}.tar.gz
Source1:        %{name}-licenses
Patch0:         %{name}-various.patch

BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libssh-devel >= 0.5
BuildRequires:  libupnp-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  qt4-devel
BuildRequires:  speex-devel

Requires:       qt-x11 >= 4.6
Requires:       openssl
Requires:       %{name}-nogui%{?_isa} = %{version}-%{release}

%description
RetroShare is a cross-platform private p2p sharing program.
It lets you share securely your friends, using a web-of-trust
to authenticate peers and OpenSSL to encrypt all communication.
RetroShare provides filesharing, chat, messages and channels.

%package nogui
Summary:       RetroShare without gui
License:       GPLv2+ and LGPLv2 and LGPLv2+ and GPLv3+ and GPLv3 and MIT
Requires:      openssl

%description nogui
RetroShare-nogui comes without a user interface. It can be controlled via
a special network protocol based on protobuf and ssh.
There are applications for Android and .Net available.


%package plugins
Summary:       Precompiled plugins for RetroShare
License:       GPLv2+ and LGPLv2 and BSD
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description plugins
Precompiled plugins for RetroShare.
So far contains LinksCloud, FeedReader and unfinished VOIP.

%prep
%setup -q -n %{name}-%{numeric}/src
%patch0 -p0

cp %{SOURCE1} .

rm -rf supportlibs # openpgpsdk
sed -i 's/\r//g' %{name}-gui/src/README.txt
find -name '*.h' -exec chmod -x {} \;
find -name '*.cpp' -exec chmod -x {} \;


%build
for DIR in libbitdht/src openpgpsdk/src libretroshare/src retroshare-gui/src retroshare-nogui/src plugins; do
  cd $DIR
  qmake-qt4 CONFIG=release
  make %{?_smp_mflags}
  cd -
done

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %{buildroot}%{_datadir}/RetroShare
mkdir -p %{buildroot}%{_libdir}/retroshare/extensions
#bin
install -m 755 retroshare-gui/src/RetroShare %{buildroot}%{_bindir}/
install -m 755 retroshare-nogui/src/retroshare-nogui %{buildroot}%{_bindir}/


#qss
cp -R retroshare-gui/src/qss %{buildroot}%{_datadir}/RetroShare/

#icons  
install -m 644 data/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/
install -m 644 data/24x24/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -m 644 data/48x48/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 data/64x64/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m 644 data/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

install -m 644 libbitdht/src/bitdht/bdboot.txt %{buildroot}%{_datadir}/RetroShare/

#plugins
install -m 755 plugins/LinksCloud/libLinksCloud.so %{buildroot}%{_libdir}/retroshare/extensions/
install -m 755 plugins/VOIP/libVOIP.so %{buildroot}%{_libdir}/retroshare/extensions/
install -m 755 plugins/FeedReader/libFeedReader.so %{buildroot}%{_libdir}/retroshare/extensions/

#menu
desktop-file-install data/%{name}.desktop

%files
%doc %{name}-gui/src/README.txt %{name}-licenses
%attr(755,root,root) %{_bindir}/RetroShare
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor
%{_datadir}/applications/%{name}.desktop

%files nogui
%doc %{name}-gui/src/README.txt %{name}-licenses
%attr(755,root,root) %{_bindir}/retroshare-nogui
%{_datadir}/RetroShare

%files plugins
%doc %{name}-gui/src/README.txt %{name}-licenses
%{_libdir}/retroshare

%changelog
* Thu Jul 04 2013 Miro Hrončok <mhroncok@redhat.com> - 0.5.4e-1
- Got file from openSUSE build service and revised

