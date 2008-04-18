%define prel svn4612

Summary:	A simple CD burning tool for the Xfce Desktop Environment
Name:		xfburn
Version:	0.3.0
Release:	%mkrel -c %{prel} 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org/projects/xfburn/
Source0:	%{name}-%{version}-%{prel}.tar.bz2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	thunar-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	libburn-devel
BuildRequires:	libisofs-devel
BuildRequires:	xfce4-dev-tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfburn is a simple CD/DVD burning tool based on libburnia 
libraries.It can blank CD-RWs, burn and create iso images, 
as well as burn personal compositions of data to either CD or DVD.

%prep
%setup -qn %{name}

./autogen.sh

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
%doc AUTHORS ChangeLog  TODO
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*.ui
%{_iconsdir}/hicolor/*
