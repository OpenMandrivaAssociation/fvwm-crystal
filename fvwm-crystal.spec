%define         srcname        %{name}

Name:           fvwm-crystal
Version:        3.7.6
Release:        1
Summary:        An eye-candy and powerful desktop environment based on FVWM2
License:        GPLv2+
Group:          Graphical desktop/Other
URL:            https://fvwm-crystal.sourceforge.net/
Source0:        https://sourceforge.net/projects/fvwm-crystal/files/%{version}/%{srcname}-%{version}.tar.gz
#Source1:        fvwm-crystal.png

BuildArch:      noarch

#needed for various scripts
Requires:       (fvwm2 or fvwm3)
Requires:       python
Requires:       xscreensaver
Requires:       xterm
Requires:       xwd
Requires:       imagemagick
Requires:       feh
Requires:       xcompmgr
Recommends:       transset-df
Requires:       bc

%description
FVWM-Crystal aims at be an easy to use, eye-candy but also powerful
desktop environment based on the F Virtual Window Manager (FVWM2). It
uses the following programs: FVWM2 as a window manager and "main
core", icons on the desktop with support for more than ten different
file managers and custom commands, various terminal emulators, as well
as music and medias players... There is built-in support for
controlling these programs, plus several other tools dedicated to
setup a wallpaper or making screen shots. Fvwm-Crystal provide some
unique features like the ability to bring in full screen virtually any
application, and to flow through the full-screened applications and
the desktop.


%prep
%autosetup -n %{srcname}-%{version} -p1

%build

%install
%make_install prefix=%{_prefix} LOCALEDIR=%{_datadir}/locale localedir=%{_datadir}/locale

%__rm -f %{buildroot}%{_datadir}/locale/en
%__rm -f %{buildroot}%{_datadir}/locale/fy
%__rm -f %{buildroot}%{_datadir}/locale/fr
%__rm -f %{buildroot}%{_datadir}/locale/de
%__rm -f %{buildroot}%{_datadir}/locale/es
%__rm -f %{buildroot}%{_datadir}/locale/it
%__rm -f %{buildroot}%{_datadir}/locale/nl
%__rm -f %{buildroot}%{_datadir}/locale/zh_CN

#install -D -m644 %{SOURCE1} %{buildroot}%{_iconsdir}/fvwm-crystal.png

%find_lang %{name} --all-name

%posttrans
if [ "$1" -eq 1 ]; then
	if [ -e %{_datadir}/xsessions/10Fvwm-Crystal.desktop ]; then
		rm -rf %{_datadir}/xsessions/10Fvwm-Crystal.desktop
	fi
	if [ -e %{_sysconfdir}/X11/dm/Sessions/10Fvwm-Crystal.desktop ]; then
		rm -rf %{_sysconfdir}/X11/dm/Sessions/10Fvwm-Crystal.desktop
	fi
fi

%files -f %{name}.lang
%doc README.md AUTHORS NEWS ChangeLog session-management-README
%{_datadir}/xsessions/fvwm-crystal.desktop
%config(noreplace) %{_sysconfdir}/sudoers.d/fvwm-crystal
%{_bindir}/*
%{_docdir}/%{name}-%{version}
%{_mandir}/man1/*
%{_datadir}/%{name}
#{_iconsdir}/fvwm-crystal.png
