#Specify default cron.d directory for a users
#%define CRONDIRPATH /opt/cron.d
Summary: Cron daemon (based on vixie cron) for executing specified programs at set times for users.
Name: 	 usercrond
Version: 1.0
Release: 1%{?dist}
Epoch:   1
License: distributable
Group:   System Environment/Base
Source0: usercrond-1.0.tar.gz
Source1: vixie-cron.init
Source2: crond.sysconfig
Patch0:  vixie-cron-4.1-_0_rh_Makefile.patch
Patch1:  vixie-cron-4.1-_1_rh_pathnames.patch
Patch2:  vixie-cron-4.1-_2_config.patch
Patch3:  vixie-cron-4.1-_3_selinux.patch
Patch4:  vixie-cron-4.1-_4_vfork_sigchld.patch
Patch5:  vixie-cron-4.1-_5_sprintf_misc.patch
Patch6:  vixie-cron-4.1-_6_rh_crond.patch
Patch7:  vixie-cron-4.1-_7_crontab-stdin.patch
Patch8:  vixie-cron-4.1-_8_root-allowed.patch
Patch9:  vixie-cron-4.1-_9_no-header.patch
Patch10: vixie-cron-4.1-_10_manpages.patch
Patch11: vixie-cron-4.1-_11_with_selinux.patch
Patch12: vixie-cron-4.1-_12_pam.patch
Patch13: vixie-cron-4.1-_13_with_pam.patch
Patch14: vixie-cron-4.1-_14_pamd_crond.patch
Patch15: vixie-cron-4.1-_15_system_crontab_user.patch
Patch16: vixie-cron-4.1-_16_crontab_selinux.patch
Patch17: vixie-cron-4.1-_17_pam-rootok.patch
Patch18: vixie-cron-4.1-_18_cron_log_facility.patch
Patch19: vixie-cron-4.1-_19_crontab_stat_not_fstat.patch
Patch20: vixie-cron-4.1-_20_nickname_man.patch
Patch21: vixie-cron-4.1-_21_-i_option.patch
Patch22: vixie-cron-4.1-_22_no_0600_mode_enforce.patch
Patch23: vixie-cron-4.1-_23_freecon_segv.patch
Patch24: vixie-cron-4.1-_24_crontab_selinux_new.patch
Patch25: vixie-cron-4.1-_25-allow-root-crontab.patch
Patch26: vixie-cron-4.1-_26-saved-uids.patch
Patch27: vixie-cron-4.1-_27-no-strip-header-comments.patch
Patch28: vixie-cron-4.1-_28-fix_ppc.patch
Patch29: vixie-cron-4.1-_29-permit_any_crontab_option.patch
Patch30: vixie-cron-4.1-_30-uninitialized.patch
Patch31: vixie-cron-4.1-_31-allow_pam_access.patch
Patch32: vixie-cron-4.1-_32-no_mail_rcpt_safe_p.patch
Patch33: vixie-cron-4.1-_33-fix_selinux_segfault.patch
Patch34: vixie-cron-4.1-_34-pam_fail_close_session.patch
Patch35: vixie-cron-4.1-_35-crontab-job-control.patch
Patch36: vixie-cron-4.1-_36-pam_close_fork_fail.patch
Patch37: vixie-cron-4.1-_37-limits.patch
Patch38: vixie-cron-4.1-_38-CAN-2005-1038.patch
Patch39: vixie-cron-4.1-loginuid.patch
Patch40: vixie_cron-4.1-162887.patch
Patch41: vixie-cron-4.1-CAN-2005-1038-fix-race.patch
Patch42: vixie-cron-4.1-_42-getseuserbyname.patch
Patch43: vixie-cron-4.1-_43-config_comments.patch
Patch44: vixie-cron-4.1-_44-build_env.patch
Patch45: vixie-cron-4.1-_45-warnings.patch
Patch46: vixie-cron-4.1-_46-audit.patch
Patch47: vixie-cron-4.1-_47-m_option.patch
Patch48: vixie-cron-4.1-_48-security.patch
Patch49: vixie-cron-4.1-_49-bz178436.patch
Patch50: vixie-cron-4.1-_50-bz178931.patch
Patch51: vixie-cron-4.1-_51-bz180145-mail_i18n.patch
Patch52: vixie-cron-4.1-_52-bz181439.patch
Patch53: vixie-cron-4.1-_53_bz199294_selinux_mls.patch
Patch54: vixie-cron-4.1-_54_bz198019_database_changes.patch
Patch55: vixie-cron-4.1-man-page-typo.patch
Patch56: vixie-cron-4.1-_55-bz203746.patch
Patch57: vixie-cron-4.1-_44-delayed_database.patch 
Patch58: vixie-cron-4.1-_52-bz181439_2.patch
Patch59: vixie-cron-4.1-_56-pam-session-system-auth.patch
Patch60: vixie-cron-4.1-_60-SELinux-contains-range.patch
Patch63: vixie-cron-4.1-owl-st_nlink.patch
Patch61: vixie-cron-4.1-_61-audit.patch
Patch62: vixie-cron-4.1-manual.patch
Patch64: vixie-cron-4.1-_61symlink.patch
Patch65: vixie-cron-4.1-tmp.patch
Patch66: vixie-cron-4.1-_62newyear.patch
Patch67: vixie-cron-4.1-_63homedir.patch
Patch68: vixie-cron-4.1-wohome.patch
Patch69: make-usercrond.patch

