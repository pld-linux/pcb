Summary:	Printed Circuit Board design tool
Summary(pl):	PCB - narzêdzie do projektowania p³ytek drukowanych
Name:		pcb
Version:	1.6.3
Release:	6
License:	GPL
Group:		X11/Applications
# devel snaps: http://dl.sourceforge.net/pcb/
Source0:	ftp://ftp.uni-ulm.de/pub/pcb/mirror/%{name}-%{version}.tgz
# Source0-md5:	2649927fd49b89d71a524082b633849e
Patch0:		%{name}-info.patch
# http://bach.ece.jhu.edu/~haceaton/pcb/glibc.patch
Patch1:		%{name}-glibc.patch
URL:		http://pcb.sourceforge.net/
BuildRequires:	XFree86-devel
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
Pcb jest podrêcznym narzêdziem pod X Window System do projektowania
p³ytek drukowanych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__perl} -pi -e 's@\\/usr\\/X11R6\\/lib\\/X11\\/pcb@%(echo %{_datadir}/pcb | sed -e 's@/@\\\\/@g')@' src/sed.script

%build
xmkmf -a
%{__make} -i \
	CC=%{__cc} \
	CDEBUGFLAGS="%{rpmcflags}" \
	PCBLIBDIR=%{_datadir}/pcb
	
%{__make} -C doc pcb.man pcb.info
%{__make} -C src Pcb.ad

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PCBLIBDIR=%{_datadir}/pcb \
	BINDIR=%{_bindir}

%{__make} -C doc install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1

install doc/pcb.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README_FILES/* doc.ps/refcard.ps* example
%attr(755,root,root) %{_bindir}/pcb
%{_appdefsdir}/Pcb
%{_datadir}/pcb
%{_mandir}/man1/*
%{_infodir}/pcb.info*
