# Created by pyp2rpm-1.1.2
%global pypi_name mps-youtube

Name:           %{pypi_name}
Version:        0.2.8
Release:        2%{?dist}
Summary:        Terminal based YouTube player and downloader

License:        GPLv3
URL:            http://github.com/np1/mps-youtube

Source0:        https://github.com/mps-youtube/mps-youtube/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/wzzrd/mps-youtube/master/mps-youtube/mpv032.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel
 
Requires:       mpv python3-pafy >= 0.5.4

%description
This project is based on mps, a terminal based program to search, stream and download music.
This implementation uses YouTube as a source of content and can play and download video as well as audio.
The pafy library handles interfacing with YouTube.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%patch

%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}
rm -f $RPM_BUILD_ROOT/usr/{README.rst,CHANGELOG,LICENSE}


%files
%doc README.rst
%doc CHANGELOG
%license LICENSE
%{_bindir}/mpsyt
%{_datadir}/applications/mps-youtube.desktop
%{python3_sitelib}/mps_youtube-%{version}-py?.?.egg-info
%{python3_sitelib}/mps_youtube/

%changelog
* Mon May 4 2020 Maxim Burgerhout <maxim@wzzrd.com> - 0.28-1
- Apply patch from unstable branc to fix mpv-0.32 issue (PR #1053)

* Sat Feb 24 2018  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.8-1
- update to version 0.2.8
- Removed youtube-dl dependency, python3-pafy requires youtube-dl

* Thu Jan 25 2018  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.7.1-2
- Fixed missing youtube-dl dependency

* Fri Feb 17 2017  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.7.1-1
- update to version 0.2.7.1

* Fri Jun 24 2016  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.6-1
- update to version 0.2.6

* Fri Nov 27 2015  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.5-3
- Added mpv to dependencies due to lack of support for streaming in mplayer

* Fri Oct 23 2015  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.5-2
- Rebuild for python3 due to lack of support for python2

* Fri Oct 23 2015  Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2.5-1
- Initial package.

