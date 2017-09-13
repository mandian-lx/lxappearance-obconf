Summary:	Plugin to configure OpenBox inside LXAppearance
Name:		lxappearance-obconf
Epoch:		1
Version:	0.2.3
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+
Url:		https://lxde.org/
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	openbox
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(lxappearance)
BuildRequires:	pkgconfig(obrender-3.5)
BuildRequires:	pkgconfig(obt-3.5)
BuildRequires:	pkgconfig(sm)

Requires:	lxappearance
Requires:	openbox

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README NEWS TODO
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

