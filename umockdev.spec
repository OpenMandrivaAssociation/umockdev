%define	major	0
%define	libname	%mklibname umockdev %{major}
%define	devname	%mklibname -d umockdev

Name:		umockdev
Version:	0.8.11
Release:	1
Summary:	Mock hardware devices

Group:		Development/C
License:	LGPLv2+
URL:		https://launchpad.net/umockdev
Source0:	https://launchpad.net/umockdev/trunk/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gudev-1.0) pkgconfig(systemd)
BuildRequires:	vala
# Required for tests
BuildRequires:	gphoto2
BuildRequires:	python3

%description
With this program and libraries you can easily create mock udev objects.
This is useful for writing tests for software which talks to
hardware devices.

%package -n	%{libname}
Summary:	Libraries for umockdev
Group:		System/Libraries

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
%setup -q

%build
%configure --enable-gtk-doc

%make

%install
%makeinstall_std

rm -r %{buildroot}%{_datadir}/doc/umockdev

%check
# Disabled for now, as the Xorg tests don't pass
# https://github.com/martinpitt/umockdev/issues/47
# make check

%files 
%doc README.rst
%{_bindir}/umockdev-*
%{_libdir}/girepository-1.0/UMockdev-1.0.typelib

%files -n %{libname}
%{_libdir}/libumockdev.so.%{major}*
%{_libdir}/libumockdev-preload.so.%{major}*

%files -n %{devname}
%doc docs/script-format.txt docs/examples/battery.c docs/examples/battery.py
%{_libdir}/libumockdev.so
%{_libdir}/pkgconfig/umockdev-1.0.pc
%{_datadir}/gir-1.0/UMockdev-1.0.gir
%{_includedir}/umockdev-1.0
%{_datadir}/gtk-doc/html/umockdev/
%{_datadir}/vala/vapi/umockdev-1.0.vapi
