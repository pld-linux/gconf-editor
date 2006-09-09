Summary:	An editor for the GConf configuration system
Summary(pl):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.16.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gconf-editor/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	e52b3177ef6ebd1fcf2c84acbe90a663
Patch0:		%{name}-desktop.patch
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2:2.10.1
Requires:	libgnomeui >= 2.14.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An editor for the GConf configuration system.

%description -l pl
Edytor do systemu konfiguracji GConf.

%prep
%setup -q
%patch0 -p1

%build
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ug

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
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/*
%{_pixmapsdir}/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/*-C.omf
%{_sysconfdir}/gconf/schemas/gconf-editor.schemas
