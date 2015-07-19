%define sqname squashfs
%define debug_package %{nil}

Name:		%{sqname}3-tools
Version:	3.3
Release:	16
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}%{version}.tgz
Source1:	sqlzma.h
Source2:	sqmagic.h
Patch0:		sqlzma2u-3.3.patch
Patch1:		squashfs3.3-nolzma.patch
# from CVS, fix hang when dealing with sparse files
Patch2:		squashfs3.3-sparse.patch
BuildRequires:	liblzmadec-devel
BuildRequires:	zlib-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{sqname}%{version}
%patch0 -p1 -b .lzma
%patch1 -p1 -b .nolzma
%patch2 -p0 -b .sparse
cp %{SOURCE1} %{SOURCE2} squashfs-tools

%build
%setup_compile_flags
%make -C squashfs-tools Sqlzma=. LzmaAlone=%{_libdir} LzmaC=%{_libdir} CC=gcc

%install
install -d %{buildroot}%{_bindir}
install -m 755 squashfs-tools/mksquashfs %{buildroot}%{_bindir}/mksquashfs3
install -m 755 squashfs-tools/unsquashfs %{buildroot}%{_bindir}/unsquashfs3

%files
%doc ACKNOWLEDGEMENTS CHANGES README
%{_bindir}/mksquashfs3
%{_bindir}/unsquashfs3
