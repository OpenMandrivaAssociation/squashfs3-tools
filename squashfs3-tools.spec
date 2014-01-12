%define sqname squashfs
%define debug_package %{nil}

Name:		%{sqname}3-tools
Version:	3.3
Release:	11
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
%make -C squashfs-tools Sqlzma=. LzmaAlone=%{_libdir} LzmaC=%{_libdir}

%install
install -d %{buildroot}%{_bindir}
install -m 755 squashfs-tools/mksquashfs %{buildroot}%{_bindir}/mksquashfs3
install -m 755 squashfs-tools/unsquashfs %{buildroot}%{_bindir}/unsquashfs3

%files
%doc ACKNOWLEDGEMENTS CHANGES README
%{_bindir}/mksquashfs3
%{_bindir}/unsquashfs3


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3-4mdv2011.0
+ Revision: 670012
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3-3mdv2011.0
+ Revision: 607559
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3-2mdv2010.1
+ Revision: 524123
- rebuilt for 2010.1

* Wed Feb 18 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.3-1mdv2009.1
+ Revision: 342569
- Fix buildrequire
- Make squashfs3-tools parallel-installable with squashfs-tools (for squashfs4)
- Fork squashfs-tools because we need support for squashfs3+lzma in One

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Olivier Blin <oblin@mandriva.com> 3.3-4mdv2008.1
+ Revision: 119554
- fix hang when dealing with sparse files (patch from CVS)

  + Thierry Vignaud <tv@mandriva.org>
    - fix description

* Thu Dec 13 2007 Olivier Blin <oblin@mandriva.com> 3.3-3mdv2008.1
+ Revision: 119429
- package unsquashfs

* Wed Dec 12 2007 Olivier Blin <oblin@mandriva.com> 3.3-2mdv2008.1
+ Revision: 119020
- rebuild with latest lzma static library to fix zlib support
- update sqlzma2u-3.3.patch from sqlzma3.3-fixed.tar.bz2

* Wed Nov 14 2007 Olivier Blin <oblin@mandriva.com> 3.3-1mdv2008.1
+ Revision: 108685
- 3.3
- update lzma patch and headers
- rediff nolzma patch

