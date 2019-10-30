Name:           sway
Version:        1.2
Release:        1%{?dist}
Summary:        sway is an i3-compatible Wayland compositor

License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/swaywm/sway/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  wlroots-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pcre-devel
BuildRequires:  json-c-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libevdev-devel
BuildRequires:  scdoc

Requires:       wlroots
Requires:       pcre
Requires:       json-c
Requires:       pango
Requires:       cairo

Recommends:     swaybg

%description


%prep
%autosetup


%build
%meson
%meson_build

%install
%meson_install

%check

%files
%license LICENSE
%doc README.*.md
%doc README.md
%{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%dir %{_sysconfdir}/sway
%{_sysconfdir}/sway/config
%dir %{_sysconfdir}/sway/security.d
%{_sysconfdir}/sway/security.d/00-defaults
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_768x1024.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_768x1024_Portrait.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_1136x640.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_1136x640_Portrait.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_1366x768.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_1920x1080.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_2048x1536.png
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_2048x1536_Portrait.png
%{_datadir}/zsh/site-functions/_sway
%{_datadir}/zsh/site-functions/_swaymsg
%{_datadir}/bash-completion/completions/sway
%{_datadir}/bash-completion/completions/swaybar
%{_datadir}/bash-completion/completions/swaymsg
%{_datadir}/fish/completions/sway.fish
%{_datadir}/fish/completions/swaymsg.fish
%{_datadir}/fish/completions/swaynag.fish
%{_datadir}/wayland-sessions/sway.desktop
%{_mandir}/man1/sway.1.*
%{_mandir}/man1/swaymsg.1.*
%{_mandir}/man1/swaynag.1.*
%{_mandir}/man5/sway.5.*
%{_mandir}/man5/sway-bar.5.*
%{_mandir}/man5/sway-input.5.*
%{_mandir}/man5/sway-output.5.*
%{_mandir}/man5/swaynag.5.*
%{_mandir}/man7/sway-ipc.7.*
%{_mandir}/man7/swaybar-protocol.7.*

%changelog
* Sat Sep 14 2019 Denis Karpovskiy <geext29@gmail.com> - 1.2-1
- Update to 1.2

* Wed Jun 19 2019 Denis Karpovskiy <geext29@gmail.com> - 1.1.1-3
- Add English README

* Tue Jun 18 2019 Denis Karpovskiy <geext29@gmail.com> - 1.1.1-2
- Add recommend for swaybg
- Add the LICENSE file
- Add the README files
- Remove dependency on particular man compression

* Sat Jun 15 2019 Denis Karpovskiy <geext29@gmail.com> - 1.1.1-1
- Initial package

