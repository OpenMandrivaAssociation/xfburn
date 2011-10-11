%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A simple CD burning tool for the Xfce Desktop Environment
Name:		xfburn
Version:	0.4.3
Release:	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org/projects/xfburn/
Source0:	http://archive.xfce.org/src/apps/xfburn/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	libburn-devel
BuildRequires:	libisofs-devel
BuildRequires:	xfce4-dev-tools
BuildRequires:	dbus-glib-devel
BuildRequires:	gstreamer0.10-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
%if %mdkver >= 201200
BuildConflicts:	hal-devel
%else
BuildRequires:	hal-devel
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfburn is a simple CD/DVD burning tool based on libburnia 
libraries.It can blank CD-RWs, burn and create iso images, 
as well as burn personal compositions of data to either CD or DVD.

%prep
%setup -q

%build
%configure2_5x \
	--enable-final \
	--disable-static \
	%if %mdkver >= 201200
	--disable-hal \
	%endif
	--enable-dbus \
	--enable-gstreamer

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
#cp -f icons/scalable/stock_xfburn-burn-cd.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

desktop-file-install \
    --add-only-show-in="XFCE" \
    --remove-category="X-XFCE" \
    --remove-category="Archiving" \
    --remove-category="Utility" \
    --add-category="AudioVideo" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/* 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor 
%endif

%files  -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog  TODO
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*.ui
%{_datadir}/Thunar/sendto/thunar-sendto-xfburn.desktop
%{_iconsdir}/hicolor/*
%{_mandir}/man1/*
