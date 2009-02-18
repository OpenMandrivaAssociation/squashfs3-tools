%define sqname	squashfs
%define sqver	3.3
%undefine sqrelease
%define rel 4
%define release	%mkrel %{?sqrelease:1.%{sqrelease}.}%{rel}
%define distname %{sqname}%{sqver}%{?sqrelease:-%{sqrelease}}
%define	Summary	Utilities for the creation of compressed squashfs images

Name:		%{sqname}-tools
Version:	%{sqver}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{distname}.tgz
Source1:	sqlzma.h
Source2:	sqmagic.h
Patch0:		sqlzma2u-3.3.patch
Patch1:		squashfs3.3-nolzma.patch
# from CVS, fix hang when dealing with sparse files
Patch2:		squashfs3.3-sparse.patch
BuildRequires:	lzma-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .lzma
%patch1 -p1 -b .nolzma
%patch2 -p0 -b .sparse
cp %{SOURCE1} %{SOURCE2} %{name}

%build
%make -C %{name} Sqlzma=. LzmaAlone=%{_libdir} LzmaC=%{_libdir}

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 %{name}/mksquashfs %{name}/unsquashfs %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS CHANGES README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
