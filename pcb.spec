Summary:	PCB design tool
Name:		pcb
Version:	1.6.3
Release:	3
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.uni-ulm.de/pub/pcb/mirror/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_infodir	/usr/share/info

%description
Pcb is a handy tool for the X Window System build to design printed
circuit boards.

%prep
%setup -q

%build
xmkmf -a
(cd doc; make pcb.man)
(cd doc; make pcb.ps)
(cd src; make Pcb.ad)
%{__make} -i

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
(cd doc; %{__make} install.man DESTDIR=$RPM_BUILD_ROOT)
(cd doc; cp pcb.info $RPM_BUILD_ROOT/%{_infodir})

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README_FILES/* doc doc.ps example $RPM_BUILD_ROOT%{_infodir}/pcb.info.gz
%attr(755,root,root) %{_bindir}/pcb
%{_libdir}/X11/app-defaults/Pcb
%{_libdir}/X11/pcb
%{_mandir}/man1/*
