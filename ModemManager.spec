#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3CAD53398973FFFA (aleksander@aleksander.es)
#
Name     : ModemManager
Version  : 1.16.4
Release  : 29
URL      : https://www.freedesktop.org/software/ModemManager/ModemManager-1.16.4.tar.xz
Source0  : https://www.freedesktop.org/software/ModemManager/ModemManager-1.16.4.tar.xz
Source1  : https://www.freedesktop.org/software/ModemManager/ModemManager-1.16.4.tar.xz.asc
Summary  : Common headers provided by ModemManager
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: ModemManager-bin = %{version}-%{release}
Requires: ModemManager-config = %{version}-%{release}
Requires: ModemManager-data = %{version}-%{release}
Requires: ModemManager-lib = %{version}-%{release}
Requires: ModemManager-license = %{version}-%{release}
Requires: ModemManager-locales = %{version}-%{release}
Requires: ModemManager-man = %{version}-%{release}
Requires: ModemManager-services = %{version}-%{release}
Requires: mobile-broadband-provider-info
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : mobile-broadband-provider-info
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(mbim-glib)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(qmi-glib)
BuildRequires : vala

%description
ModemManager.
ModemManager provides a unified high level API for communicating with mobile
broadband modems, regardless of the protocol used to communicate with the
actual device (Generic AT, vendor-specific AT, QCDM, QMI, MBIM...).

%package bin
Summary: bin components for the ModemManager package.
Group: Binaries
Requires: ModemManager-data = %{version}-%{release}
Requires: ModemManager-config = %{version}-%{release}
Requires: ModemManager-license = %{version}-%{release}
Requires: ModemManager-services = %{version}-%{release}

%description bin
bin components for the ModemManager package.


%package config
Summary: config components for the ModemManager package.
Group: Default

%description config
config components for the ModemManager package.


%package data
Summary: data components for the ModemManager package.
Group: Data

%description data
data components for the ModemManager package.


%package dev
Summary: dev components for the ModemManager package.
Group: Development
Requires: ModemManager-lib = %{version}-%{release}
Requires: ModemManager-bin = %{version}-%{release}
Requires: ModemManager-data = %{version}-%{release}
Provides: ModemManager-devel = %{version}-%{release}
Requires: ModemManager = %{version}-%{release}

%description dev
dev components for the ModemManager package.


%package lib
Summary: lib components for the ModemManager package.
Group: Libraries
Requires: ModemManager-data = %{version}-%{release}
Requires: ModemManager-license = %{version}-%{release}

%description lib
lib components for the ModemManager package.


%package license
Summary: license components for the ModemManager package.
Group: Default

%description license
license components for the ModemManager package.


%package locales
Summary: locales components for the ModemManager package.
Group: Default

%description locales
locales components for the ModemManager package.


%package man
Summary: man components for the ModemManager package.
Group: Default

%description man
man components for the ModemManager package.


%package services
Summary: services components for the ModemManager package.
Group: Systemd services

%description services
services components for the ModemManager package.


