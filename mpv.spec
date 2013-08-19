Name:           mpv
Version:        0.1.2
Release:        1%{?dist}
Summary:        Movie player playing most video formats and DVDs
License:        GPLv3+
URL:            http://%{name}.io/
Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}.tar.gz

# set defaults for Fedora
Patch0:         %{name}-config.patch

BuildRequires:  aalib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  arts-devel
BuildRequires:  a52dec-devel
BuildRequires:  bzip2-devel
BuildRequires:  directfb-devel
BuildRequires:  enca-devel
BuildRequires:  esound-devel
BuildRequires:  ffmpeg-devel >= 0.10
BuildRequires:  fribidi-devel
BuildRequires:  giflib-devel
BuildRequires:  gsm-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  libass-devel >= 0.9.10
BuildRequires:  libbluray-devel
BuildRequires:  libbs2b-devel
BuildRequires:  libcaca-devel
BuildRequires:  libcdio-devel
BuildRequires:  libdca-devel
BuildRequires:  libdv-devel
BuildRequires:  libdvdnav-devel >= 4.1.3-1
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  libmpg123-devel
BuildRequires:  libnemesi-devel >= 0.6.3
BuildRequires:  librtmp-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXv-devel
BuildRequires:  libXvMC-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  lirc-devel
#BuildRequires:  live555-devel #broken - see libnemesi as an alternative
BuildRequires:  lzo-devel >= 2
BuildRequires:  openal-soft-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python-docutils
BuildRequires:  speex-devel >= 1.1
BuildRequires:  svgalib-devel
BuildRequires:  twolame-devel
BuildRequires:  xmms-devel
BuildRequires:  xvidcore-devel >= 0.9.2
BuildRequires:  x264-devel >= 0.0.0-0.28
BuildRequires:  yasm

%description
Mpv is a movie player that plays most MPEG, VOB, AVI, OGG/OGM,
VIVO, ASF/WMA/WMV, QT/MOV/MP4, FLI, RM, NuppelVideo, yuv4mpeg, FILM,
RoQ, and PVA files. You can also use it to watch VCDs, SVCDs, DVDs,
3ivx, RealMedia, and DivX movies.
It supports a wide range of output drivers including X11, XVideo, DGA,
OpenGL, SVGAlib, fbdev, AAlib, DirectFB etc. There are also nice
antialiased shaded subtitles and OSD.
It is a fork of mplayer and mplayer2.

%prep
%setup -q
%patch0 -p1

%build
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --mandir=%{_mandir} \
    --confdir=%{_sysconfdir}/%{name} \
    --extra-cflags="$RPM_OPT_FLAGS" \
    --enable-joystick \
    --enable-lirc \
    --enable-radio \
    --enable-radio-capture \
    --disable-termcap

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Default config files
install -Dpm 644 etc/example.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%files
%doc AUTHORS LICENSE README.md Copyright
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf

%changelog
* Mon Aug 19 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-1
- Initial spec
- Inspired a lot in mplayer.spec

