%define name		ozymandns
%define version		0.1
%define release		%mkrel 4

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