%prep
%setup -q -n ModemManager-1.16.4
cd %{_builddir}/ModemManager-1.16.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619107448
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static --with-dbus-sys-dir=/usr/share/dbus-1/system.d \
--with-udev-base-dir=/usr/lib/udev/ \
--with-polkit=no \
--with-systemd-journal=no
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1619107448
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ModemManager
cp %{_builddir}/ModemManager-1.16.4/COPYING %{buildroot}/usr/share/package-licenses/ModemManager/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/ModemManager-1.16.4/COPYING.LIB %{buildroot}/usr/share/package-licenses/ModemManager/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
%find_lang ModemManager
## install_append content
ln -s ModemManager.service %{buildroot}/usr/lib/systemd/system/dbus-org.freedesktop.ModemManager1.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ModemManager
/usr/bin/mmcli

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/77-mm-broadmobi-port-types.rules
/usr/lib/udev/rules.d/77-mm-cinterion-port-types.rules
/usr/lib/udev/rules.d/77-mm-dell-port-types.rules
/usr/lib/udev/rules.d/77-mm-dlink-port-types.rules
/usr/lib/udev/rules.d/77-mm-ericsson-mbm.rules
/usr/lib/udev/rules.d/77-mm-fibocom-port-types.rules
/usr/lib/udev/rules.d/77-mm-foxconn-port-types.rules
/usr/lib/udev/rules.d/77-mm-gosuncn-port-types.rules
/usr/lib/udev/rules.d/77-mm-haier-port-types.rules
/usr/lib/udev/rules.d/77-mm-huawei-net-port-types.rules
/usr/lib/udev/rules.d/77-mm-longcheer-port-types.rules
/usr/lib/udev/rules.d/77-mm-mtk-port-types.rules
/usr/lib/udev/rules.d/77-mm-nokia-port-types.rules
/usr/lib/udev/rules.d/77-mm-pcmcia-device-blacklist.rules
/usr/lib/udev/rules.d/77-mm-quectel-port-types.rules
/usr/lib/udev/rules.d/77-mm-sierra.rules
/usr/lib/udev/rules.d/77-mm-simtech-port-types.rules
/usr/lib/udev/rules.d/77-mm-telit-port-types.rules
/usr/lib/udev/rules.d/77-mm-tplink-port-types.rules
/usr/lib/udev/rules.d/77-mm-ublox-port-types.rules
/usr/lib/udev/rules.d/77-mm-usb-device-blacklist.rules
/usr/lib/udev/rules.d/77-mm-usb-serial-adapters-greylist.rules
/usr/lib/udev/rules.d/77-mm-x22x-port-types.rules
/usr/lib/udev/rules.d/77-mm-zte-port-types.rules
/usr/lib/udev/rules.d/80-mm-candidate.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/ModemManager-1.0.typelib
/usr/share/ModemManager/mm-foxconn-t77w968-carrier-mapping.conf
/usr/share/bash-completion/completions/mmcli
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Bearer.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Call.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Firmware.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Location.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Messaging.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.ModemCdma.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Oma.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Signal.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Simple.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Time.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Voice.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Sim.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Sms.xml
/usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.xml
/usr/share/dbus-1/system-services/org.freedesktop.ModemManager1.service
/usr/share/dbus-1/system.d/org.freedesktop.ModemManager1.conf
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/22x22/apps/ModemManager.png

