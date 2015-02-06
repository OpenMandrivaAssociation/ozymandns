%define name		ozymandns
%define version		0.1
%define release		4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DNS Tunnel
License:	Distributable
Group:		Networking/Other
URL:		http://www.doxpara.com/
Source:     http://www.doxpara.com/%{name}_src_%{version}.tgz
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This is a DNS Tunnel client and server.

%prep
%setup -q -c

%build
gcc %{optflags} glance.c -o glance

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 glance %{buildroot}%{_bindir}
install -m 755 aska.pl %{buildroot}%{_bindir}
install -m 755 geta.pl %{buildroot}%{_bindir}
install -m 755 nomde.pl %{buildroot}%{_bindir}
install -m 755 droute.pl %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-3mdv2010.0
+ Revision: 430226
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2mdv2009.0
+ Revision: 268354
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2009.0
+ Revision: 213665
- import ozymandns


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2009.0
- first mdv release
