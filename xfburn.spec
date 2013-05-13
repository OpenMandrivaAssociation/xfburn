%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A simple CD burning tool for the Xfce Desktop Environment
Name:		xfburn
Version:	0.4.3
Release:	8
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org/projects/xfburn/
Source0:	http://archive.xfce.org/src/apps/xfburn/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfburn-0.4.3-gobject.patch
Patch2:		xfburn-0.4.3-desktop.patch
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.4.2
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(libburn-1)
BuildRequires:	pkgconfig(libisofs-1)
BuildRequires:	xfce4-dev-tools
BuildRequires:	dbus-glib-devel
BuildRequires:	gstreamer0.10-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
%if %mdkver >= 201200
BuildConflicts:	hal-devel
%else
BuildRequires:	hal-devel
%endif

%description
Xfburn is a simple CD/DVD burning tool based on libburnia 
libraries.It can blank CD-RWs, burn and create iso images, 
as well as burn personal compositions of data to either CD or DVD.

%prep
%setup -q
%patch1 -p0
%patch2 -p0

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

%files  -f %{name}.lang
%doc AUTHORS ChangeLog  TODO
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*.ui
%{_datadir}/Thunar/sendto/thunar-sendto-xfburn.desktop
%{_iconsdir}/hicolor/*
%{_mandir}/man1/*


%changelog
* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.4.3-6mdv2012.0
+ Revision: 789983
- Patch2: Fix desktop file
- Patch 1 - build with newer glib
- Rebuild

* Tue Oct 11 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-5
+ Revision: 704351
- do not build against hal for mdv2012

* Sat Sep 03 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-4
+ Revision: 698101
- rebuild for new libburn

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-3
+ Revision: 633045
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-2mdv2011.0
+ Revision: 579639
- adjust buildrequires
- rebuild for new xfce 4.7.0

* Sat Feb 13 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 505532
- update to new version 0.4.3
- use new url for Source0

* Wed Jul 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-2mdv2010.0
+ Revision: 404035
- rebuild
- update to new version 0.4.2

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-2mdv2009.1
+ Revision: 349187
- rebuild whole xfce

* Wed Feb 25 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-1mdv2009.1
+ Revision: 344764
- add missing file
- drop patch 0, merged upstream
- update to new version 0.4.1

* Mon Dec 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-2mdv2009.1
+ Revision: 317692
- Patch1: fix building with -Werror=format-security
- bs is hungry, feed it :)
- fix file list
- add buildrequires on libgstreamer0.10-plugins-base-devel
- update to new version 0.4.0

* Mon Nov 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.91-1mdv2009.1
+ Revision: 299612
- enable gstreamer support
- update to new version 0.3.91

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-2mdv2009.1
+ Revision: 294937
- rebuild for new Xfce4.6 beta1

* Thu Jul 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 236764
- update to new version 0.3.2

* Thu Jul 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 233500
- update to new version 0.3.1

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 214443
- update to new version 0.3.0

* Wed May 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4796.1mdv2009.0
+ Revision: 207176
- new svn snapshot

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4783.1mdv2009.0
+ Revision: 205833
- new svn snapshot

* Thu May 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4743.1mdv2009.0
+ Revision: 203875
- new svn snapshot

* Mon Apr 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4681.1mdv2009.0
+ Revision: 198463
- new snapshot

* Thu Apr 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4667.1mdv2009.0
+ Revision: 197196
- new svn snapshot

* Mon Apr 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4646.1mdv2009.0
+ Revision: 196250
- new svn snapshot

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4630.1mdv2009.0
+ Revision: 195669
- new xfburn svn snapshot

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-0.svn4612.1mdv2009.0
+ Revision: 195501
- update xfburn to the latest svn snapshot
- xfburn now uses libburn and libisofs libraries to handle CD/DVD burning, thus patch 0 is not needed
- adjust buildrequires
- do not package COPYING file
- provide better description
- fix URL

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-7mdv2008.1
+ Revision: 102422
- provide patch 0 (support for cdrkit)
- fix desktop entry

* Wed Jul 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-6mdv2008.0
+ Revision: 51344
- own dir
- drop X-MandrivaLinux

* Fri Jun 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-5mdv2008.0
+ Revision: 34326
- fix icon name

* Wed May 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-4mdv2008.0
+ Revision: 32896
- set requires on cdrkit and cdrkit-genisoimage
- drop old menu style
- add macros to %%post and %%postun
- spec file clean

