Summary:	An editor for the GConf configuration system
Summary(pl):	Edytor do systemu konfiguracji GConf
Name:		gconf-editor
Version:	2.4.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	7ebc352062fc8b6d3c09a69ad6e963a7
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	gtk+2-devel >= 2.2.4
BuildRequires:	xft-devel >= 2.0-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An editor for the GConf configuration system.

%description -l pl
Edytor do systemu konfiguracji GConf.

%prep
%setup -q

%build
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
