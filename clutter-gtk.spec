Summary:	Library integrating clutter with GTK+
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GTK+
Name:		clutter-gtk
Version:	0.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter-gtk/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	c3daf6a39749a10d4f5c9fbd3ea1da72
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	clutter-devel >= 0.3.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with GTK+.

%description -l pl.UTF-8
Biblioteka integrująca clutter z GTK+.

%package devel
Summary:	Header files for clutter-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 0.3.0
Requires:	gtk+2-devel >= 2:2.10.0

%description devel
Header files for clutter-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-gtk.

%package static
Summary:	Static clutter-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-gtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-gtk library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-gtk.

%package apidocs
Summary:	clutter-gtk API documentation
Summary(pl.UTF-8):	Dokumentacja API clutter-gtk
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter-gtk API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API clutter-gtk.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libclutter-gtk-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gtk-*.so
%{_libdir}/libclutter-gtk-*.la
%{_includedir}/clutter-*/%{name}
%{_pkgconfigdir}/clutter-gtk-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gtk-*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