Buildroot: %{_tmppath}/%{name}-%{version}-root
Requires: syslog, bash >= 2.0
Conflicts: sysklogd < 1.4.1
#%if %{WITH_SELINUX}
#Requires: libselinux >= 1.25.2-1
#Buildrequires: libselinux-devel >= 1.25.2-1
#%endif
#%if %{WITH_PAM}
#Requires: pam >= 0.77-66.8
#Buildrequires: pam-devel >= 0.77-66.8
#%endif
#%if %{WITH_AUDIT}
#Requires: audit-libs >= 1.0.3
#Buildrequires: audit-libs >= 1.0.3
#Buildrequires: audit-libs-devel >= 1.0.3
#%endif

%description
The vixie-cron package contains the Vixie version of cron.  Cron is a
standard UNIX daemon that runs specified programs at scheduled times.
Vixie cron adds better security and more powerful configuration
options to the standard version of cron.

%prep
%setup -q
%patch0 -p1 -b .rh_Makefile
%patch1 -p1 -b .rh_pathnames
%patch2 -p1 -b .config
%patch3 -p1 -b .selinux
%patch4 -p1 -b .vfork_sigchld
%patch5 -p1 -b .sprintf_misc
%patch6 -p1 -b .rh_crond
%patch7 -p1 -b .crontab-stdin
%patch8 -p1 -b .root-allowed
%patch9 -p1 -b .no-header
%patch10 -p1 -b .manpages
#%if %{WITH_SELINUX}
#SELinux
# Enables SELinux support
%patch11 -p1 -b .with_selinux
#%endif
%patch12 -p1 -b .pam
#%if %{WITH_PAM}
%patch13 -p1 -b .with_pam
%patch14 -p1 -b .pamd_crond
%patch15 -p1 -b .system_crontab_user
#%endif
%patch16 -p1 -b .crontab_selinux
%patch17 -p1 -b .pam-rootok
%patch18 -p1 -b .cron_log_facility
%patch19 -p1 -b .crontab_stat_not_fstat
%patch20 -p1 -b .nickname_man
%patch21 -p1 -b -i_option
%patch22 -p1 -b .no_0600_mode_enforce
#%if %{WITH_SELINUX}
%patch23 -p1 -b .freecon_segv
%patch24 -p1 -b .selinux_crontab_new
#%endif
%patch25 -p1 -b .allow-root-crontab
%patch26 -p1 -b .saved_uids
%patch27 -p1 -b .no-strip-header-comments
%patch28 -p1 -b .fix_ppc
%patch29 -p1 -b .permit_any_crontab_option
%patch30 -p1 -b .uninitialized
%patch31 -p1 -b .allow_pam_access
%patch32 -p1 -b .no_mail_rcpt_safe_p
%patch33 -p1 -b .fix_selinux_segfault
%patch34 -p1 -b .pam_fail_close_session
%patch35 -p1 -b .job_control
%patch36 -p1 -b .pam_close_fork_fail
%patch37 -p1 -b .limits
%patch38 -p1 -b .CAN-2005-1038
%patch39 -p1 -b .loginuid
%patch40 -p1 -b .162887
%patch41 -p1 -b .CAN-2005-1038-fix-race
%patch42 -p1 -b .getseuserbyname
%patch43 -p1 -b .config_comments
%patch44 -p1 -b .build_env
%patch45 -p1 -b .warnings
%patch46 -p1 -b .audit_deny
%patch47 -p1 -b .-m_option
%patch48 -p1 -b .security
%patch49 -p1 -b .bz178436
%patch50 -p1 -b .bz178931
%patch51 -p1 -b .mail_i18n
%patch52 -p1 -b .bz181439
%patch53 -p1 -b .selinux_mls
%patch54 -p1 -b .bz198019
%patch55 -p1 -b .man-page-typo
%patch56 -p1 -b .bz203746
%patch57 -p1 -b .delayed_database
%patch58 -p1 -b .bz181439_2
%patch59 -p1 -b .pam-session-system-auth
%patch60 -p1 -b .selinux-contains-range
%patch63 -p1 -b .st_nlink
%patch61 -p1 -b .audit
%patch62 -p1 -b .manual
%patch64 -p1 -b ._61symlink
%patch65 -p1 -b .tmp
%patch66 -p1 -b ._62newyear
%patch67 -p1 -b ._63homedir
%patch68 -p1 -b ._68wohome
%patch69 -p1 -b .make-usercrond

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -g -DLINT -Dlint" \
%if 0%(test "%CRONDIRPATH" != "")
CRONDIRPATH=%{CRONDIRPATH} \
%endif
;
#%if %{WITH_SELINUX}
#WITH_SELINUX=1 \
#%endif
#%if %{WITH_PAM}
#WITH_PAM=1 \
#%endif
#%if %{WITH_AUDIT}
#WITH_AUDIT=1 \
#%endif
#;

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
 
