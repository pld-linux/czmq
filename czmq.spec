Summary:	High-level C binding for 0MQ
Summary(pl.UTF-8):	Wysokopoziomowe wiązania C dla 0MQ
Name:		czmq
Version:	3.0.2
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
# Source0-md5:	7697688bf65a35bc33ae2db51ebb0e3b
Patch0:		no-Werror.patch
Patch1:		%{name}-link.patch
URL:		http://zeromq.org/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libsodium-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	xmlto
BuildRequires:	zeromq-devel >= 4
Requires:	zeromq >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High-level C binding for 0MQ.

%description -l pl.UTF-8
Wysokopoziomowe wiązania C dla 0MQ.

%package devel
Summary:	Header files for CZMQ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CZMQ
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zeromq-devel >= 4

%description devel
Header files for CZMQ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CZMQ.

%package static
Summary:	Static CZMQ library
Summary(pl.UTF-8):	Statyczna biblioteka CZMQ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CZMQ library.

%description static -l pl.UTF-8
Statyczna biblioteka CZMQ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
# use include subdir - file names could be too common (zfile.h etc.)
%configure \
	--disable-silent-rules \
	--includedir=%{_includedir}/czmq
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libczmq.la

# too common name
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{makecert,czmq_makecert}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/{makecert,czmq_makecert}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/czmq_makecert
%attr(755,root,root) %{_libdir}/libczmq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libczmq.so.3
%{_mandir}/man1/czmq_makecert.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libczmq.so
%{_includedir}/czmq
%{_pkgconfigdir}/libczmq.pc
%{_mandir}/man3/zactor.3*
%{_mandir}/man3/zarmour.3*
%{_mandir}/man3/zauth.3*
%{_mandir}/man3/zauth_v2.3*
%{_mandir}/man3/zbeacon.3*
%{_mandir}/man3/zbeacon_v2.3*
%{_mandir}/man3/zcert.3*
%{_mandir}/man3/zcertstore.3*
%{_mandir}/man3/zchunk.3*
%{_mandir}/man3/zclock.3*
%{_mandir}/man3/zconfig.3*
%{_mandir}/man3/zctx.3*
%{_mandir}/man3/zdigest.3*
%{_mandir}/man3/zdir.3*
%{_mandir}/man3/zdir_patch.3*
%{_mandir}/man3/zfile.3*
%{_mandir}/man3/zframe.3*
%{_mandir}/man3/zgossip.3*
%{_mandir}/man3/zhash.3*
%{_mandir}/man3/zhashx.3*
%{_mandir}/man3/ziflist.3*
%{_mandir}/man3/zlist.3*
%{_mandir}/man3/zlistx.3*
%{_mandir}/man3/zloop.3*
%{_mandir}/man3/zmonitor.3*
%{_mandir}/man3/zmonitor_v2.3*
%{_mandir}/man3/zmsg.3*
%{_mandir}/man3/zmutex.3*
%{_mandir}/man3/zpoller.3*
%{_mandir}/man3/zproxy.3*
%{_mandir}/man3/zproxy_v2.3*
%{_mandir}/man3/zrex.3*
%{_mandir}/man3/zsock.3*
%{_mandir}/man3/zsock_option.3*
%{_mandir}/man3/zsocket.3*
%{_mandir}/man3/zsockopt.3*
%{_mandir}/man3/zstr.3*
%{_mandir}/man3/zsys.3*
%{_mandir}/man3/zthread.3*
%{_mandir}/man3/zuuid.3*
%{_mandir}/man7/czmq.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libczmq.a
