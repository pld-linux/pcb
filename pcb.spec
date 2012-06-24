Summary:	Printed Circuit Board design tool
Summary(pl):	PCB - narz�dzie do projektowania p�ytek drukowanych
Name:		pcb
Version:	20050315
Release:	0.1
License:	GPL
Group:		X11/Applications
# devel snaps: http://dl.sourceforge.net/pcb/
Source0:	http://dl.sourceforge.net/pcb/%{name}-%{version}.tar.gz
# Source0-md5:	853a0709003c2c8967c756b6068476f6
#Source0:	ftp://ftp.uni-ulm.de/pub/pcb/mirror/%{name}-%{version}.tar.gz
URL:		http://pcb.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	gtk2+-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Pcb is a handy tool for the X Window System build to design printed
circuit boards.

%description -l pl
Pcb jest podr�cznym narz�dziem pod X Window System do projektowania
p�ytek drukowanych.

%prep
%setup -q

%build
%configure
%{__make} -i \
	CC=%{__cc} \
	CDEBUGFLAGS="%{rpmcflags}" \
	PCBLIBDIR=%{_datadir}/pcb
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PCBLIBDIR=%{_datadir}/pcb \
	BINDIR=%{_bindir}

install doc/pcb.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README_FILES/* example
%attr(755,root,root) %{_bindir}/pcb
%attr(755,root,root) %{_bindir}/pcb-bin
#%{_appdefsdir}/Pcb
%{_datadir}/pcb
%{_mandir}/man1/*
%{_infodir}/pcb.info*
