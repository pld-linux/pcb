Summary: PCB design tool
Name: pcb
Version: 1.6.3
Release: 2
Group: X11/Applications
Copyright: GPL
Source: ftp://ftp.uni-ulm.de/pub/pcb/mirror/pcb-1.6.3.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pcb is a handy tool for the X Window System build to design 
printed circuit boards. 

%prep
%setup -q

%build
xmkmf -a
(cd doc; make)
(cd src; make Pcb.ad)
make -i

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make install.man DESTDIR=$RPM_BUILD_ROOT
make install.info DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README_FILES/* doc doc.ps example $RPM_BUILD_ROOT%{_infodir}/pcb.info
/usr/X11R6/bin/pcb
/usr/X11R6/lib/X11/app-defaults/Pcb
/usr/X11R6/lib/X11/pcb
/usr/X11R6/man/man1/pcb.1x
