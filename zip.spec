Summary: A file compression and packaging utility compatible with PKZIP.
Name: zip
Version: 2.3
Release: 30
License: distributable
Group: Applications/Archiving
Source: ftp.uu.net:/pub/archiving/zip/src/zip23.tar.gz
Source1: ftp://ftp.freesoftware.com/pub/infozip/src/zcrypt29.tar.gz
URL: http://www.info-zip.org/pub/infozip/Zip.html
Patch0: zip23.patch
Patch1: exec-shield.patch
Patch2: zip23-umask.patch
Patch3: zip-2.3-near-4GB.patch
Patch4: zip-2.3-configure.patch
Patch5: zip-2.3-currdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%prep
%setup -q -a 1
%patch0 -p1 -b .zip
%patch1 -p1 -b .zip
%patch2 -p1 -b .umask
%patch3 -p1 -b .4gb
%patch4 -p1 -b .cfg
%patch5 -p1 -b .currdir

%build
make -f unix/Makefile prefix=/usr "CFLAGS=$RPM_OPT_FLAGS -I. -DUNIX -D_LARGEFILE64_SOURCE" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

make -f unix/Makefile prefix=$RPM_BUILD_ROOT/usr \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

pushd $RPM_BUILD_ROOT
for n in zipnote zipsplit zip zipcloak ; do
    chmod 755 ./usr/bin/$n
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS CHANGES MANUAL TODO WHATSNEW WHERE LICENSE
%doc proginfo/algorith.txt
/usr/bin/zipnote
/usr/bin/zipsplit
/usr/bin/zip
/usr/bin/zipcloak
%{_mandir}/man1/zip.1*

%changelog
* Mon Mar  7 2005 Ivana Varekova <varekova@redhat.com> 2.3-30
- rebuilt

* Mon Jan 17 2005 Ivana Varekova <varekova@redhat.com> 2.3-29
- Fix bug #142237 - problem with -d and ./files containing archives

* Mon Jun 21 2004 Lon Hohberger <lhh@redhat.com> 2.3-24
- Extend max file/archive size to 2^32-8193 (4294959103) bytes
- Include better debugging output for configure script

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 19 2004 Lon Hohberger <lhh@redhat.com> 2.3-22
- Fix typos

* Tue Feb 17 2004 Lon Hohberger <lhh@redhat.com> 2.3-21
- Include LICENSE file per bugzilla #116004

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec 22 2003 Lon Hohberger <lhh@redhat.com> 2.3-19
- Make temp file have umask 0066 mode (#112516)

* Fri Oct 24 2003 Lon Hohberger <lhh@redhat.com> 2.3-18
- Incorporate Arjan's exec-shield patch for i386

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr  2 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Don't strip explicitly

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.3-11
- Add URL

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Aug 25 2000 Bill Nottingham <notting@redhat.com>
- add encryption code (#16878)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild in new environment

* Mon Mar 13 2000 Bill Nottingham <notting@redhat.com>
- spec file cleanups (#10143)

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- fix some perms

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Tue Jan 11 2000 Bill Nottingham <notting@redhat.com>
- update to 2.3

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- updated text in the spec file

* Fri Jan 15 1999 Cristian Gafton <gafton@redhat.com>
- patch top build on the arm

* Mon Dec 21 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
