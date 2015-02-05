Name:           cura-lulzbot
Version:        14.12
Release:        1%{?dist}
Summary:        Cura LulzBot Edition, 3D printer control software

# Code is AGPLv3
# Example models are CC-BY-SA
License:        AGPLv3 and CC-BY-SA

URL:            https://www.lulzbot.com/cura

Source0:        https://github.com/alephobjects/Cura/archive/lulzbot-%{version}.tar.gz
Source1:        %{name}
Source2:        %{name}.desktop

# Use system paths and make it parallel installable with cura
Patch1:         %{name}-system-paths.patch

# Rework the logic of determining the version (didn't work)
Patch2:         %{name}-version.patch

# Disable installation of firmwares Fedora doesn't ship
Patch3:         %{name}-no-firmware.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       PyOpenGL
Requires:       wxPython
Requires:       pyserial
Requires:       numpy
Requires:       python-power
Requires:       pypy
Requires:       CuraEngine >= 14.12.1

%description
The default software for the LulzBot Mini 3D printer is called Cura LulzBot
Edition. Cura is a Free Software program that both prepares your files for
printing (by converting your model into GCODE), and also allows you to control
the operation of your LulzBot 3D printer.


%prep
%setup -qn Cura-lulzbot-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

dos2unix resources/example/Attribution.txt

sed -i 's/REPLACE_THIS_IN_SPEC/%{version}/' Cura/util/version.py

# remove shebang
sed -i '1d' Cura/cura.py
sed -i '1d' Cura/util/pymclevel/mce.py

# Remove firmware
rm resources/firmware/*

# Rename icon
mv resources/cura{,-lulzbot}.ico

# Relocate imports - don't write patch for this, as this sed needs no rebasing ;)
find -name \*.py -exec sed -i \
  -e 's/from Cura import/from CuraLulzbot import/g' \
  -e 's/from Cura\./from CuraLulzbot./g' \
  -e 's/import Cura/import CuraLulzbot/g' {} \;

%build
# rebuild locales
cd resources/locale
mv po pl # polish code was wrong
rm *.in *.pot
for FILE in *; do
  rm $FILE/LC_MESSAGES/Cura.mo
  msgfmt $FILE/LC_MESSAGES/Cura.po -o $FILE/LC_MESSAGES/CuraLulzbot.mo
  rm $FILE/LC_MESSAGES/Cura.po
done
cd -

%install
mkdir -p %{buildroot}%{python_sitelib}/CuraLulzbot
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_bindir}

cp -apr Cura/* %{buildroot}%{python_sitelib}/CuraLulzbot
rm -rf %{buildroot}%{python_sitelib}/CuraLulzbot/LICENSE
cp -apr resources/* %{buildroot}%{_datadir}/%{name}
cp -apr plugins %{buildroot}%{_datadir}/%{name}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name} %{buildroot}%{python_sitelib}/CuraLulzbot/resources
ln -s %{_datadir}/%{name}/%{name}.ico %{buildroot}%{_datadir}/pixmaps

# locales
cp -ar %{buildroot}%{_datadir}/%{name}/locale/* %{buildroot}%{_datadir}/locale
rm -rf %{buildroot}%{_datadir}/%{name}/locale
ln -s -f %{_datadir}/locale/ %{buildroot}%{_datadir}/%{name}/ # the app expects the locale folder in here

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%{find_lang} CuraLulzbot

%files -f CuraLulzbot.lang
%license Cura/LICENSE resources/example/Attribution.txt
%doc changelog
%{python_sitelib}/CuraLulzbot
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.ico
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%changelog
* Wed Feb 04 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12-1
- Initial package (started as cura.spec fork)

