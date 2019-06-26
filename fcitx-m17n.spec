Name: fcitx-m17n
Version:	0.2.4
Release: 3
Source0: http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
Summary: M17N plugin for fcitx
URL: http://www.fcitx-im.org
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(m17n-core)
Requires: m17n-db

%description
M17N plugin for fcitx.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %{name}

%files -f %name.lang
%{_libdir}/fcitx/fcitx-m17n.so
%{_datadir}/fcitx/addon/fcitx-m17n.conf
%{_datadir}/fcitx/configdesc/fcitx-m17n.desc
%{_datadir}/fcitx/m17n
