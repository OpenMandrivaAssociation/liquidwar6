Name:		liquidwar6
Version:	0.0.13beta
Release:	%mkrel 2
Summary:	Unique multiplayer wargame
License:	GPLv3
Group:		Games/Arcade
URL:		http://www.gnu.org/software/liquidwar6/
Source0:	http://ftp.gnu.org/gnu/liquidwar6/%{name}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	expat-devel
BuildRequires:	gtk+2-devel
BuildRequires:	guile-devel
BuildRequires:	jpeg-devel
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libstdc++-static-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	png-devel
BuildRequires:	readline-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel

%description
Liquid War 6 is a unique multiplayer wargame. Your army is a blob of
liquid and you have to try and eat your opponents. Rules are very
simple yet original, they have been invented by Thomas Colcombet. It
is possible to play alone against the computer but the game is really
designed to be played with friends, on a single computer, on a LAN, or
on Internet.

Warning! The game is still under heavy development and may be unstable.

%prep
%setup -q

%build
# Don't build static and shared libraries, build only game binary
%configure2_5x --enable-allinone
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__rm -rf %{buildroot}%{_libdir}
%__rm -rf %{buildroot}%{_includedir}

desktop-file-install	--vendor="" \
			--dir %{buildroot}%{_datadir}/applications \
			--add-category="ArcadeGame" \
			%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%if %{mdvver} < 201200
%post
%_install_info %{name}*.info

%preun
%_remove_install_info %{name}*.info
%endif

%files -f %{name}.lang
%doc AUTHORS README NEWS COPYING
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}-%{version}
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man6/*
%{_infodir}/%{name}*

