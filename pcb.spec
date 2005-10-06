Summary:	Printed Circuit Board design tool
Summary(pl):	PCB - narzêdzie do projektowania p³ytek drukowanych
Name:		pcb
Version:	20050609
Release:	0.1
License:	GPL
Group:		X11/Applications
# devel snaps: http://dl.sourceforge.net/pcb/
Source0:	http://dl.sourceforge.net/pcb/%{name}-%{version}.tar.gz
# Source0-md5:	a09473705c80eaf4f796617263d9f8fe
#Source0:	%{name}-gtk-%{version}.tar.bz2
Patch0:		%{name}-menu.patch
URL:		http://pcb.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Pcb is a handy tool for the X Window System build to design printed
circuit boards.

%description -l pl
Pcb jest podrêcznym narzêdziem pod X Window System do projektowania
p³ytek drukowanych.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
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
%attr(755,root,root) %{_bindir}/*
##%attr(755,root,root) %{_bindir}/pcb
##%attr(755,root,root) %{_bindir}/pcb-bin
#%{_appdefsdir}/Pcb
%{_datadir}/pcb
%{_mandir}/man1/*
%{_infodir}/pcb.info*
