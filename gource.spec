# TODO
# - use fonts-TTF-freefont
Summary:	Software version control visualization
Name:		gource
Version:	0.24
Release:	0.1
URL:		http://gource.googlecode.com/
Source0:	http://gource.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f896ebc6efbe3deed47dccf6c768dba5
License:	GPL v3+
Group:		X11/Applications
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	freetype-devel
BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL-based 3D visualisation tool for source control repositories.
The repository is displayed as a tree where the root of the repository
is the centre, directories are branches and files are leaves.
Contributors to the source code appear and disappear as they
contribute to specific files and directories.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gource
%dir %{_datadir}/gource
%{_datadir}/gource/*.png
%dir %{_datadir}/gource/fonts
%doc %{_datadir}/gource/fonts/README
%{_datadir}/gource/fonts/FreeSans.ttf
%{_mandir}/man1/gource.1*
