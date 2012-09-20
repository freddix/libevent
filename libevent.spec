Summary:	Event notification library
Name:		libevent
Version:	2.0.20
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/downloads/libevent/libevent/%{name}-%{version}-stable.tar.gz
# Source0-md5:	94270cdee32c0cd0aa9f4ee6ede27e8e
Patch0:		%{name}-link.patch
URL:		http://www.monkey.org/~provos/libevent/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. It is meant to replace the asynchronous event loop
found in event-driven network servers.

%package devel
Summary:	Header files for libevent library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libevent library.

%prep
%setup -qn %{name}-%{version}-stable
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libevent*.so.?
%attr(755,root,root) %{_libdir}/libevent*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/event_rpcgen.py
%attr(755,root,root) %{_libdir}/libevent*.so
%{_libdir}/libevent*.la
%{_libdir}/libevent_extra.la
%{_includedir}/*.h
%{_includedir}/event2
%{_pkgconfigdir}/*.pc

