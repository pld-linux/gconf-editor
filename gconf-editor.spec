%define name gconf
%define version editor
%define release 1mdk

Summary: An editor for the GConf configuration system
Name: gconf-editor
Version: 0.1
Release: 1mdk
Source0: ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/gNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libgtk+2.0_0-devel
BuildRequires: libGConf2-devel

%description
gconf-edit is an editor for the GConf configuration system

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Apr 30 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1-1mdk
- Initial Mandrake package (GNOME 2)


# end of file
