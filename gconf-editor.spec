Summary:	An editor for the GConf configuration system
Summary(pl.UTF-8):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.20.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gconf-editor/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	b686677878b5754ffa8d0a2cc1129988
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.10.1
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	libgnomeui >= 2.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An editor for the GConf configuration system.

%description -l pl.UTF-8
Edytor do systemu konfiguracji GConf.

%prep
%setup -q

%build
mkdir m4
%{__intltoolize}
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*
%{_pixmapsdir}/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/gconf-editor/gconf-editor-C.omf
%lang(de) %{_omf_dest_dir}/gconf-editor/gconf-editor-de.omf
%lang(es) %{_omf_dest_dir}/gconf-editor/gconf-editor-es.omf
%lang(fr) %{_omf_dest_dir}/gconf-editor/gconf-editor-fr.omf
%lang(it) %{_omf_dest_dir}/gconf-editor/gconf-editor-it.omf
%lang(oc) %{_omf_dest_dir}/gconf-editor/gconf-editor-oc.omf
%lang(sv) %{_omf_dest_dir}/gconf-editor/gconf-editor-sv.omf
%lang(uk) %{_omf_dest_dir}/gconf-editor/gconf-editor-uk.omf
%{_sysconfdir}/gconf/schemas/gconf-editor.schemas
