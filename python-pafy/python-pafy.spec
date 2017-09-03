# Created by pyp2rpm-3.1.2
%global pypi_name pafy

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Retrieve YouTube content and metadata

License:        LGPLv3
URL:            http://np1.github.io/pafy/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
.. image:: https://img.shields.io/pypi/v/Pafy.svg     :target:
https://pypi.python.org/pypi/pafy .. image::
https://img.shields.io/pypi/dm/Pafy.svg     :target:
https://pypi.python.org/pypi/pafy .. image::
https://img.shields.io/coveralls/np1/pafy/develop.svg     :target:
https://coveralls.io/r/np1/pafy?branchdevelop .. ...

%package -n     python3-%{pypi_name}
Summary:        Retrieve YouTube content and metadata
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
.. image:: https://img.shields.io/pypi/v/Pafy.svg     :target:
https://pypi.python.org/pypi/pafy .. image::
https://img.shields.io/pypi/dm/Pafy.svg     :target:
https://pypi.python.org/pypi/pafy .. image::
https://img.shields.io/coveralls/np1/pafy/develop.svg     :target:
https://coveralls.io/r/np1/pafy?branchdevelop .. ...

%package -n     python2-%{pypi_name}
Summary:        Retrieve YouTube content and metadata
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
.. image:: https://img.shields.io/pypi/v/Pafy.svg     :target:
https://pypi.python.org/pypi/pafy .. image::
https://img.shields.io/pypi/dm/Pafy.svg     :target:
https://pypi.python.org/pypi/pafy .. image::
https://img.shields.io/coveralls/np1/pafy/develop.svg     :target:
https://coveralls.io/r/np1/pafy?branchdevelop .. ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install
cp %{buildroot}/%{_bindir}/ytdl %{buildroot}/%{_bindir}/ytdl-2
ln -sf %{_bindir}/ytdl-2 %{buildroot}/%{_bindir}/ytdl-%{python2_version}

%py3_install
cp %{buildroot}/%{_bindir}/ytdl %{buildroot}/%{_bindir}/ytdl-3
ln -sf %{_bindir}/ytdl-3 %{buildroot}/%{_bindir}/ytdl-%{python3_version}


%files -n python3-%{pypi_name} 
%doc README.rst
%{_bindir}/ytdl
%{_bindir}/ytdl-3
%{_bindir}/ytdl-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst
%{_bindir}/ytdl-2
%{_bindir}/ytdl-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jun 24 2016 copr-service - 0.5.1-1
- Initial package.