%preun

%postun
%if 0%(test "%CRONDIRPATH" != "")
rmdir %{CRONDIRPATH}
%endif

%pre
echo -e "\nWARNING : This RPM, %{name}, is from EA Sports OnDemand!\n"
%if 0%(test "%CRONDIRPATH" != "")
mkdir -pm 777 %{CRONDIRPATH}
%endif

%files

%attr(6755,root,root) /usr/bin/usercrond

%changelog
* Thu Apr 12 2012 Scott Fontan <sfontan@ea.com> - 1.0-1
- Created usercrond from vixie-cron source

* Tue Jul 15 2008 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-76
- 222464 crond failed "Days of week" after a few hours on 1st/Jan
- 241877 Cron does not handle home directories with group deny permissions
- 455379 cron jobs for users without home doesn't work
- Resolves: rhbz#241877, rhbz#222464, rhbz#455379

* Fri Jun 22 2007 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-72
- tmp directory variable
- Resolves: #232295

* Fri May 18 2007 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-71
- added back patches removed for previous errata - 222461, 223532, 223894
- Resolves: rhbz#222461, rhbz#223532, rhbz#223894

* Fri May 11 2007 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-70
- removed last patches, added only CVE 235880. Removed 222461, 223532, 223894.
- Resolves: rhbz#235880

* Mon Apr 30 2007 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-69
- Resolves: rhbz#222461

* Tue Apr 24 2007 Steve Grubb <sgrubb@redhat.com> - 4:4.1-68
- Resolves: #235880 CVE-2007-1856 crontab denial of service

* Tue Mar 20 2007 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-67
- fix in man page
- Resolves: rhbz#223532

* Mon Feb 5 2007 Dan Walsh <dwalsh@redhat.com> - 4:4.1-66.2
- Send audit message when setfilecon fails.
Resolves: #223894

* Sat Dec 30 2006 Dan Walsh <dwalsh@redhat.com> - 4:4.1-66.1
- Still broken.  cron should call setexeccon on system as well as user jobs
Resolves: #207433

* Fri Dec 15 2006 Dan Walsh <dwalsh@redhat.com> - 4:4.1-66
- MLS Option patch needs some tweeking
Resolves: #207433

* Mon Dec 11 2006 James Antill <james.antill@redhat.com> - 4:4.1-65
- Add MLS option for LSPP.
- Resolves: rhbz#207433

* Tue Sep 05 2006 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-64
- include system-auth for session in crond.pam, it now avoids
  using pam_unix if the process is crond

