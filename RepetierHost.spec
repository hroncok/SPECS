Name:           RepetierHost
Version:        0.82b
Release:        4%{?dist}
Summary:        3D printer control software
License:        ASL 2.0
URL:            http://www.repetier.com/
%global commit dff824fad56a992c845b4d9fae815c4527ab6285
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/repetier/Repetier-Host/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.desktop
BuildArch:      noarch
BuildRequires:  mono(xbuild)
BuildRequires:  mono(OpenTK)
BuildRequires:  font(freesans)
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
Requires:       font(freesans)

%description
Software for controlling RepRap style 3D-printer like Mendel, Darwin or Prusa
Mendel. Works with most firmware types. It is optimized to work with
Repetier-Firmware Other working firmware is Sprinter, Teacup, Marlin and all
compatible firmwares.

%prep
%setup -qn Repetier-Host-%{commit}
# Drop Slic3r and OpenTK licenses
head -16 Repetier-Host-licence.txt > Repetier-Host-licence.txt.short \
&& mv -f Repetier-Host-licence.txt.short Repetier-Host-licence.txt
dos2unix Repetier-Host-licence.txt README* changelog.txt

cd src/%{name}

# Linux is case sensitive
sed -i 's/ColorSlider.designer.cs/ColorSlider.Designer.cs/' %{name}.csproj

# Overwrite Arial with something more free
sed -i 's/Arial/FreeSans/g' view/utils/ArrowButton.cs view/RepetierEditor.Designer.cs view/PrintPanel.Designer.cs

cd -

%build
cd src/%{name}
xbuild %{name}.sln /p:Configuration=Release
cd -

%install
mkdir -p %{buildroot}/usr/lib/mono/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

cp src/%{name}/bin/Release/%{name}* %{buildroot}/usr/lib/mono/%{name}
cp -r src/data/* %{buildroot}%{_datadir}/%{name}
ln -s %{_datadir}/%{name} %{buildroot}/usr/lib/mono/%{name}/data
cp src/%{name}/repetier-logo-trans32.ico %{buildroot}%{_datadir}/pixmaps/%{name}.ico

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

echo '#!/usr/bin/env bash' > %{buildroot}%{_bindir}/%{name}
echo 'mono /usr/lib/mono/%{name}/%{name}.exe' >> %{buildroot}%{_bindir}/%{name}
echo 'exit $?' >> %{buildroot}%{_bindir}/%{name}
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%doc APACHE-LICENSE-2.0.txt Repetier-Host-licence.txt README* changelog.txt
/usr/lib/mono/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.ico

%changelog
* Mon Jan 14 2013 Miro Hrončok <mhroncok@redhat.com> - 0.82b-4
- Moved some of the code modifications to %%prep

* Wed Jan 09 2013 Miro Hrončok <mhroncok@redhat.com> - 0.82b-3
- Updated to respect new GitHub rule

* Sun Jan 06 2013 Miro Hrončok <miro@hroncok.cz> - 0.82b-2
- Overwrite Arial with something more free

* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.82b-1
- First try
