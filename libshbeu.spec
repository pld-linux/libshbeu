Summary:	Library for controlling SH-Mobile BEU (Blend Engine Unit)
Summary(pl.UTF-8):	Biblioteka do sterowania układem SH-Mobile BEU (Blend Engine Unit)
Name:		libshbeu
Version:	1.1.0
Release:	1
License:	LGPL v2+
Group:		Libraries
# trailing #/%{name}-%{version}.tar.gz is a hack for df
#Source0Download: https://oss.renesas.com/modules/document/?libshbeu
Source0:	https://oss.renesas.com/modules/document/gate.php/?way=attach&refer=libshbeu&openfile=%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0-md5:	1accc7c988673863727ce21dad62def3
Patch0:		%{name}-link.patch
URL:		https://oss.renesas.com/modules/document/?libshbeu
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libuiomux-devel >= 1.5.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
Requires:	libuiomux >= 1.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libshbeu is a library for controlling SH-Mobile BEU (Blend Engine
Unit).

%description -l pl.UTF-8
Biblioteka do sterowania układem SH-Mobile BEU (Blend Engine Unit).

%package devel
Summary:	Header files for libshbeu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libshbeu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuiomux-devel >= 1.5.0

%description devel
Header files for libshbeu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libshbeu.

%package static
Summary:	Static libshbeu library
Summary(pl.UTF-8):	Statyczna biblioteka libshbeu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libshbeu library.

%description static -l pl.UTF-8
Statyczna biblioteka libshbeu.

%package apidocs
Summary:	libshbeu API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libshbeu
Group:		Documentation

%description apidocs
API and internal documentation for libshbeu library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libshbeu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	ncurses_lib="-lncurses -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkgconfig (with link patch)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libshbeu.la
# HTML packaged in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libshbeu

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/shbeu-display
%attr(755,root,root) %{_libdir}/libshbeu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshbeu.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshbeu.so
%{_includedir}/shbeu
%{_pkgconfigdir}/shbeu.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libshbeu.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libshbeu/html/*
