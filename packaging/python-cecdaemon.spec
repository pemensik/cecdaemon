%global srcname cecdaemon

%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-cecdaemon
Version:        1.0.0
Release:        2%{?dist}
Summary:        CEC Daemon for linux media centers

License:        MIT
URL:            https://github.com/simons-public/cecdaemon
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
cecdaemon is for managing the Consumer Electronics Control (CEC) capabilities
of your linux media center. Some embedded systems (like Raspberry Pi) have
native support for CEC. Many video cards do not have CEC capabilities, so you
may need an adapter like the one offered by PulseEight to use CEC with your computer.

Currently it is able to translate remote buttons to computer input, run shell
commands, and set the device name, and run shell scripts on standby and wake.


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-libcec
Requires:       python3-uinput

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
cecdaemon is for managing the Consumer Electronics Control (CEC) capabilities
of your linux media center. Some embedded systems (like Raspberry Pi) have
native support for CEC. Many video cards do not have CEC capabilities, so you
may need an adapter like the one offered by PulseEight to use CEC with your computer.

Provides generic python module cecdaemon.

%package -n %{srcname}
Summary:        %{summary}
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}
cecdaemon is for managing the Consumer Electronics Control (CEC) capabilities
of your linux media center. Some embedded systems (like Raspberry Pi) have
native support for CEC. Many video cards do not have CEC capabilities, so you
may need an adapter like the one offered by PulseEight to use CEC with your computer.

Currently it is able to translate remote buttons to computer input, run shell
commands, and set the device name, and run shell scripts on standby and wake.

Contains daemon itself.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n %{srcname}
%doc UINPUT-KEYS.md
%{_bindir}/cecdaemon
%{_bindir}/cecusercodes
%{_datadir}/cecdaemon

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info/

%changelog
* Wed Sep 28 2022 Petr Menšík <pemensik@redhat.com> - 1.0.0-2
- Move daemon to separate subpackage

* Wed Sep 28 2022 Petr Menšík <pemensik@redhat.com> - 1.0.0-1
- Initial package