%files dev
%defattr(-,root,root,-)
/usr/include/ModemManager/ModemManager-compat.h
/usr/include/ModemManager/ModemManager-enums.h
/usr/include/ModemManager/ModemManager-errors.h
/usr/include/ModemManager/ModemManager-names.h
/usr/include/ModemManager/ModemManager-version.h
/usr/include/ModemManager/ModemManager.h
/usr/include/libmm-glib/libmm-glib.h
/usr/include/libmm-glib/mm-bearer-ip-config.h
/usr/include/libmm-glib/mm-bearer-properties.h
/usr/include/libmm-glib/mm-bearer-stats.h
/usr/include/libmm-glib/mm-bearer.h
/usr/include/libmm-glib/mm-call-audio-format.h
/usr/include/libmm-glib/mm-call-properties.h
/usr/include/libmm-glib/mm-call.h
/usr/include/libmm-glib/mm-cdma-manual-activation-properties.h
/usr/include/libmm-glib/mm-enums-types.h
/usr/include/libmm-glib/mm-errors-types.h
/usr/include/libmm-glib/mm-firmware-properties.h
/usr/include/libmm-glib/mm-firmware-update-settings.h
/usr/include/libmm-glib/mm-gdbus-bearer.h
/usr/include/libmm-glib/mm-gdbus-call.h
/usr/include/libmm-glib/mm-gdbus-manager.h
/usr/include/libmm-glib/mm-gdbus-modem.h
/usr/include/libmm-glib/mm-gdbus-sim.h
/usr/include/libmm-glib/mm-gdbus-sms.h
/usr/include/libmm-glib/mm-helper-types.h
/usr/include/libmm-glib/mm-kernel-event-properties.h
/usr/include/libmm-glib/mm-location-3gpp.h
/usr/include/libmm-glib/mm-location-cdma-bs.h
/usr/include/libmm-glib/mm-location-common.h
/usr/include/libmm-glib/mm-location-gps-nmea.h
/usr/include/libmm-glib/mm-location-gps-raw.h
/usr/include/libmm-glib/mm-manager.h
/usr/include/libmm-glib/mm-modem-3gpp-ussd.h
/usr/include/libmm-glib/mm-modem-3gpp.h
/usr/include/libmm-glib/mm-modem-cdma.h
/usr/include/libmm-glib/mm-modem-firmware.h
/usr/include/libmm-glib/mm-modem-location.h
/usr/include/libmm-glib/mm-modem-messaging.h
/usr/include/libmm-glib/mm-modem-oma.h
/usr/include/libmm-glib/mm-modem-signal.h
/usr/include/libmm-glib/mm-modem-simple.h
/usr/include/libmm-glib/mm-modem-time.h
/usr/include/libmm-glib/mm-modem-voice.h
/usr/include/libmm-glib/mm-modem.h
/usr/include/libmm-glib/mm-network-timezone.h
/usr/include/libmm-glib/mm-object.h
/usr/include/libmm-glib/mm-pco.h
/usr/include/libmm-glib/mm-signal.h
/usr/include/libmm-glib/mm-sim.h
/usr/include/libmm-glib/mm-simple-connect-properties.h
/usr/include/libmm-glib/mm-simple-status.h
/usr/include/libmm-glib/mm-sms-properties.h
/usr/include/libmm-glib/mm-sms.h
/usr/include/libmm-glib/mm-unlock-retries.h
/usr/lib64/libmm-glib.so
/usr/lib64/pkgconfig/ModemManager.pc
/usr/lib64/pkgconfig/mm-glib.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/ModemManager/libmm-plugin-altair-lte.so
/usr/lib64/ModemManager/libmm-plugin-anydata.so
/usr/lib64/ModemManager/libmm-plugin-broadmobi.so
/usr/lib64/ModemManager/libmm-plugin-cinterion.so
/usr/lib64/ModemManager/libmm-plugin-dell.so
/usr/lib64/ModemManager/libmm-plugin-dlink.so
/usr/lib64/ModemManager/libmm-plugin-ericsson-mbm.so
/usr/lib64/ModemManager/libmm-plugin-fibocom.so
/usr/lib64/ModemManager/libmm-plugin-foxconn.so
/usr/lib64/ModemManager/libmm-plugin-generic.so
/usr/lib64/ModemManager/libmm-plugin-gosuncn.so
/usr/lib64/ModemManager/libmm-plugin-haier.so
/usr/lib64/ModemManager/libmm-plugin-huawei.so
/usr/lib64/ModemManager/libmm-plugin-iridium.so
/usr/lib64/ModemManager/libmm-plugin-linktop.so
/usr/lib64/ModemManager/libmm-plugin-longcheer.so
/usr/lib64/ModemManager/libmm-plugin-motorola.so
/usr/lib64/ModemManager/libmm-plugin-mtk.so
/usr/lib64/ModemManager/libmm-plugin-nokia-icera.so
/usr/lib64/ModemManager/libmm-plugin-nokia.so
/usr/lib64/ModemManager/libmm-plugin-novatel-lte.so
/usr/lib64/ModemManager/libmm-plugin-novatel.so
/usr/lib64/ModemManager/libmm-plugin-option-hso.so
/usr/lib64/ModemManager/libmm-plugin-option.so
/usr/lib64/ModemManager/libmm-plugin-pantech.so
/usr/lib64/ModemManager/libmm-plugin-quectel.so
/usr/lib64/ModemManager/libmm-plugin-samsung.so
/usr/lib64/ModemManager/libmm-plugin-sierra-legacy.so
/usr/lib64/ModemManager/libmm-plugin-sierra.so
/usr/lib64/ModemManager/libmm-plugin-simtech.so
/usr/lib64/ModemManager/libmm-plugin-telit.so
/usr/lib64/ModemManager/libmm-plugin-thuraya.so
/usr/lib64/ModemManager/libmm-plugin-tplink.so
/usr/lib64/ModemManager/libmm-plugin-ublox.so
/usr/lib64/ModemManager/libmm-plugin-via.so
/usr/lib64/ModemManager/libmm-plugin-wavecom.so
/usr/lib64/ModemManager/libmm-plugin-x22x.so
/usr/lib64/ModemManager/libmm-plugin-zte.so
/usr/lib64/ModemManager/libmm-shared-foxconn.so
/usr/lib64/ModemManager/libmm-shared-icera.so
/usr/lib64/ModemManager/libmm-shared-novatel.so
/usr/lib64/ModemManager/libmm-shared-option.so
/usr/lib64/ModemManager/libmm-shared-sierra.so
/usr/lib64/ModemManager/libmm-shared-telit.so
/usr/lib64/ModemManager/libmm-shared-xmm.so
/usr/lib64/libmm-glib.so.0
/usr/lib64/libmm-glib.so.0.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ModemManager/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/ModemManager/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mmcli.1
/usr/share/man/man8/ModemManager.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ModemManager.service
/usr/lib/systemd/system/dbus-org.freedesktop.ModemManager1.service

%files locales -f ModemManager.lang
%defattr(-,root,root,-)

