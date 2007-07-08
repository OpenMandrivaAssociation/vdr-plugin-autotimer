
%define plugin	autotimer
%define name	vdr-plugin-%plugin
%define version	0.2.0
%define rel	4

Summary:	VDR plugin: Autotimer
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-autotimer/
Source:		http://phivdr.dyndns.org/vdr/vdr-autotimer/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Simple autotimer plugin for vdr. This plugin creates automatically
timers for matching EPG events.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY *.example


