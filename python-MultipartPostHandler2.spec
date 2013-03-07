%global with_python3 1
%global pypi_name MultipartPostHandler2
Name:           python-%{pypi_name}
Version:        0.1.1
Release:        2%{?dist}
Summary:        A handler for urllib2 to enable multipart form uploading
# License note in MultipartPostHandler.py
License:        LGPLv2+
URL:            http://pypi.python.org/pypi/%{pypi_name}/0.1.1
Source0:        http://pypi.python.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        A handler for urllib2 to enable multipart form uploading

%description -n python3-%{pypi_name}
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.
%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf doc # no real doc there

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

%build
%{__python} setup.py build

%if 0%{?with_python3}
cd %{py3dir}
%{__python3} setup.py build
cd -
%endif # with_python3

%install
%if 0%{?with_python3}
cd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
chmod +x %{buildroot}%{python3_sitelib}/MultipartPostHandler.py
cd -
%endif # with_python3

chmod +x %{buildroot}%{python_sitelib}/MultipartPostHandler.py
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.txt
%{python_sitelib}/MultipartPostHandler*
%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/MultipartPostHandler*

%changelog
* Wed Feb 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Introduced Python 3 subpackage

* Fri Jan 25 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Created by pyp2rpm-0.5.1
- Revised
