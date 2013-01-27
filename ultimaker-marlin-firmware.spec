%global commit ec97307ce17c34c05c958034aafb0b135135cd27
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           ultimaker-marlin-firmware
Version:        12.12
Release:        0.2.RC1%{?dist}
Summary:        Ultimaker firmware for the 3D printer
#this uses the arduino cross-compiler, so the output is arch-independent
BuildArch:      noarch
License:        GPLv3+
URL:            https://github.com/Ultimaker/Marlin
Source0:        https://github.com/Ultimaker/Marlin/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  ino

%description
%{summary}.

%prep
%setup -qn Marlin-%{commit}

# make the directory structure like ino likes it
mv Marlin src
mkdir lib

%build
ino build -m mega

%install
install -Dpm0644 .build/mega/firmware.hex \
                %{buildroot}%{_datadir}/%{name}/%{name}.hex

%files
%{_datadir}/%{name}
%doc src/COPYING README.md

%changelog
* Sun Jan 27 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-0.2.RC1
- Updated source to follow GitHub rule

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 12.12-0.1.RC1
- rough initial package
