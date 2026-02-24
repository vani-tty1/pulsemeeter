Name:           pulsemeeter
Version:        2.0.0
Release:        1%{?dist}
Summary:        A pulseaudio audio routing application
License:        MIT
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Pulsemeeter is an audio routing application for PulseAudio/PipeWire.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pulsemeeter

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pulsemeeter
%{_bindir}/pmctl
%{_datadir}/applications/pulsemeeter.desktop
%{_datadir}/icons/hicolor/*/apps/Pulsemeeter.png

%changelog
* Tue Feb 24 2026 Vani <vani@fedora> - 2.0.0-1
- Update build macros to meet Fedora 43/44 Python packaging guidelines