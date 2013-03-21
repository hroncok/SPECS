%global with_python3 1
# comment this out in koji
#%%global locally 1
%global pypi_name MultipartPostHandler2
Name:           python-%{pypi_name}
Version:        0.1.1
Release:        3%{?dist}
Summary:        A handler for urllib2 to enable multipart form uploading
# License note in MultipartPostHandler.py
License:        LGPLv2+
URL:            http://pypi.python.org/pypi/%{pypi_name}/%{version}
Source0:        http://pypi.python.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Remove the example in main() from the library and keep it separated
Patch0:         %{name}-cut-out-main.patch

# Several Python3 specific things, needs to be applied after 2to3!
Patch1:         %{name}-python3.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python-tools
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
%patch0 -p1
rm -rf doc # no real doc there

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
cd %{py3dir}
find . -name '*.py' | xargs sed -i '1s|^#!%{__python}|#!%{__python3}|'
2to3 --write --nobackup *.py
%patch1 -p1
cd -
# copy the example back so it can be used in %%doc
cp %{py3dir}/MultipartPostHandler-example.py python3-MultipartPostHandler-example.py
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
cd -
%endif # with_python3

%{__python} setup.py install --skip-build --root %{buildroot}

%if 0%{?locally}
%check
%{__python} MultipartPostHandler-example.py
%if 0%{?with_python3}
cd %{py3dir}
%{__python3} MultipartPostHandler-example.py
cd -
%endif # with_python3
%endif # locally

%files
%doc README.txt MultipartPostHandler-example.py
%{python_sitelib}/*
%files -n python3-%{pypi_name}
%doc README.txt python3-MultipartPostHandler-example.py
%{python3_sitelib}/*

%changelog
* Thu Mar 21 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Remove the example in main() from the library and keep it separated
- Added patch witch Python 3 specific things

* Wed Feb 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Introduced Python 3 subpackage

* Fri Jan 25 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Created by pyp2rpm-0.5.1
- Revised
