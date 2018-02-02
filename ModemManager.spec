#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ModemManager
Version  : 1.6.12
Release  : 5
URL      : https://www.freedesktop.org/software/ModemManager/ModemManager-1.6.12.tar.xz
Source0  : https://www.freedesktop.org/software/ModemManager/ModemManager-1.6.12.tar.xz
Summary  : Common headers provided by ModemManager
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: ModemManager-bin
Requires: ModemManager-config
Requires: ModemManager-lib
Requires: ModemManager-data
Requires: ModemManager-locales
Requires: ModemManager-doc
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(polkit-gobject-1)

%description
ModemManager.
ModemManager provides a unified high level API for communicating with mobile
broadband modems, regardless of the protocol used to communicate with the
actual device (Generic AT, vendor-specific AT, QCDM, QMI, MBIM...).

%package bin
Summary: bin components for the ModemManager package.
Group: Binaries
Requires: ModemManager-data
Requires: ModemManager-config

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
Requires: ModemManager-lib
Requires: ModemManager-bin
Requires: ModemManager-data
Provides: ModemManager-devel

%description dev
dev components for the ModemManager package.


%package doc
Summary: doc components for the ModemManager package.
Group: Documentation

%description doc
doc components for the ModemManager package.


%package lib
Summary: lib components for the ModemManager package.
Group: Libraries
Requires: ModemManager-data

%description lib
lib components for the ModemManager package.


%package locales
Summary: locales components for the ModemManager package.
Group: Default

%description locales
locales components for the ModemManager package.


%prep
%setup -q -n ModemManager-1.6.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514386402
%configure --disable-static --without-mbim --without-qmi
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1514386402
rm -rf %{buildroot}
%make_install
%find_lang ModemManager

%files
%defattr(-,root,root,-)
/lib/udev/rules.d/77-mm-cinterion-port-types.rules
/lib/udev/rules.d/77-mm-dell-port-types.rules
/lib/udev/rules.d/77-mm-ericsson-mbm.rules
/lib/udev/rules.d/77-mm-haier-port-types.rules
/lib/udev/rules.d/77-mm-huawei-net-port-types.rules
/lib/udev/rules.d/77-mm-longcheer-port-types.rules
/lib/udev/rules.d/77-mm-mtk-port-types.rules
/lib/udev/rules.d/77-mm-nokia-port-types.rules
/lib/udev/rules.d/77-mm-pcmcia-device-blacklist.rules
/lib/udev/rules.d/77-mm-simtech-port-types.rules
/lib/udev/rules.d/77-mm-telit-port-types.rules
/lib/udev/rules.d/77-mm-usb-device-blacklist.rules
/lib/udev/rules.d/77-mm-usb-serial-adapters-greylist.rules
/lib/udev/rules.d/77-mm-x22x-port-types.rules
/lib/udev/rules.d/77-mm-zte-port-types.rules
/lib/udev/rules.d/80-mm-candidate.rules

%files bin
%defattr(-,root,root,-)
/usr/bin/ModemManager
/usr/bin/mmcli

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ModemManager.service

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/22x22/apps/ModemManager.png
/usr/share/polkit-1/actions/org.freedesktop.ModemManager1.policy

%files dev
%defattr(-,root,root,-)
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
/usr/include/libmm-glib/mm-call-properties.h
/usr/include/libmm-glib/mm-call.h
/usr/include/libmm-glib/mm-cdma-manual-activation-properties.h
/usr/include/libmm-glib/mm-enums-types.h
/usr/include/libmm-glib/mm-errors-types.h
/usr/include/libmm-glib/mm-firmware-properties.h
/usr/include/libmm-glib/mm-gdbus-bearer.h
/usr/include/libmm-glib/mm-gdbus-call.h
/usr/include/libmm-glib/mm-gdbus-manager.h
/usr/include/libmm-glib/mm-gdbus-modem.h
/usr/include/libmm-glib/mm-gdbus-sim.h
/usr/include/libmm-glib/mm-gdbus-sms.h
/usr/include/libmm-glib/mm-helper-types.h
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/ModemManager/libmm-plugin-altair-lte.so
/usr/lib64/ModemManager/libmm-plugin-anydata.so
/usr/lib64/ModemManager/libmm-plugin-cinterion.so
/usr/lib64/ModemManager/libmm-plugin-dell.so
/usr/lib64/ModemManager/libmm-plugin-ericsson-mbm.so
/usr/lib64/ModemManager/libmm-plugin-generic.so
/usr/lib64/ModemManager/libmm-plugin-haier.so
/usr/lib64/ModemManager/libmm-plugin-huawei.so
/usr/lib64/ModemManager/libmm-plugin-iridium.so
/usr/lib64/ModemManager/libmm-plugin-linktop.so
/usr/lib64/ModemManager/libmm-plugin-longcheer.so
/usr/lib64/ModemManager/libmm-plugin-motorola.so
/usr/lib64/ModemManager/libmm-plugin-mtk.so
/usr/lib64/ModemManager/libmm-plugin-nokia-icera.so
/usr/lib64/ModemManager/libmm-plugin-nokia.so
/usr/lib64/ModemManager/libmm-plugin-novatel.so
/usr/lib64/ModemManager/libmm-plugin-novatel_lte.so
/usr/lib64/ModemManager/libmm-plugin-option-hso.so
/usr/lib64/ModemManager/libmm-plugin-option.so
/usr/lib64/ModemManager/libmm-plugin-pantech.so
/usr/lib64/ModemManager/libmm-plugin-samsung.so
/usr/lib64/ModemManager/libmm-plugin-sierra-legacy.so
/usr/lib64/ModemManager/libmm-plugin-sierra.so
/usr/lib64/ModemManager/libmm-plugin-simtech.so
/usr/lib64/ModemManager/libmm-plugin-telit.so
/usr/lib64/ModemManager/libmm-plugin-thuraya.so
/usr/lib64/ModemManager/libmm-plugin-via.so
/usr/lib64/ModemManager/libmm-plugin-wavecom.so
/usr/lib64/ModemManager/libmm-plugin-x22x.so
/usr/lib64/ModemManager/libmm-plugin-zte.so
/usr/lib64/libmm-glib.so.0
/usr/lib64/libmm-glib.so.0.3.0

%files locales -f ModemManager.lang
%defattr(-,root,root,-)

