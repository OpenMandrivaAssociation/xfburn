Summary:	A simple CD burning tool for the Xfce Desktop Environment
Name:		xfburn
Version:	0.3.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org/projects/xfburn/
Source0:	http://goodies.xfce.org/releases/xfburn/%{name}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	thunar-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	libburn-devel
BuildRequires:	libisofs-devel
BuildRequires:	xfce4-dev-tools
BuildRequires:	dbus-glib-devel
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
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
cp -f icons/scalable/stock_xfburn-burn-cd.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

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
%{_iconsdir}/hicolor/*
