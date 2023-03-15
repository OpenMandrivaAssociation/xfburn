%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	A simple CD burning tool for the Xfce Desktop Environment
Name:		xfburn
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org/projects/xfburn/
Source0:	http://archive.xfce.org/src/apps/xfburn/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(libburn-1)
BuildRequires:	pkgconfig(libisofs-1)
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

%description
Xfburn is a simple CD/DVD burning tool based on libburnia 
libraries.It can blank CD-RWs, burn and create iso images, 
as well as burn personal compositions of data to either CD or DVD.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-gudev \
	--enable-dbus \
	--enable-gstreamer

%make_build

%install
%make_install

desktop-file-install \
    --add-only-show-in="XFCE" \
    --remove-category="X-XFCE" \
    --remove-category="Archiving" \
    --remove-category="Utility" \
    --add-category="AudioVideo" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/* 

%find_lang %{name}

%files  -f %{name}.lang
%doc AUTHORS ChangeLog TODO README*
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/metainfo/org.xfce.xfburn.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*.ui
%{_datadir}/Thunar/sendto/thunar-sendto-xfburn.desktop
%{_iconsdir}/hicolor/*
%{_mandir}/man1/*
