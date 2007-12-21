Summary:	A simple CD burning tool for the Xfce Desktop Environment
Name:		xfburn
Version:	0.2.0
Release:	%mkrel 7
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://foo-projects.org/~pollux/xfburn
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.2.0-cdrkit.patch
BuildRequires:	libxfcegui4-devel >= 4.3.90.2 
BuildRequires:	dbus-devel
BuildRequires:	thunar-devel
BuildRequires:	hal-devel
BuildRequires:	exo-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
##1 or more are needed for burning
Requires:	cdrkit
Requires:	cdrkit-genisoimage
Requires:	cdrdao
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfburn is a simple CD burning tool acting as a front-end 
to mkisofs, cdrdao, readcd and cdrecord. It can blank CD-RW, 
copy CDs, burn and create iso images, and burn personal 
composition of data.

%prep
%setup -q
%patch0 -p1 -b .cdrkit
%build
# Disable check for burning software, only used at runtime
export cdrdao_found=yes
export cdrecord_found=yes
export mkisofs_found=yes
export readcd_found=yes

%configure2_5x \
	--enable-final \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert icons/24x24/stock_xfburn-burn-cd.png -geometry 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert icons/24x24/stock_xfburn-burn-cd.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert icons/24x24/stock_xfburn-burn-cd.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

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

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor 

%files  -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*.ui
%{_iconsdir}/hicolor/*
