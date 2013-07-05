Name:           retroshare
%global numeric 0.5.4
Version:        %{numeric}e
Release:        1%{?dist}
License:        GPLv2+ and GPLv3+ and LGPLv2 and LGPLv2+ and LGPLv3
# see %%{name}-licenses
# the license mess was already reported upstream
Summary:        Secure chat and file sharing
URL:            http://retroshare.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/RetroShare-v%{version}.tar.gz
Source1:        %{name}-licenses

# original patch from upstream openSUSE Build Service repo
Patch0:         %{name}-various.patch

# use system libs
Patch1:         %{name}-unbundle.patch

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


%package -n bitdht
Summary:       Distributed Hash Table library
License:       LGPLv3

%description -n bitdht
BitDHT is a LGPL'd general purpose C++ Distributed Hash Table library.
It is designed to take hassle out over creating your own DHT.
BitDHT is compatible with bitttorrent's DHT and can leverage this network
to bootstrap your own personal DHT.


%package -n bitdht-devel
Summary:       BitDHT development files
License:       LGPLv3
Requires:      bitdht%{?_isa} = %{version}-%{release}

%description -n bitdht-devel
Development files for BitDHT.


%package -n openpgpsdk
Summary:       OpenPGP library
License:       ASL 2.0

%description -n openpgpsdk
The OpenPGP SDK project provides an open source library, written in C,
which implements the OpenPGP specification.

%package -n openpgpsdk-devel
Summary:       OpenPGP SDK development files
License:       ASL 2.0
Requires:      openpgpsdk%{?_isa} = %{version}-%{release}

%description -n openpgpsdk-devel
Development files for OpenPGP SDK.

%prep
%setup -q -n %{name}-%{numeric}/src
%patch0 -p0
%patch1 -p1

cp %{SOURCE1} .

rm -rf supportlibs rsctrl
sed -i 's/\r//g' %{name}-gui/src/README.txt
find -name '*.h' -exec chmod -x {} \;
find -name '*.cpp' -exec chmod -x {} \;


%build
for DIR in libbitdht/src openpgpsdk/src libretroshare/src retroshare-gui/src retroshare-nogui/src plugins; do
  cd $DIR
  %{_qt4_qmake} CONFIG=release
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
mkdir -p %{buildroot}%{_datadir}/bitdht
mkdir -p %{buildroot}%{_libdir}/retroshare/extensions
mkdir -p %{buildroot}%{_includedir}/bitdht/{bitdht,udp,util}
mkdir -p %{buildroot}%{_includedir}/openpgpsdk

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

#plugins
install -m 755 plugins/LinksCloud/libLinksCloud.so %{buildroot}%{_libdir}/retroshare/extensions/
install -m 755 plugins/VOIP/libVOIP.so %{buildroot}%{_libdir}/retroshare/extensions/
install -m 755 plugins/FeedReader/libFeedReader.so %{buildroot}%{_libdir}/retroshare/extensions/

#menu
desktop-file-install data/%{name}.desktop

# libbitdht
cp -pP libbitdht/src/lib/* %{buildroot}%{_libdir}/
cp -pP libbitdht/src/bitdht/*.h %{buildroot}%{_includedir}/bitdht/bitdht
cp -pP libbitdht/src/bitdht/bdboot.txt %{buildroot}%{_datadir}/bitdht
cp -pP libbitdht/src/udp/*.h %{buildroot}%{_includedir}/bitdht/udp
cp -pP libbitdht/src/util/*.h %{buildroot}%{_includedir}/bitdht/util
ln -s %{_datadir}/bitdht/bdboot.txt %{buildroot}%{_datadir}/RetroShare/

# openpgpsdk
cp -pP openpgpsdk/src/lib/* %{buildroot}%{_libdir}/
cp -pP openpgpsdk/src/openpgpsdk/*.h %{buildroot}%{_includedir}/openpgpsdk/

%files
%doc %{name}-gui/src/README.txt %{name}-gui/src/chnagelog.txt %{name}-licenses
%attr(755,root,root) %{_bindir}/RetroShare
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor
%{_datadir}/applications/%{name}.desktop

%files nogui
%doc %{name}-gui/src/README.txt %{name}-gui/src/chnagelog.txt %{name}-licenses
%attr(755,root,root) %{_bindir}/retroshare-nogui
%{_datadir}/RetroShare

%files plugins
%doc %{name}-gui/src/README.txt %{name}-gui/src/chnagelog.txt %{name}-licenses
%{_libdir}/retroshare

%files -n bitdht
%doc libbitdht/src/README.txt
%{_libdir}/libbitdht.so.*
%{_datadir}/bitdht

%files -n bitdht-devel
%doc libbitdht/src/README.txt libbitdht/src/example
%{_includedir}/bitdht/
%{_libdir}/libbitdht.so

%files -n openpgpsdk
%{_libdir}/libops.so.*

%files -n openpgpsdk-devel
%{_includedir}/openpgpsdk/
%{_libdir}/libops.so

%changelog
* Thu Jul 04 2013 Miro Hrončok <mhroncok@redhat.com> - 0.5.4e-1
- Got file from openSUSE build service and revised
- Create separete bitdht and openpgpsdk packages

