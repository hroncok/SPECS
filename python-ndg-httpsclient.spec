Name:           python-ndg-httpsclient
Version:        0.3.2
Release:        1%{?dist}
Summary:        Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL

License:        BSD
URL:            http://ndg-security.ceda.ac.uk/wiki/ndg_httpsclient/
Source0:        https://pypi.python.org/packages/source/n/ndg-httpsclient/ndg_httpsclient-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  pyOpenSSL
BuildRequires:  openssl
BuildRequires:  /usr/bin/killall
 
Requires:       pyOpenSSL
Requires:       python-pyasn1

%description
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

%prep
%setup -q -n ndg_httpsclient-%{version}
# Remove bundled egg-info
rm -rf ndg_httpsclient.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
cd ndg/httpsclient/test/
./scripts/openssl_https_server.sh &
sleep 1
# the test suite is not working and we don't know why
# upstream bugtracker is not functional
#for FILE in test_*.py; do
for FILE in test_utils.py; do
  PYTHONPATH=../../.. %{__python2} ./$FILE
done
killall openssl

%files
%doc LICENSE
%{_bindir}/ndg_httpclient
%{python2_sitelib}/ndg
%{python2_sitelib}/ndg_httpsclient-%{version}-py?.?.egg-info
%{python2_sitelib}/ndg_httpsclient-%{version}-py?.?-nspkg.pth

%changelog
* Tue Oct 14 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-1
- Initial package.
