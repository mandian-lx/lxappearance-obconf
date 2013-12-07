Summary:        Plugin to configure OpenBox inside LXAppearance
Name:           lxappearance-obconf
Version:        0.5.1
Release:        8
Group:          Graphical desktop/Other
License:        GPLv2+
Url:            http://lxde.org/
Source0:        %{name}-%{version}.tar.gz
Patch0:		lxappearance-obconf-automake_113.patch
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:	openbox
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(lxappearance)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  pkgconfig(sm)
Requires:       lxappearance >= 0.5.1
Requires:       openbox

%description
This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%prep
%setup -qn %{name}
%apply_patches

# dirty hack for outdated/changing LINGUAS file
cd po
ls *.po > LINGUAS
sed -i 's/.po//g' LINGUAS
./autogen.sh

%build
%configure --disable-static
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
# FIXME add NEWS and TODO
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/

