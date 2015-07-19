%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-m17n
Version: 0.2.0
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 10
Source0: http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: M17N plugin for fcitx
URL: http://www.fcitx-im.org
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(m17n-core)

%track
prog %{name} = {
	url = http://download.fcitx-im.org/%{name}
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
M17N plugin for fcitx

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%_libdir/fcitx/fcitx-m17n.so
%_datadir/fcitx/addon/fcitx-m17n.conf
%_datadir/fcitx/configdesc/fcitx-m17n.desc
%_datadir/fcitx/m17n
