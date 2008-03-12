Summary:	An editor for the GConf configuration system
Summary(pl.UTF-8):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.22.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gconf-editor/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	7ca99aec214dd855b5de7dacc8937055
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libgnomeui-devel >= 2.22.01
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	libgnomeui >= 2.22.01
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An editor for the GConf configuration system.

%description -l pl.UTF-8
Edytor do systemu konfiguracji GConf.

%prep
%setup -q

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv po/sr@{Latn,latin}.po

%build
%{__intltoolize}
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install gconf-editor.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gconf-editor.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gconf-editor
%{_desktopdir}/gconf-editor.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/gconf-editor.1*
%{_pixmapsdir}/gconf-editor
%{_sysconfdir}/gconf/schemas/gconf-editor.schemas
