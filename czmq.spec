Summary:	High-level C binding for 0MQ
Summary(pl.UTF-8):	Wysokopoziomowe wiązania C dla 0MQ
Name:		czmq
Version:	1.4.1
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
# Source0-md5:	b54bcf101e5e23285b8ff0ad80a58c41
URL:		http://zeromq.org/
BuildRequires:	zeromq-devel
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
Requires:	zeromq-devel

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

%build
# use include subdir - file names could be too common (zfile.h etc.)
%configure \
	--includedir=%{_includedir}/czmq
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libczmq.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/czmq_selftest
%attr(755,root,root) %{_libdir}/libczmq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libczmq.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libczmq.so
%{_includedir}/czmq
%{_pkgconfigdir}/libczmq.pc
%{_mandir}/man3/zbeacon.3*
%{_mandir}/man3/zclock.3*
%{_mandir}/man3/zctx.3*
%{_mandir}/man3/zfile.3*
%{_mandir}/man3/zframe.3*
%{_mandir}/man3/zhash.3*
%{_mandir}/man3/zlist.3*
%{_mandir}/man3/zloop.3*
%{_mandir}/man3/zmsg.3*
%{_mandir}/man3/zmutex.3*
%{_mandir}/man3/zsocket.3*
%{_mandir}/man3/zsockopt.3*
%{_mandir}/man3/zstr.3*
%{_mandir}/man3/zsys.3*
%{_mandir}/man3/zthread.3*
%{_mandir}/man7/czmq.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libczmq.a
