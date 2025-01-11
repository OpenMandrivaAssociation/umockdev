%define major 0
%define libname %mklibname umockdev
%define oldlibname %mklibname umockdev 0
%define devname %mklibname -d umockdev

Name:		umockdev
Version:	0.19.0
Release:	2
Summary:	Mock hardware devices

Group:		Development/C
License:	LGPLv2+
URL:		https://launchpad.net/umockdev
Source0:	https://github.com/martinpitt/umockdev/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  clang = 19.1.5
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:	gtk-doc
BuildRequires:  pkgconfig(libpcap)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(udev)
BuildRequires:	vala
# Required for tests
BuildRequires:	gphoto2
BuildRequires:	python

%description
With this program and libraries you can easily create mock udev objects.
This is useful for writing tests for software which talks to
hardware devices.

%package -n	%{libname}
Summary:	Libraries for umockdev
Group:		System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
Libraries for umockdev.

%package -n	%{devname}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
The %{name}-devel package contains the libraries to develop
using %{name}.

%prep
%autosetup -p1

%build
# Due https://github.com/martinpitt/umockdev/issues/260
#export CC=gcc
#export CXX=g++
%meson

%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete
#rm -r %{buildroot}%{_datadir}/doc/umockdev

%check
# Disabled for now, as the Xorg tests don't pass
# https://github.com/martinpitt/umockdev/issues/47
# make check

%files 
%doc README.md
%{_bindir}/umockdev-*
%{_libdir}/girepository-1.0/UMockdev-1.0.typelib

%files -n %{libname}
%{_libdir}/libumockdev.so.%{major}*
%{_libdir}/libumockdev-preload.so.%{major}*

%files -n %{devname}
%doc docs/script-format.txt docs/examples/battery.c docs/examples/battery.py
%{_libdir}/libumockdev.so
%{_libdir}/libumockdev-preload.so
%{_libdir}/pkgconfig/umockdev-1.0.pc
%{_datadir}/gir-1.0/UMockdev-1.0.gir
%{_includedir}/umockdev-1.0
%{_datadir}/vala/vapi/umockdev-1.0.vapi
