Summary:	Software version control visualization
Summary(pl.UTF-8):	Narzędzie wizualizujące kontrolę wersji
Name:		gource
Version:	0.43
Release:	5
License:	GPL v3+
Source0:	https://github.com/acaudwell/Gource/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d2b601782692301f6d8ecc97dc85d3f7
Patch0:		gl-ac.patch
URL:		http://gource.googlecode.com/
Group:		X11/Applications
BuildRequires:	GLM
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	freetype-devel
BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	glew-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	tinyxml-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	fonts-TTF-freefont
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software projects are displayed by Gource as an animated tree with the
root directory of the project at its centre. Directories appear as
branches with files as leaves. Developers can be seen working on the
tree at the times they contributed to the project.

Currently there is first party support for Git and Mercurial, and
third party (using additional steps) for CVS and SVN.

%description -l pl.UTF-8
Gource wyświetla projekty software'owe jako animowane drzewo z
katalogiem głównym projektu w centrum. Podkatalogi przedstawione są w
postaci gałęzi, a pliki to liście. Developerzy widoczni są przy pracy
nad drzewem w czasie gdy rzeczywiście pracowali.

Na chwilę obecną Gource natywnie wspiera repozytoria Git i Mercurial.
Przy pomocy zewnętrznych narzędzi można również oglądać repozytoria
CVS i SVN.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	CC=%{__cxx} \
	--with-tinyxml \
	--enable-ttf-font-dir=%{_datadir}/fonts/TTF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/gource
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.tga
%{_datadir}/%{name}/*.style
%{_datadir}/%{name}/shaders
%{_mandir}/man1/gource.1*
