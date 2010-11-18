Summary:	Library integrating clutter with GTK+
Summary(pl.UTF-8):	Biblioteka integrująca clutter z GTK+
Name:		clutter-gtk
Version:	0.10.8
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://www.clutter-project.org/sources/clutter-gtk/0.10/%{name}-%{version}.tar.gz
# Source0-md5:	2233c7f92535f5017accea04701131cd
Patch0:		gobject-introspection.patch
Patch1:		%{name}-fix.patch
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-modules
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
Requires:	clutter-devel >= 1.0.0
Requires:	gtk+2-devel >= 2:2.10.0

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
%attr(755,root,root) %{_libdir}/libclutter-gtk-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-gtk-0.10.so.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gtk-0.10.so
%{_libdir}/libclutter-gtk-0.10.la
%{_includedir}/clutter-1.0/%{name}
%{_pkgconfigdir}/clutter-gtk-0.10.pc
%{_datadir}/gir-1.0/*.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-gtk-0.10.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
