usercrond
=========

hacked up vixie crond that runs as a user instead of root and reads crons from a .d style directory


the src.rpm should be able to generate an rpm - otherwise it's currently up to you to extract, patch, build and install.


The real magic is in SOURCE/make-usercrond.patch

this is basically a rhel crond source rpm extracted.  spec, patches, and original source.

basic usage is to run the usercrond binary as the user you want to run as.

by default it looks for $HOME/cron.d/

ls -l cron.d/
total 16
-r--r--r-- 1 tw tw 1704 Jan 10 16:24 deploy-crons
-r--r--r-- 1 tw tw  339 Jun 11  2012 serverdb-maint

the files in there are bog standard crontabs.  (no user column!)   add one, it gets picked up and read.


tada.

sample sysV init script in usercrond.init (requires config for the user to run it as - just su's to the user)



Credit to Scott F, if he ever wants to take it, for doing the real work to make this happen!  I just provided the idea and the push!
