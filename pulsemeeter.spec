Name:           pulsemeeter
Version:        2.0.0
Release:        1%{?dist}
Summary:        A pulseaudio audio routing application
License:        MIT
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pulsemeeter is an audio routing application for PulseAudio/PipeWire.

%prep
%autosetup -c

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{_bindir}/pulsemeeter
%{_bindir}/pmctl
%{python3_sitelib}/pulsemeeter/
%{python3_sitelib}/pulsemeeter-*.egg-info/
%{_datadir}/applications/pulsemeeter.desktop
%{_datadir}/icons/hicolor/*/apps/Pulsemeeter.png