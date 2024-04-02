#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	systemd	# systemd

Summary:	High-level C binding for 0MQ
Summary(pl.UTF-8):	Wysokopoziomowe wiązania C dla 0MQ
Name:		czmq
Version:	4.2.0
Release:	6
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/zeromq/czmq/releases
Source0:	https://github.com/zeromq/czmq/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7e09997db6ac3b25e8ed104053040722
Patch1:		%{name}-link.patch
URL:		http://zeromq.org/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.28.0
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	lz4-devel
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_systemd:BuildRequires:	systemd-devel >= 1:200}
BuildRequires:	xmlto
BuildRequires:	zeromq-devel >= 4
Requires:	curl-libs >= 7.28.0
%{?with_systemd:Requires:	systemd-libs >= 1:200}
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
Requires:	curl-devel >= 7.28.0
Requires:	libmicrohttpd-devel
Requires:	libuuid-devel
Requires:	lz4-devel
%{?with_systemd:Requires:	systemd-devel >= 1:200}
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

%package -n python-czmq
Summary:	Python 2 bindings for CZMQ
Summary(pl.UTF-8):	Wiązania Pythona 2 do CZMQ
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-czmq
Python 2 bindings for CZMQ - the high level C binding for 0MQ.

%description -n python-czmq -l pl.UTF-8
Wiązania Pythona 2 do CZMQ - wysokopoziomowego wiązania C do 0MQ.

%package -n python3-czmq
Summary:	Python 3 bindings for CZMQ
Summary(pl.UTF-8):	Wiązania Pythona 3 do CZMQ
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-czmq
Python 3 bindings for CZMQ - the high level C binding for 0MQ.

%description -n python3-czmq -l pl.UTF-8
Wiązania Pythona 3 do CZMQ - wysokopoziomowego wiązania C do 0MQ.

%prep
%setup -q
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
# use include subdir - file names could be too common (zfile.h etc.)
%configure \
	--enable-bindings-python \
	--enable-drafts \
	--disable-silent-rules \
	--includedir=%{_includedir}/czmq \
	%{!?with_systemd:--with-libsystemd=no}
%{__make}

cd bindings/python

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd bindings/python

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libczmq.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/zmakecert
%attr(755,root,root) %{_libdir}/libczmq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libczmq.so.4
%{_mandir}/man1/zmakecert.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libczmq.so
%{_includedir}/czmq
%{_pkgconfigdir}/libczmq.pc
%dir %{_datadir}/zproject
%{_datadir}/zproject/czmq
%{_mandir}/man3/zactor.3*
%{_mandir}/man3/zargs.3*
%{_mandir}/man3/zarmour.3*
%{_mandir}/man3/zauth.3*
%{_mandir}/man3/zbeacon.3*
%{_mandir}/man3/zcert.3*
%{_mandir}/man3/zcertstore.3*
%{_mandir}/man3/zchunk.3*
%{_mandir}/man3/zclock.3*
%{_mandir}/man3/zconfig.3*
%{_mandir}/man3/zdigest.3*
%{_mandir}/man3/zdir.3*
%{_mandir}/man3/zdir_patch.3*
%{_mandir}/man3/zfile.3*
%{_mandir}/man3/zframe.3*
%{_mandir}/man3/zgossip.3*
%{_mandir}/man3/zhash.3*
%{_mandir}/man3/zhashx.3*
%{_mandir}/man3/zhttp_client.3*
%{_mandir}/man3/zhttp_request.3*
%{_mandir}/man3/zhttp_response.3*
%{_mandir}/man3/zhttp_server.3*
%{_mandir}/man3/zhttp_server_options.3*
%{_mandir}/man3/ziflist.3*
%{_mandir}/man3/zlist.3*
%{_mandir}/man3/zlistx.3*
%{_mandir}/man3/zloop.3*
%{_mandir}/man3/zmonitor.3*
%{_mandir}/man3/zmsg.3*
%{_mandir}/man3/zpoller.3*
%{_mandir}/man3/zproc.3*
%{_mandir}/man3/zproxy.3*
%{_mandir}/man3/zrex.3*
%{_mandir}/man3/zsock.3*
%{_mandir}/man3/zstr.3*
%{_mandir}/man3/zsys.3*
%{_mandir}/man3/ztimerset.3*
%{_mandir}/man3/ztrie.3*
%{_mandir}/man3/zuuid.3*
%{_mandir}/man7/czmq.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libczmq.a

%if %{with python2}
%files -n python-czmq
%defattr(644,root,root,755)
%{py_sitescriptdir}/czmq
%{py_sitescriptdir}/czmq-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-czmq
%defattr(644,root,root,755)
%{py3_sitescriptdir}/czmq
%{py3_sitescriptdir}/czmq-%{version}-py*.egg-info
%endif