* Wed Aug 30 2006 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-63
- fix problem with selinux (#181439)

* Mon Aug 28 2006 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-61
- changes in spec file (#204230)

* Fri Aug 25 2006 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-60
- patch from Jose Plans fixed: Job delayed after using crontab -e

* Fri Aug 25 2006 Marcela Maslanova <mmaslano@redhat.com> - 4:4.1-59
- small changes in man-page cron
- (#203746) RFC3834, patch from James Ralston

* Thu Jul 20 2006 Jason Vas Dias <jvdias@redhat.com> - 4:4.1-58
- fix bug 199294: support for LSPP multiple per-job SELinux contexts
- fix bug 198019: make database.c correct if crontab mtime changes 
                  while spool dir mtime does not.

* Fri Jul 14 2006 Jason Vas Dias <jvdias@redhat.com> - 4:4.1-56.FC6
- fix bug 198893 - change permissions of cron spool directories to 0700

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4:4.1-55.FC6.1
- rebuild

* Tue May 30 2006 Jason Vas Dias <jvdias@redhat.com> - 4:4.1-55.FC6
- fix bug 191823: fix missing BuildRequires: audit-libs-devel

* Wed Feb 15 2006 Jason Vas Dias <jvdias@redhat.com> - 4:4.1-54.FC5
- fix bug 181702: Requires:audit-libs, not Requires:audit

* Tue Feb 14 2006 Jason Vas Dias <jvdias@redhat.com> - 4:4.1-52.FC5
- fix bug 181439: enable easier selection of optional 'WITH_*'
  compilation features

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4:4.1-51.FC5.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jason Vas Dias<jvdias@redhat.com> - 4.1-51.FC5
- fix bug 180145: provide support for mail in non-ascii charsets

* Thu Jan 26 2006 Jason Vas Dias<jvdias@redhat.com> - 4.1-50.FC5
- fix bug 178436: prevent per-minute jobs being delayed into next minute
- fix bug 178931: remove pam_unix and pam_krb5 from pam session stack

* Tue Jan 10 2006 Jason Vas Dias<jvdias@redhat.com>
- fix bug 177476: make minder/mailer process run as job user 
  with user context; re-organize PAM and SELinux code 
 
* Thu Dec 15 2005 Jason Vas Dias<jvdias@redhat.com>
- fix bug 172885: Replace Requires:sysklogd with Requires:syslog

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Nov 13 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-41.FC5
- patches for IBM LSPP testing:
- Steve Grubb's patch to emit audit log message on crontab denial
- Use of sendmail unacceptable for LSPP: provide -m <mail command> option

* Tue Oct 18 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-40.FC5
- *** NOTE : please do not modify vixie-cron without contacting ***
  *** the package maintainer (me at the moment).                ***
  *** Or at least test it first!                                ***
- fix bug 170830: it was not the pam_stack change - the setuid
  mode of crontab was dropped for some reason.
- apply Dan's new getseuserbyname patch
- somehow build_env() invocation was dropped - use pam_env settings.

* Fri Oct 14 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-39-FC5
- fix bug 170830: the last PAM change disabled all cron jobs.
  backing out the new PAM configuration file until I've had a
  chance to test it with replacement of pam_stack.so.

* Thu Oct 13 2005 Tomas Mraz <tmraz@redhat.com> - 4.1-38.FC5
- use include instead of pam_stack in pam config

* Sat Aug 13 2005 Dan Walsh <dwalsh@redhat.com>  - 4.1-37.FC5
- Change checkPasswdAccess to selinux_check_passwd_access for new selinux api

* Mon Jul 11 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-36.FC4
- fix bug 162887: allow multiple /etc/cron.d crontabs for *system* user
- further fix for bug 154920 / CAN-2005-1038 ( crontab -e ):
     invoke editor and copy operation as non-root user
   
* Fri Jun 17 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-FC4.34
- fix bug 160811: FC3 version compared >= FC4 version
- fix bug 159216: add pam_loginuid support for new audit system

* Thu Apr 14 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-33_FC4
- fix bug 154922 / CAN-2005-1038: check that new crontab is 
      regular file after editor session ends.
- fix bug 154575: use PATH_MAX (4096) as max filename length; also make 
      limits on command line and env.var. lengths sensible (131072).

* Fri Apr 08 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-32_FC4
- do pam_close_session and pam_setcred(pamh, PAM_DELETE_CRED)
- if fork fails

* Thu Apr 07 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-30_FC4
- fix bug 154065: crontab's job control broken: by 
-     xpid = waitpid(pid,&waiter,WUNTRACED);... 
-     if( WIFSTOPPED(waiter) )... kill(getpid(),WSTOPSIG(waiter));
- crontab should not kill itself with SIGSTOP if its child
- gets SIGSTOP; hence it does not need the waitpid WUNTRACED flag.
 
* Tue Apr 05 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-28_FC4
- Required for EAL Audit certification: 
- If pam_setcred should fail, the pam_session could fail to be
- closed, leaving autofs user directories still mounted.

* Tue Mar 15 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-26_FC4
- fix bug 151145: segfault if cronjob runs without any SELinux user 
- security context (eg. in a broken chroot environment)

* Fri Feb 25 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-24_FC4
- Add an /etc/sysconfig/crond file for containing CRONDARGS and
- settings like CRON_VALIDATE_MAILRCPTS .

* Fri Feb 25 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-24_FC4
- Fix bug 147636 - disable silly mail recipient name checking 
- (do_command.c's safe_p()) by default . Can be enabled by 
- presence of CRON_VALIDATE_MAILRCPTS variable in crond's 
- environment - also '_'s in MAILTOs are allowed.

* Tue Jan 25 2005 Jason Vas Dias <jvdias@redhat.com> - 4.1-22
- Fix bug 146073 - allow the 'pam_access' module to be used with
- cron - set 'PAM_TTY' item to 'cron' .

* Wed Dec 20 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-21
- fix bug 142953 : allow read-only crontabs + provide -p 
- 'permit all crontabs' option to disable mode checking. 

* Wed Dec 20 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-21
- fixed all uninitialized variable warnings

* Fri Dec 03 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-20
- Fix for ppc -m32 RPM_OPT_FLAGS compilation options
- (bug 141760)

* Fri Oct 15 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-19
- crontab -e should only strip NHEADER_LINES comments 
- (NHEADER_LINES==0), not at least one header comment line.
- (bug 135845)

* Sat Oct 09 2004 Florian La Roche <laroche@redhat.com> - 4.1-18
- no need to make user installed crontabs readable

* Thu Sep 30 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-17
- Users not allowed to use 'crontab mycrontab', while
- 'crontab < mycrontab' allowed; this is because misc.c's
- swap_uids_back() was not using save_euid / save_egid .
- Thanks to Mads Martin Joergensen <mmj@suse.de> for pointing this out.

* Wed Sep 29 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-16
- Just found out in testing that if neither /etc/cron.{deny,allow}
- exist, root is unable to use crontab - I'm sure root could before,
- but is in any case meant to be able to. Allowing root to use crontab.

* Wed Sep 29 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-14
- Fix for bug 130102 got dropped somehow from latest CVS.
- This is now restored - in %post, if neither /etc/cron.{deny,allow}
- exist, touch /etc/cron.deny, to allow all users to use crontab,
- as was previous default vixie-cron behaviour.

* Fri Sep 17 2004 Jason Vas Dias <jvdias@redhat.com> - 4.1-12
- Merged Dan's patch with vixie-cron-4.1-11 which was not 
- latest version according to new CVS ?!?!

* Fri Sep 17 2004 Dan Walsh <dwalsh@redhat.com>  - 4.1-12
- Updated SELinux patch to use checkPasswdAccess

* Tue Aug 31 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-11
- Fixed SIGSEGV in free_user when !is_selinux_enabled() and crontab
- has no valid jobs (bug 131390).

* Wed Aug 18 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.10
- Fixed bug 130102: Restored default behaviour if neither 
- /etc/cron.deny nor /etc/cron.allow exist - 'touch /etc/cron.deny'
- in %post

* Wed Aug 11 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.9
- Removed 0600 mode enforcement as per Florian La Roche's request

* Tue Aug 10 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.8
- Allowed editors such as 'gedit' which do not modify original
- file, but which rename(2) a temp file to original, to be used
- by crontab -e (bug 129170).

* Tue Aug 10 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.8
- Added '-i' option to crontab to prompt the user before deleting
- crontab with '-r'.

* Tue Aug 10 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.8
- Added documentation for '@' nicknames to crontab.5
- (bugs 107542, 89899). Also removed 'second when' (bug 59802). 

* Sun Aug 1  2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.7
- fixed bug 128924: 'cron' log facility not being used

* Fri Jul 30 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1.6
- Added PAM 'auth sufficient pam_rootok.so' to /etc/pam.d/crond
- (fixes bug 128843) - on dwalsh's advice.

* Thu Jul 29 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-5
- Added Buildrequires: pam-devel

* Wed Jul 28 2004 Dan Walsh <dwalsh@redhat.com> - 4.1-4
- Fix crontab to do SELinux checkaccess

* Wed Jul 28 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-3
- Fixed bug 128701: cron fails to parse user 6th field in
- system crontabs (patch15)

* Tue Jul 27 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-2
- Changed 'Requires' dependency from 'pam-devel' to 'pam'.

* Mon Jul 26 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-1
- Added PAM access control support.

* Thu Jul 22 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-1
- Changed post-install to change mode of existing crontabs to
- 0600 to allow run by new ISC cron 4.1 

* Thu Jul 22 2004 Jason Vas Dias <jvdias@redhat.com>  - 4.1-1
- Upgraded to ISC cron 4.1

* Thu Jul  1 2004 Jens Petersen <petersen@redhat.com> - 3.0.1-94
- add vixie-cron-3.0.1-cron-descriptors-125110.patch to close std descriptors
  when forking (Bernd Schmidt, 121280)
- add vixie-cron-3.0.1-no-crontab-header-89809.patch to not prepend header to
  crontab files (Damian Menscher, 103899)
- fix use of RETVAL in init.d script (Enrico Scholz, 97784)
- add safer malloc call to vixie-cron-3.0.1-sprintf.patch 
- add cron-3.0.1-crontab-syntax-error-114386.patch to fix looping on crontab
  syntax error (Miloslav Trmac, 89937)

* Fri Jun 25 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-93
- Add fixes from NSA 

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-92
- Add fixes from NSA 

* Tue Jun 15 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-91
- Change patch to check SElinux properly, go back to using fname instead of uname

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jun 4 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-89
- Fix patch

* Fri Jun 4 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-88
- Add patch to allow it to run in permissive mode.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 4 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-86
- Add security_getenforce check.

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> - 3.0.1-85
- Fix call to is_selinux_enabled()

* Mon Dec 8 2003 Dan Walsh <dwalsh@redhat.com> - 3.0.1-84
- change daemon flag to 1

* Wed Dec 3 2003 Dan Walsh <dwalsh@redhat.com> - 3.0.1-83
- Add daemon to make sure child is clean

* Fri Nov  7 2003 Jens Petersen <petersen@redhat.com> - 3.0.1-82
- add vixie-cron-3.0.1-pie.patch to build crond as pie (#108414)
  [Ulrich Drepper]
- require libselinux and buildrequire libselinux-devel

* Thu Oct 30 2003 Dan Walsh <dwalsh@redhat.com> - 3.0.1-81.sel
- turn on selinux

* Tue Sep 30 2003 Jens Petersen <petersen@redhat.com> - 3.0.1-80
- add vixie-cron-3.0.1-vfork-105616.patch to use fork instead of vfork
  (#105616) [report and patch from ian@caliban.org]
- update vixie-cron-3.0.1-redhat.patch not to change DESTMAN redundantly
  (it is overrriden in the spec file anyway)

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> - 3.0.1-79
- turn off selinux

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> - 3.0.1-78.sel
- turn on selinux

* Tue Jul 29 2003 Dan Walsh <dwalsh@redhat.com> - 3.0.1-77
- Patch to run on SELinux

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 19 2003 Jens Petersen <petersen@redhat.com> - 3.0.1-75
- add vixie-cron-3.0.1-root_-u-85879.patch from Valdis Kletnieks to allow
  root to run "crontab -u <user>" even for users that aren't allowed to

* Wed Feb 19 2003 Jens Petersen <petersen@redhat.com> - 3.0.1-74
- fix preun script typo (#75137) [reported by Peter Bieringer]

* Tue Feb 11 2003 Bill Nottingham <notting@redhat.com> 3.0.1-73
- don't set SIGCHLD to SIG_IGN and then try and wait... (#84046)

* Fri Feb  7 2003 Nalin Dahyabhai <nalin@redhat.com> 3.0.1-72
- adjust cron.d patch so that it ignores file with names that begin with '#'
  or end with '~', '.rpmorig', '.rpmsave', or '.rpmnew'
- merge hunk of buffer overflow patch into the cron.d patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 3.0.1-70
- rebuild on all arches

* Sat Jul 20 2002 Akira TAGOH <tagoh@redhat.com> 3.0.1-69
- vixie-cron-3.0.1-nonstrip.patch: applied to fix the stripped binary issue.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 10 2002 Bill Huang <bhuang@redhat.com>
- Fix preun bugs.(#55340)
- Fix fprintf bugs.(#65209)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 15 2002 Bill Huang <bhuang@redhat.com>
- Fixed #62963.

* Thu Apr 04 2002 James McDermott <jmcdermo@redhat.com>
- Alter behavior of crontab to take stdin as the default
  behavior if no options are specified. 

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Mar  8 2001 Bill Nottingham <notting@redhat.com>
- add patch from Alan Eldridge <alane@geeksrus.net> to
  fix double execution of jobs (#29868)

* Mon Feb 11 2001 Bill Nottingham <notting@redhat.com>
- fix buffer overflow in crontab

* Wed Feb  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- fix usage string in initscript (#26533)

* Tue Feb  6 2001 Bill Nottingham <notting@redhat.com>
- fix build with new glibc (#25931)

* Tue Jan 23 2001 Bill Nottingham <notting@redhat.com>
- change i18n mechanism

* Fri Jan 19 2001 Bill Nottingham <notting@redhat.com>
- log as 'crond', not 'CROND' (#19410)
- account for shifts in system clock (#23230, patch from <pererik@onedial.se>)
- i18n-ize initscript

* Thu Aug 24 2000 Than Ngo <than@redhat.com>
- fix to set startup position correct at update

* Wed Aug 24 2000 Than Ngo <than@redhat.com>
- add /sbin/service to Prereq
- call /sbin/service instead service
- fix startup position (Bug #13353)

* Mon Aug  7 2000 Bill Nottingham <notting@redhat.com>
- fix crond logging patch (dan@doom.cmc.msu.ru)
- log via syslog (suggestion from jos@xos.nl)
- put system crontab location in crontab(5) (#14842)

* Fri Jul 28 2000 Bill Nottingham <notting@redhat.com>
- fix condrestart

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- fix reload bug (#14065)

* Fri Jul 14 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul  6 2000 Bill Nottingham <notting@redhat.com>
- prereq /etc/init.d

* Mon Jul  3 2000 Bill Nottingham <notting@redhat.com>
- fix %%post; we do condrestart in %%postun

* Thu Jun 29 2000 Bill Nottingham <notting@redhat.com>
- oops, fix init script

* Tue Jun 27 2000 Bill Nottingham <notting@redhat.com>
- require new initscripts, not prereq

* Mon Jun 26 2000 Bill Nottingham <notting@redhat.com>
- initscript hacks

* Wed Jun 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak logrotate config

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild in new env.
- FHS fixes
- don't ship chkconfig links

* Fri Mar 31 2000 Bill Nottingham <notting@redhat.com>
- fix non-root builds (#10490)

* Sun Mar 26 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- do not remove log files

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Wed Aug 25 1999 Bill Nottingham <notting@redhat.com>
- fix buffer overflow

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jul 30 1999 Michael K. Johnson <johnsonm@redhat.com>
- dayofmonth and month can't be 0

* Thu Jun  3 1999 Jeff Johnson <jbj@redhat.com>
- in cron.log use "kill -HUP pid" not killall to preserve errors (#2241).

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- add note to man page about DST conversion causing strangeness
- documented cron.d patch

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved cron.d patch

* Mon Apr 12 1999 Erik Troan <ewt@redhat.com>
- added cron.d patch

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- clean up log files on deinstallation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 28)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- reset SIGCHLD before grandchild execle (problem #732)

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch to get rid of the dangerous sprintf() calls
- added BuildRoot and Prereq: /sbin/chkconfig

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed cron/crond dichotomy in init file.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- fixed bad init symlinks

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- force it to use SIGCHLD instead of defunct SIGCLD

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- updated for chkconfig
- added status, restart options to init script

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Switch conditional from "axp" to "alpha" 

