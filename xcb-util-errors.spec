Name:           xcb-util-errors
Version:        1.0
Release:        1%{?dist}
Summary:        XCB utility functions for error handling

License:        MIT
URL:            https://cgit.freedesktop.org/xcb/util-errors/
Source0:        https://xcb.freedesktop.org/dist/xcb-util-errors-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(x11)

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
autoreconf -vfi
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/libxcb-errors.la

%check
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libxcb-errors.so.0.0.0
%license COPYING

%files devel
%dir %{_includedir}/xcb
%{_includedir}/xcb/xcb_errors.h
%{_libdir}/libxcb-errors.so.0
%{_libdir}/libxcb-errors.so
%{_libdir}/pkgconfig/xcb-errors.pc

%changelog
* Sat Jun 15 2019 Denis Karpovskiy <geext29@gmail.com> - 1.0-1
- Initial build

