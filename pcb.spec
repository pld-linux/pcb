Summary:	Printed Circuit Board design tool
Summary(pl):	PCB - narzêdzie do projektowania p³ytek drukowanych
Name:		pcb
%define	_snap	20040530
Version:	2.0
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/pcb/%{name}-%{_snap}.tar.gz
# Source0-md5:	4a2463340d4eaf2045ef388986ad7e7f
URL:		http://pcb.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tgif
BuildRequires:	tk
#BuildRequires:	Xaw3d-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Pcb is a handy tool for the X Window System build to design printed
circuit boards.

%description -l pl
Pcb jest podrêcznym narzêdziem pod X Window System do projektowania
p³ytek drukowanych.

%prep
%setup -q -n %{name}-%{_snap}

%build
%configure
#	--with-xaw=Xaw3d
	# brakes menus

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}
install -d $RPM_BUILD_ROOT%{_appdefsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install $RPM_BUILD_ROOT%{_datadir}/pcb/Pcb $RPM_BUILD_ROOT%{_appdefsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README_FILES/{CHANGES,INSTALL,MAILING,README,Tools,Whats_new_in_2.0} AUTHORS ChangeLog NEWS
%doc $RPM_BUILD_ROOT%{_datadir}/pcb/examples
%doc $RPM_BUILD_ROOT%{_datadir}/pcb/pcb.html
%doc $RPM_BUILD_ROOT%{_datadir}/pcb/refcard.pdf
%doc $RPM_BUILD_ROOT%{_datadir}/pcb/tutorial

%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_appdefsdir}/Pcb

%attr(755,root,root) %{_datadir}/pcb/*.sh
%attr(755,root,root) %{_datadir}/pcb/qfp-ui
%attr(644,root,root) %{_datadir}/pcb/default_font
%attr(644,root,root) %{_datadir}/pcb/pcblib
%attr(644,root,root) %{_datadir}/pcb/pcblib.contents
%attr(644,root,root) %{_datadir}/pcb/pcb-menu.res
%attr(644,root,root) %{_datadir}/pcb/qfp.dat
%attr(755,root,root) %{_datadir}/pcb/m4
%attr(755,root,root) %{_datadir}/pcb/tools
%attr(755,root,root) %{_datadir}/pcb/newlib

%attr(644,root,root) %{_infodir}/pcb.info*
