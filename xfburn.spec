 
#%define iconname xfburn.png

%define version     0.2.0
%define release     3
%define __libtoolize    /bin/true


Summary:    A simple CD burning tool for the Xfce Desktop Environment
Name:       xfburn
Version:    %{version}
Release:    %mkrel %{release}
License:    GPL
URL:         http://foo-projects.org/~pollux/xfburn
Source0:    %{name}-%{version}.tar.bz2 
Group:      Graphical desktop/Xfce
BuildRoot:  %{_tmppath}/%{name}-root
BuildRequires:  libxfcegui4-devel >= 4.3.90.2 
BuildRequires:  dbus-devel
BuildRequires:  thunar-devel
BuildRequires:  hal-devel
BuildRequires:  exo-devel
BuildRequires:  ImageMagick
BuildRequires:	desktop-file-utils
##1 or more are needed for burning
Requires: cdrecord
Requires: mkisofs
Requires: cdrdao

%description
Xfburn is a simple CD burning tool acting as a front-end to
mkisofs, cdrdao, readcd and cdrecord; it is based on gtk+

This version is considered alpha, it's not feature complete and
certainly presents bugs.

The 0.1.0 version supports:
 o blanking cd-rw
 o copying cd
 o burning iso images
 o creating iso images
 o burning a personal composition of files

In the future (no need to fill feature requests for these ones)
 it will support:
 o loading/saving compositions
 o burning dvd
 o audio composition
 o intensive usage of thunar-vfs (optionally)

To improve the next release, please fill bugs on:

http://bugs.xfce.org/
 
%prep
%setup -q -n %{name}-%{version}

%build
# Disable check for burning software, only used at runtime
export cdrdao_found=yes
export cdrecord_found=yes
export mkisofs_found=yes
export readcd_found=yes
%configure2_5x  
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
convert icons/24x24/stock_xfburn-burn-cd.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert icons/24x24/stock_xfburn-burn-cd.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert icons/24x24/stock_xfburn-burn-cd.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname}

# Menu
(cd $RPM_BUILD_ROOT
cat > .%{_menudir}/%name <<EOF
?package(%name):\
command="%{_bindir}/%{name}"\
icon="%{iconname}"\
title="Xfburn"\
longtitle="A simple CD burning tool"\
needs="x11"\
section="System/Archiving/Cd Burning" \
xdg="true"
EOF
)

desktop-file-install --vendor="" \
--add-category="X-MandrivaLinux-System-Archiving-CDBurning" \
--add-only-show-in="XFCE" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/* 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor 

%files  -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%{_bindir}/%{name} 
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*.ui
%{_menudir}/%{name}
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_iconsdir}/hicolor/24x24/stock/navigation/*xfburn*


