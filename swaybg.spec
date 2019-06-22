Name:           swaybg
Version:        1.0
Release:        2%{?dist}
Summary:        Wallpaper tool for Wayland compositors

License:        MIT
URL:            https://github.com/swaywm/swaybg
Source0:        https://github.com/swaywm/swaybg/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  scdoc
BuildRequires:  git

Requires:       libwayland-client
Requires:       cairo

%description
swaybg is a wallpaper utility for Wayland compositors. It is compatible with
any Wayland compositor which implements the following Wayland protocols.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/swaybg.1.*
%{_bindir}/swaybg

%changelog
* Wed Jun 19 2019 Denis Karpovskiy <geext29@gmail.com> - 1.0-2
- Fix wayland dependencies

* Tue Jun 18 2019 Denis Karpovskiy <geext29@gmail.com> - 1.0-1
- Initial package
