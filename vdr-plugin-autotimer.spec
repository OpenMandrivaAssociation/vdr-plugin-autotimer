%define plugin	autotimer

Summary:	VDR plugin: Autotimer
Name:		vdr-plugin-%plugin
Version:	2.0.0
Release:	1
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-autotimer/
Source:		http://phivdr.dyndns.org/vdr/vdr-autotimer/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Simple autotimer plugin for vdr. This plugin creates automatically
timers for matching EPG events.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY *.example
