Summary:	An editor for the GConf configuration system
Summary(pl):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications
# Source0-md5:	3a267c5724d086d7d5f47691980faff1
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.5/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+2-devel >= 2.0.1
BuildRequires:	GConf2-devel >= 1.2.1-10
BuildRequires:	Xft-devel >= 2.0-6

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
%{_datadir}/applications/*
%{_pixmapsdir}/*
