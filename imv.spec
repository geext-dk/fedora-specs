Name:           imv
Version:        3.1.0
Release:        1%{?dist}
Summary:        Image viewer for X11/Wayland

License:        MIT
URL:            https://github.com/eXeC64/imv
Source0:        https://github.com/eXeC64/imv/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  fontconfig-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  freeimage-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libcmocka-devel
BuildRequires:  asciidoc

Requires:       fontconfig
Requires:       SDL2
Requires:       SDL2_ttf
BuildRequires:  freeimage
BuildRequires:  librsvg2

%description
mv is a command line image viewer intended for use with tiling window managers.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}" CPPFLAGS="%{optflags}"

%install
PREFIX=%{buildroot}%{_prefix} CONFIGPREFIX=%{buildroot}%{_sysconfdir} make install

%check
%__make check

%files
%license LICENSE
%doc CHANGELOG
%doc README.md
%config(noreplace) %{_sysconfdir}/imv_config
%{_bindir}/imv
%{_mandir}/man1/imv.1.*
%{_mandir}/man5/imv.5.*
%{_datadir}/applications/imv.desktop


%changelog
* Wed Jun 19 2019 Denis Karpovskiy <geext29@gmail.com> - 3.1.0-1
- Initial package
