Summary: A file compression and packaging utility compatible with PKZIP
Name: zip
Version: 2.31
Release: 9%{?dist}
License: BSD
Group: Applications/Archiving
Source: http://ftp.info-zip.org/pub/infozip/src/zip231.tar.gz
URL: http://www.info-zip.org/pub/infozip/Zip.html
Patch0: zip23.patch
Patch1: zip-2.31-exec-shield.patch
Patch2: zip23-umask.patch
Patch5: zip-2.3-currdir.patch
Patch6: zip-2.31-install.patch
Patch7: zip-2.31-near-4GB.patch
Patch8: zip-2.31-configure.patch
Patch9: zip-2.31-time.patch
Patch10: zip-2.3-sf.patch
Patch11: zip-2.31-umask_mode.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%prep
%setup -q
%patch0 -p1 -b .zip
%patch1 -p1 -b .exec-shield
%patch2 -p1 -b .umask
%patch5 -p1 -b .currdir
%patch6 -p1 -b .install
%patch7 -p1 -b .4gb
%patch8 -p1 -b .lhh
%patch9 -p1 -b .time
%patch10 -p1 -b .out
%patch11 -p1 -b .um

%build
make -f unix/Makefile prefix=%{_prefix} "CFLAGS=$RPM_OPT_FLAGS -I. -DUNIX -D_LARGEFILE64_SOURCE" generic_gcc  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} 
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

pushd $RPM_BUILD_ROOT
for n in zipnote zipsplit zip zipcloak ; do
        chmod 755 .%{_bindir}/$n
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README CHANGES TODO WHATSNEW WHERE LICENSE README.CR
%doc proginfo/algorith.txt
%{_bindir}/zipnote
%{_bindir}/zipsplit
%{_bindir}/zip
%{_bindir}/zipcloak
%{_mandir}/man1/zip.1*

%changelog
* Thu Dec  3 2009 Karel Klic <kklic@redhat.com> - 2.31-9
- Renamed exec-shield.patch to zip-2.31-exec-shield.patch
- Removed zcrypt29.tar.gz as it is no longer necessary

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.31-6
- Autorebuild for GCC 4.3

* Wed Nov 14 2007 Ivana Varekova <varekova@redhat.com> - 2.31-5
- add S_IWOTH option

* Mon Nov  5 2007 Ivana Varekova <varekova@redhat.com> - 2.31-4
- fix "zip does not honor umask setting when creating archives"
- fix "zip segfaults by attempt to archive big file"
- spec file cleanup

* Wed Feb  7 2007 Ivana Varekova <varekova@redhat.com> - 2.31-3
- incorporate the next peckage review comment

* Tue Feb  6 2007 Ivana Varekova <varekova@redhat.com> - 2.31-2
- incorporate the package review   

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.31-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.31-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.31-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Ivana Varekova <varekova@redhat.com> 2.31-1
- update to 2.31

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
