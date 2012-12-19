Summary:	Library integrating clutter with GTK+
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GTK+
Name:		clutter-gtk
Version:	1.4.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://download.gnome.org/sources/clutter-gtk/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	842601b584daf4447a46799a4ba88df6
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 0.9.12
BuildRequires:	gtk+3-devel >= 3.2.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	clutter >= 1.10.0
Requires:	gtk+3 >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with GTK+.

%description -l pl.UTF-8
Biblioteka integrująca clutter z GTK+.

%package devel
Summary:	Header files for clutter-gtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-gtk
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.10.0
Requires:	gtk+3-devel >= 3.2.0

%description devel
Header files for clutter-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-gtk.

%package static
Summary:	Static clutter-gtk library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-gtk
Group:		X11/Development/Libraries
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
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang cluttergtk-1.0

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f cluttergtk-1.0.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libclutter-gtk-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-gtk-1.0.so.0
%{_libdir}/girepository-1.0/GtkClutter-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gtk-1.0.so
%{_includedir}/clutter-gtk-1.0
%{_pkgconfigdir}/clutter-gtk-1.0.pc
%{_datadir}/gir-1.0/GtkClutter-1.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gtk-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-1.0
