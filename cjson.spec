Name:       cjson
Version:    1.7.10
Release:    1%{?dist}
Summary:    Ultra-lightweight JSON parser in ANSI C 

License:    MIT
URL:        https://github.com/DaveGamble/cJSON
Source0:    https://github.com/DaveGamble/cJSON/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc

%description
cJSON aims to be the dumbest possible parser that you can get your job done
with. It's a single file of C, and a single header file.
JSON is described best here: http://www.json.org/. It's like XML, but fat-free.
You use it to move data around, store things, or just generally represent your
program's state.
As a library, cJSON exists to take away as much legwork as it can, but not get
in your way. As a point of pragmatism (i.e. ignoring the truth), I'm going to
say that you can use it in one of two modes: Auto and Manual.

%package devel
Summary: Development files for the cJSON library
Requires: cjson
%description devel
Development files for the cJSON including cmake configuration
files, pkg-config file and unversioned shared library

%package static
Summary: cJSON library compiled statically
Requires: cjson-devel
%description static
The cJSON library compiled statically

%prep
%setup -q -n cJSON-1.7.10

%build
mkdir build
pushd build
%cmake .. -DENABLE_CJSON_TEST=Off -DENABLE_CJSON_UTILS=Off -DBUILD_SHARED_AND_STATIC_LIBS=On
%__make %{?_smp_mflags}

%install
pushd build
%make_install
install -m 0755 -d %{buildroot}%{_pkgdocdir}
install -m 0644 %{_builddir}/cJSON-%version/README.md       %{buildroot}%{_pkgdocdir}/README.md
install -m 0644 %{_builddir}/cJSON-%version/CHANGELOG.md    %{buildroot}%{_pkgdocdir}/CHANGELOG.md
install -m 0644 %{_builddir}/cJSON-%version/CONTRIBUTORS.md %{buildroot}%{_pkgdocdir}/CONTRIBUTORS.md

%files
%license LICENSE
%{_libdir}/libcjson.so.1
%{_libdir}/libcjson.so.%{version}
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/CHANGELOG.md
%doc %{_pkgdocdir}/CONTRIBUTORS.md

%files devel
%{_includedir}/cjson/cJSON.h
%dir %{_libdir}/cmake/cJSON
%{_libdir}/cmake/cJSON/cjson.cmake
%{_libdir}/cmake/cJSON/cJSONConfig.cmake
%{_libdir}/cmake/cJSON/cJSONConfigVersion.cmake
%{_libdir}/cmake/cJSON/cjson-noconfig.cmake
%{_libdir}/pkgconfig/libcjson.pc
%{_libdir}/libcjson.so

%files static
%{_libdir}/libcjson.a

%changelog
* Wed Dec 26 2018 Denis Karpovskiy <geext29@gmail.com> - 1.7.10-1
- Initial package
