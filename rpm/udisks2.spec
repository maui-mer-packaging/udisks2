# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       udisks2

# >> macros
# << macros
%define libatasmart_version 0.17
%define dbus_version 1.2
%define smp_utils_version 0.94
%define mdadm_version 2.6.7
%define parted_version 1.8.8
%define udev_version 165
%define glib2_version 2.31.13
%define polkit_version 0.92
%define device_mapper_version 1.02
%define sg3_utils_version 1.27
%define dbus_glib_version 0.82

Summary:    Disk Manager
Version:    2.1.3
Release:    1
Group:      System/Libraries
License:    GPLv2+
URL:        http://www.freedesktop.org/wiki/Software/udisks
Source0:    %{name}-%{version}.tar.xz
Source100:  udisks2.yaml
Requires:   dbus >= %{dbus_version}
Requires:   udev >= %{udev_version}
Requires:   util-linux
Requires:   e2fsprogs
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gudev-1.0) >= %{udev_version}
BuildRequires:  pkgconfig(libatasmart) >= %{libatasmart_version}
BuildRequires:  pkgconfig(libsystemd) >= 44
BuildRequires:  pkgconfig(polkit-agent-1) >= %{polkit_version}
BuildRequires:  pkgconfig(polkit-gobject-1) >= %{polkit_version}
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev) >= %{udev_version}
BuildRequires:  pkgconfig(dbus-1) >= %{dbus_version}
BuildRequires:  pkgconfig(dbus-glib-1) >= %{dbus_glib_version}
BuildRequires:  pkgconfig(libparted) >= %{parted_version}
BuildRequires:  pkgconfig(devmapper) >= %{device_mapper_version}
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  gnome-common
BuildRequires:  libacl-devel
BuildRequires:  python
BuildRequires:  sg3_utils-devel >= %{sg3_utils_version}
Provides:   DeviceKit-disks = 010
Conflicts:   kernel < 2.6.26
Obsoletes:   DeviceKit-disks <= 009

%description
udisks provides a daemon, D-Bus API and command line tools for
managing disks and storage devices. This package is for the udisks 2.x
series.


%package -n libudisks2
Summary:    Dynamic library to access the udisks daemon
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libudisks2
This package contains the dynamic library libudisks2, which provides
access to the udisks daemon. This package is for the udisks 2.x
series.


%package -n libudisks2-devel
Summary:    Development files for libudisks2
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libudisks2 = %{version}-%{release}
Requires:   pkgconfig

%description -n libudisks2-devel
This package contains the development files for the library
libudisks2, a dynamic library, which provides access to the udisks
daemon. This package is for the udisks 2.x series.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static \
    --disable-man-pages \
    --disable-man \
    --disable-gtk-doc \
    --disable-gtk-doc-html

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%find_lang udisks2

%post -n libudisks2 -p /sbin/ldconfig

%postun -n libudisks2 -p /sbin/ldconfig

%files -f udisks2.lang
%defattr(-,root,root,-)
%doc README AUTHORS NEWS COPYING HACKING
%dir %{_sysconfdir}/udisks2
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_datadir}/bash-completion/completions/udisksctl
%{_prefix}/lib/systemd/system/udisks2.service
%{_prefix}/lib/udev/rules.d/80-udisks2.rules
%{_sbindir}/umount.udisks2
%dir %{_prefix}/lib/udisks2
%{_prefix}/lib/udisks2/udisksd
%{_bindir}/udisksctl
%{_datadir}/polkit-1/actions/org.freedesktop.udisks2.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
# >> files
# << files

%files -n libudisks2
%defattr(-,root,root,-)
%{_libdir}/libudisks2.so.*
%{_libdir}/girepository-1.0/UDisks-2.0.typelib
# >> files libudisks2
# << files libudisks2

%files -n libudisks2-devel
%defattr(-,root,root,-)
%{_libdir}/libudisks2.so
%dir %{_includedir}/udisks2
%dir %{_includedir}/udisks2/udisks
%{_includedir}/udisks2/udisks/*.h
%{_datadir}/gir-1.0/UDisks-2.0.gir
%{_libdir}/pkgconfig/udisks2.pc
# >> files libudisks2-devel
# << files libudisks2-devel
