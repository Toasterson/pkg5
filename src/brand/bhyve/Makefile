#
# This file and its contents are supplied under the terms of the
# Common Development and Distribution License ("CDDL"), version 1.0.
# You may only use this file in accordance with the terms of version
# 1.0 of the CDDL.
#
# A full copy of the text of the CDDL should have accompanied this
# source. A copy of the CDDL is also available via the Internet at
# http://www.illumos.org/license/CDDL.

#
# Copyright 2020 OmniOS Community Edition (OmniOSce) Association.
#

BRAND = bhyve
FILES = config.xml createzone firewall.ksh image.ksh init log.ksh platform.xml socat support uninstall util.ksh vars.ksh

BRANDDIR = $(ROOTBRAND)/$(BRAND)
BRANDFILES = $(FILES:%=$(BRANDDIR)/%)

include ../Makefile.com

# Rewrite the selected interpreter, including a shebang without arguments.
$(BRANDDIR)/init: $(BRANDDIR) init
	$(RM) $@
	$(SED) -e '1s/python3 /python$(PYVER) /' \
	    -e '1s/python3$$/python$(PYVER)/' init > $@
	$(CHMOD) 0755 $@
