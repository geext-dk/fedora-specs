Name:       wlroots
Version:    0.7.0
Release:    1%{?dist}
Summary:    Pluggable, composable, unopinionated modules for building a Wayland compositor

License:    MIT
URL:        https://github.com/swaywm/wlroots
Source0:    https://github.com/swaywm/wlroots/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  systemd-devel
BuildRequires:  pixman-devel
BuildRequires:  freerdp-devel
BuildRequires:  libwinpr-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-errors-devel
BuildRequires:  libcap-devel

%description
wlroots implements a huge variety of Wayland compositor features and implements them right, so you can focus on the features that make your compositor unique. By using wlroots, you get high performance, excellent hardware compatibility, broad support for many wayland interfaces, and comfortable development tools - or any subset of these features you like, because all of them work independently of one another and freely compose with anything you want to implement yourself.

%package devel
Summary: Development files for the wlroots library

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}


%description devel
Development files for the wlroots library

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/libwlroots.so.3.5.1

%files devel
%{_libdir}/libwlroots.so.3
%{_libdir}/libwlroots.so
%{_libdir}/pkgconfig/wlroots.pc
%{_includedir}/wlr

%changelog
* Sat Sep 14 2019 Denis Karpovskiy <geext29@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Sat Jun 15 2019 Denis Karpovskiy <geext29@gmail.com> - 0.6.0-1
- Initial package
