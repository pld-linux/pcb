Summary:	PCB design tool
Summary(pl):	PCB - narzêdzie do projektowania
Name:		pcb
Version:	1.6.3
Release:	4
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.uni-ulm.de/pub/pcb/mirror/%{name}-%{version}.tgz
Patch0:		%{name}-info.patch
BuildRequires:	XFree86-devel
BuildRequires:	tetex-latex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Pcb is a handy tool for the X Window System build to design printed
circuit boards.

%description -l pl
Pcb jest podrêcznym narzêdziem pod X Window System do projektowania
p³ytek.

%prep
%setup -q
%patch0 -p1

%build
xmkmf -a
%{__make} -i \
	CC=%{__cc} \
	CDEBUGFLAGS="%{rpmcflags}"
%{__make} -C doc pcb.man
%{__make} -C src Pcb.ad

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__make} -C doc install.man \
	DESTDIR=$RPM_BUILD_ROOT

install doc/pcb.info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf README_FILES/* docs/refcard.ps

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README_FILES/* docs/*gz example
%attr(755,root,root) %{_bindir}/pcb
%{_libdir}/X11/app-defaults/Pcb
%{_libdir}/X11/pcb
%{_mandir}/man1/*
%{_infodir}/pcb.info*
