Summary:        Plugin to configure OpenBox inside LXAppearance
Name:           lxappearance-obconf
Version:        0.5.1
Release:        4

Group:          Graphical desktop/Other
License:        GPLv2+
URL:            http://lxde.org/
Source0:        %{name}-%{version}.tar.gz
Patch0:		lxappearance-obconf-automake_113.patch

BuildRequires:  gtk+2-devel

BuildRequires:  openbox-devel 
BuildRequires:  lxappearance-devel
BuildRequires:  pkgconfig(sm)
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:	openbox
BuildRequires:	automake
Requires:       lxappearance >= 0.5.1
Requires:       openbox

%description
This plugin adds an addtional tab called "Window Border" to LXAppearance. 
It is only visible when the plugin is installed and Openbox is in use.

%prep
%setup -q -n %{name}
%patch0 -p1

# dirty hack for outdated/changing LINGUAS file
cd po
ls *.po > LINGUAS
sed -i 's/.po//g' LINGUAS

%build
./autogen.sh
%configure --disable-static
%make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/lxappearance/plugins/obconf.la
%find_lang %{name}

%files -f %{name}.lang
# FIXME add NEWS and TODO
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins/obconf.so
%{_datadir}/lxappearance/obconf/


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.1-2mdv2011.0
+ Revision: 692998
- update to 0.5.1

* Wed Jun 01 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.0-9
+ Revision: 682398
- update for new lxappearance

* Sun Apr 17 2011 Frank Kober <emuse@mandriva.org> 0.5.0-4
+ Revision: 653962
- bump release
- fix BR naming
- rebuild

* Thu Feb 17 2011 Александр Казанцев <kazancas@mandriva.org> 0.5.0-2
+ Revision: 638309
+ rebuild (emptylog)

* Fri Dec 31 2010 Александр Казанцев <kazancas@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 626795
- initial release
- import lxappearance-obconf


*Sat Nov 6 2010 Alexander Kazancev <kazancas@mandriva.ru> - 0.0.1
- initial release
