Summary:	An editor for the GConf configuration system
Summary(pl):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	69b4b380b198997d6e9a456645e9015f
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	gtk+2-devel >= 2.3.0-1.20031110.1
BuildRequires:	xft-devel >= 2.0-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An editor for the GConf configuration system.

%description -l pl
Edytor do systemu konfiguracji GConf.

%prep
%setup -q

%build
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
