Name:		libosip2
Version:	5.3.0
Release:	1%{?dist}_netxms
Summary:	This is the oSIP library.

License:	BSD
URL:		https://savannah.nongnu.org/projects/exosip
Source0:	https://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
This is the oSIP library. It has been designed to provide the Internet Community
a simple way to support the Session Initiation Protocol. SIP is described in
the RFC3261 which is available at http://www.ietf.org/rfc/rfc3261.txt.
This distribution is built specifically for NetXMS packaging.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la

%files
%{_libdir}/libosip2.so.*
%{_libdir}/libosipparser2.so.*

#%doc COPYING README VERSION

%files devel
%{_includedir}/osip2/*
%{_includedir}/osipparser2/*
%{_libdir}/pkgconfig/libosip2.pc
%{_libdir}/libosip2.a
%{_libdir}/libosip2.so
%{_libdir}/libosipparser2.a
%{_libdir}/libosipparser2.so
%{_mandir}/man1/osip.1*

%ldconfig_scriptlets

%changelog
* Wed Sep 28 2022 Alex Kirhenshtein <alk@netxms.org>
- Upstream updated to 5.3.0
