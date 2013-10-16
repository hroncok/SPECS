%global commit 6c9206902f9b01d60f4c373cc2db7b017fb49e72
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           ultimaker2-marlin-firmware
Version:        13.10
Release:        1%{?dist}
Summary:        Ultimaker2 firmware for the 3D printer
#this uses the arduino cross-compiler, so the output is arch-independent
BuildArch:      noarch
License:        GPLv3+
URL:            https://github.com/Ultimaker/SecretMarlin
Source0:        https://github.com/Ultimaker/SecretMarlin/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  ino
BuildRequires:  dos2unix

%description
%{summary}.

%global platform mega2560

%prep
%setup -qn SecretMarlin-%{commit}

# make the directory structure like ino likes it
mv Marlin src
mkdir lib
# In some files configuration.h is used instead of Configuration.h, etc
ln -s Configuration.h src/configuration.h
ln -s Marlin.h src/marlin.h

iconv -f iso8859-1 -t utf-8 src/COPYING > src/COPYING.conv && mv -f src/COPYING.conv src/COPYING
dos2unix README.md

%build
ino build -m %{platform}

%install
install -Dpm0644 .build/%{platform}/firmware.hex %{buildroot}%{_datadir}/%{name}/MarlinUltimaker2.hex

%files
%{_datadir}/%{name}
%doc src/COPYING README.md

%changelog
* Wed Oct 16 2013 Miro Hrončok <mhroncok@redhat.com> - 13.10-1
- New package (inspired a lot by ultimaker-marlin-firmware)
