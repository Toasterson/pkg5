#
# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL"), version 1.0.
# You may only use this file in accordance with the terms of version
# 1.0 of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source.  A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.
#

# Copyright 2024 OmniOS Community Edition (OmniOSce) Association.

include ../Makefile.com

ROOTUSRSHAREMAN = $(ROOTUSRSHARE)/man
MAN1DIR = $(ROOTUSRSHAREMAN)/man1
MAN7DIR = $(ROOTUSRSHAREMAN)/man7
MAN8DIR = $(ROOTUSRSHAREMAN)/man8
JA_MAN1DIR = $(ROOTUSRSHAREMAN)/ja_JP.UTF-8/man1
JA_MAN7DIR = $(ROOTUSRSHAREMAN)/ja_JP.UTF-8/man7
JA_MAN8DIR = $(ROOTUSRSHAREMAN)/ja_JP.UTF-8/man8
ZH_MAN1DIR = $(ROOTUSRSHAREMAN)/zh_CN.UTF-8/man1
ZH_MAN7DIR = $(ROOTUSRSHAREMAN)/zh_CN.UTF-8/man7
ZH_MAN8DIR = $(ROOTUSRSHAREMAN)/zh_CN.UTF-8/man8

MAN1 = \
	pkg.1 \
	pkgdepend.1 \
	pkgdiff.1 \
	pkgfmt.1 \
	pkglint.1 \
	pkgmerge.1 \
	pkgmogrify.1 \
	pkgrecv.1 \
	pkgrepo.1 \
	pkgsend.1 \
	pkgsign.1 \
	pkgsurf.1

MAN7 = \
	bhyve.7 \
	ipkg.7 \
	kvm.7 \
	pkg.7

MAN8 = pkg.depotd.8 pkg.depot-config.8 pkg.sysrepo.8

# These translations predate the English mdoc conversion.
L10N_MAN1 = \
	pkg.1 \
	pkgdepend.1 \
	pkgdiff.1 \
	pkgfmt.1 \
	pkglint.1 \
	pkgmerge.1 \
	pkgmogrify.1 \
	pkgrecv.1 \
	pkgrepo.1 \
	pkgsend.1 \
	pkgsign.1
L10N_MAN7 = pkg.7
L10N_MAN8 = pkg.depotd.8 pkg.sysrepo.8

MANDIRS = $(MAN1DIR) $(MAN7DIR) $(MAN8DIR) \
	$(JA_MAN1DIR) $(JA_MAN7DIR) $(JA_MAN8DIR) \
	$(ZH_MAN1DIR) $(ZH_MAN7DIR) $(ZH_MAN8DIR)

all:

install: \
	$(MANDIRS) \
	$(MAN1:%=$(MAN1DIR)/%) \
	$(MAN7:%=$(MAN7DIR)/%) \
	$(MAN8:%=$(MAN8DIR)/%) \
	$(L10N_MAN1:%=$(JA_MAN1DIR)/%) \
	$(L10N_MAN7:%=$(JA_MAN7DIR)/%) \
	$(L10N_MAN8:%=$(JA_MAN8DIR)/%) \
	$(L10N_MAN1:%=$(ZH_MAN1DIR)/%) \
	$(L10N_MAN7:%=$(ZH_MAN7DIR)/%) \
	$(L10N_MAN8:%=$(ZH_MAN8DIR)/%)

check:
	-mandoc -T lint $(MAN1) $(MAN7) $(MAN8) 2>&1 | \
		egrep -v '(outdated mandoc.db|referenced manual not found)'

clean clobber:

$(MANDIRS):
	$(MKDIR) $@

$(MAN1DIR)/% $(MAN7DIR)/% $(MAN8DIR)/%: %
	$(RM) $@; $(INSTALL) -f $(@D) -m 0444 $<

$(JA_MAN1DIR)/% $(JA_MAN7DIR)/% $(JA_MAN8DIR)/%: ja_JP/%
	$(RM) $@; $(INSTALL) -f $(@D) -m 0444 $<

$(ZH_MAN1DIR)/% $(ZH_MAN7DIR)/% $(ZH_MAN8DIR)/%: zh_CN/%
	$(RM) $@; $(INSTALL) -f $(@D) -m 0444 $<
