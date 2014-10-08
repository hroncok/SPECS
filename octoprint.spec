Name:           octoprint
Version:        1.1.0
%global         rcver rc2
Release:        0.1.%{rcver}%{?dist}
Summary:        The responsive web interface for your 3D printer
License:        AGPLv3

URL:            http://octoprint.org/
Source0:        https://github.com/foosel/OctoPrint/archive/%{version}-%{rcver}.tar.gz

# currently in https://github.com/hroncok/RPMAdditionalSources
Source1:        %{name}.service
Source2:        %{name}-README.shutdown

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  systemd

Requires:       PyYAML
Requires:       numpy
Requires:       pyserial
Requires:       python-flask
Requires:       python-flask-login
Requires:       python-flask-principal
Requires:       python-netaddr
Requires:       python-sockjs-tornado
Requires:       python-tornado
Requires:       python-werkzeug

Requires(postun): procps-ng

%description
OctoPrint is a so called host software for 3D printers that controls your
3D printer and sends it the actual commands to do its job. Other tools for
this task include Printrun, RepetierHost and also Cura.

OctoPrint differs from existing host solutions in that its major focus is
to provide a web interface that allows controlling the printer remotely from
anywhere on the network or even the internet while offering the same
responsiveness and feedback options available on native host applications like
the ones listed above. In order to achieve this, OctoPrint makes heavy use of
current web technologies and frameworks, such as AJAX and HTML5 web sockets.

OctoPrint was developed to be run on small embedded devices such as the popular
Raspberry Pi. It allows you to turn your existing 3D printer into a WiFi
enabled one and untether it from your laptop or work station.

%prep
%setup -q -n OctoPrint-%{version}-%{rcver}
cp %{SOURCE2} README.shutdown

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

install -Dpm0755 run %{buildroot}%{_bindir}/%{name}-run
install -Dp %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service


# octoprint-shutdown
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d/
touch %{buildroot}%{_sysconfdir}/sudoers.d/%{name}-shutdown

# configuration
mkdir -p %{buildroot}%{_localstatedir}/%{name}
ln -s %{_localstatedir}/%{name}/.%{name}/config.yaml %{buildroot}%{_sysconfdir}/%{name}.yaml

# the pid file
mkdir -p %{buildroot}%{_tmpfilesdir}
echo 'd /run/%{name} 0700 %{name} %{name} -' > %{buildroot}%{_tmpfilesdir}/%{name}.conf

%post
/usr/sbin/adduser -b %{_localstatedir} -K MAIL_DIR=/dev/null %{name} &> /dev/null || :
/usr/sbin/usermod -a -G dialout octoprint &> /dev/null || :
/usr/bin/su %{name} -c 'mkdir -p %{_localstatedir}/%{name}/.%{name}/' &> /dev/null || :
/usr/bin/su %{name} -c 'touch %{_localstatedir}/%{name}/.%{name}/config.yaml' &> /dev/null || :
/usr/bin/systemctl daemon-reload || :

%postun
/usr/bin/systemctl stop %{name}.service &> /dev/null || :
/usr/bin/pkill -u %{name} &> /dev/null || :
/usr/bin/rm %{_localstatedir}/%{name}/%{name}.pid &> /dev/null || :
/usr/bin/systemctl daemon-reload || :

%files
%doc README.md LICENSE README.shutdown
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{python2_sitelib}/%{name}
%{python2_sitelib}/*.egg-info
%ghost %config(noreplace) %{_sysconfdir}/sudoers.d/%{name}-shutdown
%ghost %config(noreplace) %{_localstatedir}/%{name}
%{_sysconfdir}/%{name}.yaml
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf

%changelog
* Wed Oct 08 2014 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-0.1.rc2
- New version

* Fri Mar 28 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.2.rc1
- Use %%{_tmpfilesdir} for pidfile

* Sat Jan 04 2014 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.1.rc1
- Initial spec.
