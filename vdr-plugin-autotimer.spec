
%define plugin	autotimer
%define name	vdr-plugin-%plugin
%define version	0.2.0
%define rel	11

Summary:	VDR plugin: Autotimer
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-autotimer/
Source:		http://phivdr.dyndns.org/vdr/vdr-autotimer/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Simple autotimer plugin for vdr. This plugin creates automatically
timers for matching EPG events.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

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




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-11mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-10mdv2009.1
+ Revision: 359285
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.0-9mdv2009.0
+ Revision: 197900
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.0-8mdv2009.0
+ Revision: 197631
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.0-7mdv2008.1
+ Revision: 145028
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.0-6mdv2008.1
+ Revision: 144979
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.2.0-5mdv2008.1
+ Revision: 103060
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.2.0-4mdv2008.0
+ Revision: 49969
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.0-3mdv2008.0
+ Revision: 42056
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.2.0-2mdv2008.0
+ Revision: 22706
- rebuild for new vdr

* Sat Apr 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 16567
- update URL
- 0.2.0


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-7mdv2007.0
+ Revision: 90891
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-6mdv2007.1
+ Revision: 73951
- rebuild for new vdr
- Import vdr-plugin-autotimer

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2007.0
- rebuild for new vdr

* Thu Jun 22 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2007.0
- initial Mandriva release

