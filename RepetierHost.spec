Name:           RepetierHost
Version:        0.82b
Release:        1%{?dist}
Summary:        3D printer control software
License:        ASL 2.0
URL:            http://www.repetier.com/
# git hash 54ff8a364f
# git clone git://github.com/repetier/Repetier-Host.git; cd Repetier-Host
# git archive master --format tar.gz > ../%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildArch:      noarch
BuildRequires:  mono(xbuild)
BuildRequires:  mono(OpenTK)
BuildRequires:  dos2unix

%description
Software for controlling RepRap style 3D-printer like Mendel, Darwin or Prusa
Mendel. Works with most firmware types. It is optimized to work with
Repetier-Firmware Other working firmware is Sprinter, Teacup, Marlin and all
compatible firmwares.

%prep
%setup -cq
# Drop Slic3r and OpenTK licenses
head -16 Repetier-Host-licence.txt > Repetier-Host-licence.txt.short \
&& mv -f Repetier-Host-licence.txt.short Repetier-Host-licence.txt
dos2unix Repetier-Host-licence.txt README* changelog.txt

%build
cd src/%{name}
sed -i 's/ColorSlider.designer.cs/ColorSlider.Designer.cs/' %{name}.csproj
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
* Mon Dec 31 2012 Miro Hrončok <miro@hroncok.cz> - 0.82b-1
- First try
