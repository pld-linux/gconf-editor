Summary:	An editor for the GConf configuration system
Summary(pl):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.7.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	1d009a010a5d26f27950ec7ac8adbd10
Patch0:		%{name}-locale-names.patch
BuildRequires:	GConf2-devel >= 2.7.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	libgnomeui-devel >= 2.7.1
BuildRequires:	libtool
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An editor for the GConf configuration system.

%description -l pl
Edytor do systemu konfiguracji GConf.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
gnome-doc-common
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
