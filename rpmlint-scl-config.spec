Name:           rpmlint-scl-config
Version:        0
Release:        1%{?dist}
Summary:        Software Collections related configuration for rpmlint
License:        Public Domain
Source0:        scl.config
BuildArch:      noarch
Requires:       rpmlint => 1.6

%description
Configuration that enables Software Collections checks for rpmlint.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}%{_sysconfdir}/rpmlint
install -pm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/rpmlint/scl.config

%files
%config(noreplace) %{_sysconfdir}/rpmlint/scl.config

%changelog
* Thu Aug 14 2014 Miro Hrončok <mhroncok@redhat.com> - 0-1
- Initial package

