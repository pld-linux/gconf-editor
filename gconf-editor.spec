Summary:	An editor for the GConf configuration system
Summary(pl):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.6.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	456d5dbddefffe7b49f18688aa9c1975
Patch0:		%{name}-locale-names.patch
BuildRequires:	GConf2-devel >= 2.5.90
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
