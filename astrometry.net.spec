Name: astrometry.net
Version: 0.72
Release: 1%{?dist}
Summary: Astrometry Engine
Group: Sciences/Astronomy
License: BSD
URL: http://astrometry.net/downloads/%{name}-%{version}.tar.gz
Source0: %{name}-%{version}.tar.gz
Source1: astrometry.net.sh
Source2: astrometry.net.csh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: cfitsio-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libXrender-devel
BuildRequires: netpbm-devel
BuildRequires: python-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: zlib-devel

Requires: netpbm-progs
Requires: numpy
Requires: pyfits
Requires: python

%description
The astrometry engine will take any image and return the astrometry world
coordinate system (WCS)—ie, a standards-based description of the (usually
nonlinear) transformation between image coordinates and sky coordinates—with
absolutely no “false positives” (but maybe some “no answers”).  It will do its
best, even when the input image has no—or totally incorrect—meta-data.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} \
	ARCH_FLAGS="%{optflags}" \
	INSTALL_DIR="%{buildroot}/opt/astrometry.net" \
	FINAL_DIR="/opt/astrometry.net" \
	%{?el5:CFITS_INC="-D_REENTRANT -I/usr/include/cfitsio"}

%install
rm -rf %{buildroot}
make %{?_smp_mflags} install \
	ARCH_FLAGS="%{optflags}" \
	INSTALL_DIR="%{buildroot}/opt/astrometry.net" \
	FINAL_DIR="/opt/astrometry.net"

mkdir -p %{buildroot}/etc/profile.d
cp -p %SOURCE1 %{buildroot}/etc/profile.d/
cp -p %SOURCE2 %{buildroot}/etc/profile.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/profile.d
/opt/astrometry.net

%changelog
* Wed Aug 02 2017 Ira W. Snyder <isnyder@lco.global> - 0.72-1
- New version.
* Fri Dec 04 2015 Ira W. Snyder <isnyder@lco.global> - 0.64-1
- New version.
* Mon Aug 24 2015 Ira W. Snyder <isnyder@lco.global> - 0.56-1
- Initial build, using instructions from Curtis McCully.
- The EL5 cfitsio-devel pkg-config file contains wrong cflags, so we fix it
  locally in this file.
