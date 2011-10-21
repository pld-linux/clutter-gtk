Summary:	Library integrating clutter with GTK+
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GTK+
Name:		clutter-gtk
Version:	0.10.8
Release:	5
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://www.clutter-project.org/sources/clutter-gtk/0.10/%{name}-%{version}.tar.gz
# Source0-md5:	2233c7f92535f5017accea04701131cd
Patch0:		gobject-introspection.patch
Patch1:		%{name}-fix.patch
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 0.9.3
BuildRequires:	gtk+2-devel >= 2:2.19.5
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	python-modules
Requires:	clutter >= 1.2.0
Requires:	gtk+2 >= 2:2.19.5
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
Requires:	clutter-devel >= 1.2.0
Requires:	gtk+2-devel >= 2:2.19.5

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
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libclutter-gtk-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-gtk-0.10.so.0
%{_libdir}/girepository-1.0/GtkClutter-0.10.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gtk-0.10.so
%{_includedir}/clutter-1.0/%{name}
%{_pkgconfigdir}/clutter-gtk-0.10.pc
%{_datadir}/gir-1.0/GtkClutter-0.10.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gtk-0.10.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
