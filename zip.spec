Summary: A file compression and packaging utility compatible with PKZIP.
Name: zip
Version: 2.3
Release: 11
Copyright: distributable
Group: Applications/Archiving
Source: ftp.uu.net:/pub/archiving/zip/src/zip23.tar.gz
Source1: ftp://ftp.freesoftware.com/pub/infozip/src/zcrypt29.tar.gz
URL: http://www.info-zip.org/pub/infozip/Zip.html
Patch0: zip23.patch
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

%build
make -f unix/Makefile prefix=/usr "CFLAGS=$RPM_OPT_FLAGS -I. -DUNIX" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

make -f unix/Makefile prefix=$RPM_BUILD_ROOT/usr \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

pushd $RPM_BUILD_ROOT
for n in zipnote zipsplit zip zipcloak ; do
    strip ./usr/bin/$n
    chmod 755 ./usr/bin/$n
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS CHANGES MANUAL TODO WHATSNEW WHERE proginfo/algorith.txt
/usr/bin/zipnote
/usr/bin/zipsplit
/usr/bin/zip
/usr/bin/zipcloak
%{_mandir}/man1/zip.1*

%changelog
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
