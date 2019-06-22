Name:       wlroots
Version:    0.6.0
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
%{_libdir}/libwlroots.so.3.4.1

%files devel
%{_libdir}/libwlroots.so.3
%{_libdir}/libwlroots.so
%{_libdir}/pkgconfig
%{_libdir}/pkgconfig/wlroots.pc
%dir %{_includedir}/wlr
%{_includedir}/wlr/config.h
%{_includedir}/wlr/version.h
%{_includedir}/wlr/backend.h
%{_includedir}/wlr/xcursor.h
%{_includedir}/wlr/xwayland.h
%{_includedir}/wlr/backend
%{_includedir}/wlr/backend/drm.h
%{_includedir}/wlr/backend/headless.h
%{_includedir}/wlr/backend/interface.h
%{_includedir}/wlr/backend/libinput.h
%{_includedir}/wlr/backend/multi.h
%{_includedir}/wlr/backend/noop.h
%{_includedir}/wlr/backend/session.h
%{_includedir}/wlr/backend/wayland.h
%{_includedir}/wlr/backend/x11.h
%{_includedir}/wlr/backend/session
%{_includedir}/wlr/backend/session/interface.h
%{_includedir}/wlr/interfaces
%{_includedir}/wlr/interfaces/wlr_input_device.h
%{_includedir}/wlr/interfaces/wlr_keyboard.h
%{_includedir}/wlr/interfaces/wlr_output.h
%{_includedir}/wlr/interfaces/wlr_pointer.h
%{_includedir}/wlr/interfaces/wlr_switch.h
%{_includedir}/wlr/interfaces/wlr_tablet_pad.h
%{_includedir}/wlr/interfaces/wlr_tablet_tool.h
%{_includedir}/wlr/interfaces/wlr_touch.h
%dir %{_includedir}/wlr/render
%{_includedir}/wlr/render/dmabuf.h
%{_includedir}/wlr/render/egl.h
%{_includedir}/wlr/render/drm_format_set.h
%{_includedir}/wlr/render/gles2.h
%{_includedir}/wlr/render/interface.h
%{_includedir}/wlr/render/wlr_renderer.h
%{_includedir}/wlr/render/wlr_texture.h
%dir %{_includedir}/wlr/types
%{_includedir}/wlr/types/wlr_box.h
%{_includedir}/wlr/types/wlr_buffer.h
%{_includedir}/wlr/types/wlr_compositor.h
%{_includedir}/wlr/types/wlr_cursor.h
%{_includedir}/wlr/types/wlr_data_control_v1.h
%{_includedir}/wlr/types/wlr_data_device.h
%{_includedir}/wlr/types/wlr_export_dmabuf_v1.h
%{_includedir}/wlr/types/wlr_foreign_toplevel_management_v1.h
%{_includedir}/wlr/types/wlr_fullscreen_shell_v1.h
%{_includedir}/wlr/types/wlr_gamma_control_v1.h
%{_includedir}/wlr/types/wlr_gamma_control.h
%{_includedir}/wlr/types/wlr_gtk_primary_selection.h
%{_includedir}/wlr/types/wlr_idle_inhibit_v1.h
%{_includedir}/wlr/types/wlr_idle.h
%{_includedir}/wlr/types/wlr_input_device.h
%{_includedir}/wlr/types/wlr_input_inhibitor.h
%{_includedir}/wlr/types/wlr_input_method_v2.h
%{_includedir}/wlr/types/wlr_keyboard.h
%{_includedir}/wlr/types/wlr_layer_shell_v1.h
%{_includedir}/wlr/types/wlr_linux_dmabuf_v1.h
%{_includedir}/wlr/types/wlr_list.h
%{_includedir}/wlr/types/wlr_matrix.h
%{_includedir}/wlr/types/wlr_output_damage.h
%{_includedir}/wlr/types/wlr_output_layout.h
%{_includedir}/wlr/types/wlr_output_management_v1.h
%{_includedir}/wlr/types/wlr_output.h
%{_includedir}/wlr/types/wlr_pointer_constraints_v1.h
%{_includedir}/wlr/types/wlr_pointer_gestures_v1.h
%{_includedir}/wlr/types/wlr_pointer.h
%{_includedir}/wlr/types/wlr_presentation_time.h
%{_includedir}/wlr/types/wlr_primary_selection_v1.h
%{_includedir}/wlr/types/wlr_primary_selection.h
%{_includedir}/wlr/types/wlr_region.h
%{_includedir}/wlr/types/wlr_relative_pointer_v1.h
%{_includedir}/wlr/types/wlr_screencopy_v1.h
%{_includedir}/wlr/types/wlr_screenshooter.h
%{_includedir}/wlr/types/wlr_seat.h
%{_includedir}/wlr/types/wlr_server_decoration.h
%{_includedir}/wlr/types/wlr_surface.h
%{_includedir}/wlr/types/wlr_switch.h
%{_includedir}/wlr/types/wlr_tablet_pad.h
%{_includedir}/wlr/types/wlr_tablet_tool.h
%{_includedir}/wlr/types/wlr_tablet_v2.h
%{_includedir}/wlr/types/wlr_text_input_v3.h
%{_includedir}/wlr/types/wlr_touch.h
%{_includedir}/wlr/types/wlr_virtual_keyboard_v1.h
%{_includedir}/wlr/types/wlr_xcursor_manager.h
%{_includedir}/wlr/types/wlr_xdg_decoration_v1.h
%{_includedir}/wlr/types/wlr_xdg_output_v1.h
%{_includedir}/wlr/types/wlr_xdg_shell_v6.h
%{_includedir}/wlr/types/wlr_xdg_shell.h
%dir %{_includedir}/wlr/util
%{_includedir}/wlr/util/edges.h
%{_includedir}/wlr/util/log.h
%{_includedir}/wlr/util/region.h

%changelog
* Sat Jun 15 2019 Denis Karpovskiy <geext29@gmail.com> - 0.6.0-1
- Initial package
