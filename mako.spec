Name:           mako
Version:        1.3
Release:        1%{?dist}
Summary:        A lightweight Wayland notification daemon

License:        MIT
URL:            https://wayland.emersion.fr/mako
Source0:        https://github.com/emersion/mako/releases/download/v%{version}/mako-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  systemd-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  scdoc

Requires:       libwayland-client
Requires:       pango
Requires:       cairo
Requires:       systemd

%description
A lightweight notification daemon for Wayland. Works on Sway.

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
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1.*
%{_mandir}/man1/makoctl.1.*


%changelog
* Wed Jun 19 2019 Denis Karpovskiy <geext29@gmail.com> - 1.3-1
- Initial package
