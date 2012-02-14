Summary:        Plugin to configure OpenBox inside LXAppearance
Name:           lxappearance-obconf
Version:        0.5.1
Release:        3
Group:          Graphical desktop/Other
License:        GPLv2+
URL:            http://lxde.org/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  pkgconfig(lxappearance)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
Requires:       lxappearance >= 0.5.1
Requires:       openbox

%description
This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%prep
%setup -qn %{name}
# dirty hack for outdated/changing LINGUAS file
cd po
ls *.po > LINGUAS
sed -i 's/.po//g' LINGUAS

%build
./autogen.sh
%configure \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm %{buildroot}%{_libdir}/lxappearance/plugins/obconf.la
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/

