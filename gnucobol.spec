Summary:	GnuCOBOL translator/compiler
Summary(pl.UTF-8):	Translator/kompilator GnuCOBOL
Name:		gnucobol
Version:	3.1
Release:	1
License:	LGPL v3+ (library), GPL v3+ (compiler)
Group:		Development/Languages
Source0:	http://ftp.gnu.org/gnu/gnucobol/%{name}-%{version}.tar.xz
# Source0-md5:	0fadb83569c4a73c2d4cdd084289c1ba
Patch0:		%{name}-info.patch
URL:		https://gnucobol.sourceforge.io/
BuildRequires:	db-devel >= 4.1
BuildRequires:	gmp-devel >= 4.1.2
BuildRequires:	json-c-devel >= 0.12
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-devel = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuCOBOL is a free (like both in "free speech" and in "free beer")
COBOL compiler, formerly known as OpenCOBOL. It implements a
substantial part of the COBOL 85, COBOL 2002 and COBOL 2014 standards,
as well as many extensions included in other COBOL compilers.

GnuCOBOL translates COBOL into C and compiles the translated code
using the native C compiler on various platforms, including
Unix/Linux, Mac OS X, and Microsoft Windows.

%description -l pl.UTF-8
GnuCOBOL to wolnodostępny (zarówno wolny, jak i darmowy) kompilator
języka COBOL, wcześniej znany jako OpenCOBOL. Implementuje znaczącą
część standardów COBOL 85, COBOL 2002 i COBOL 2014, a także wiele
rozszerzeń włącznych do innych kompilatorów języka.

GnuCOBOL tłumaczy COBOL do języka C i kompiluje przetłumaczony kod
przy użyciu natywnego kompilatora C na różnych platformach, w tym
Unix/Linux, Mac OS X i Microsoft Windows.

%package libs
Summary:	GnuCOBOL runtime library
Summary(pl.UTF-8):	Biblioteka uruchomieniowa GnuCOBOL-a
License:	LGPL v3+
Group:		Libraries
Requires:	gmp >= 4.1.2
Requires:	ncurses >= 5.2

%description libs
GnuCOBOL runtime library.

%description libs -l pl.UTF-8
Biblioteka uruchomieniowa GnuCOBOL-a.

%package devel
Summary:	Header files for GnuCOBOL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GnuCOBOL-a
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GnuCOBOL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GnuCOBOL-a.

%package static
Summary:	GnuCOBOL static library
Summary(pl.UTF-8):	Biblioteka statyczna GnuCOBOL-a
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GnuCOBOL static library.

%description static -l pl.UTF-8
Biblioteka statyczna GnuCOBOL-a.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-curses=ncurses \
	--with-db \
	--with-json=json-c \
	--with-math=gmp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_libdir}/gnucobol/*.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/cobc
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info*
%{_mandir}/man1/cobc.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cobcrun
%attr(755,root,root) %{_libdir}/libcob.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcob.so.4
%dir %{_libdir}/gnucobol
%attr(755,root,root) %{_libdir}/gnucobol/CBL_OC_DUMP.so
%{_mandir}/man1/cobcrun.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cob-config
%attr(755,root,root) %{_libdir}/libcob.so
%{_libdir}/libcob.la
%{_includedir}/libcob.h
%{_includedir}/libcob
%{_mandir}/man1/cob-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcob.a
