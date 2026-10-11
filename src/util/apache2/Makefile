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

include ../../Makefile.com

ROOTDEPOT = $(ROOT)/etc/pkg/depot
ROOTSYSREPO = $(ROOT)/etc/pkg/sysrepo
ROOTWEB = $(ROOTUSRSHARE)/lib/pkg/web
ROOTDEPOTLOG = $(ROOT)/var/log/pkg/depot
ROOTSYSREPOLOG = $(ROOT)/var/log/pkg/sysrepo

DEPOT = depot.conf.mako depot_httpd.conf.mako depot_httpd_ssl_protocol.conf depot_index.py
SYSREPO = sysrepo_httpd.conf.mako sysrepo_p5p.py sysrepo_publisher_response.mako
LOGS = access_log error_log rewrite.log
DIRS = $(ROOTDEPOT) $(ROOTSYSREPO) $(ROOTWEB) $(ROOTDEPOTLOG) $(ROOTSYSREPOLOG)

all check clean clobber:

install: $(DIRS) $(DEPOT:%=$(ROOTDEPOT)/%) $(SYSREPO:%=$(ROOTSYSREPO)/%) \
	$(ROOTWEB)/repos.shtml $(LOGS:%=$(ROOTDEPOTLOG)/%) $(LOGS:%=$(ROOTSYSREPOLOG)/%)

$(DIRS):
	$(MKDIR) $@

$(ROOTDEPOT)/%: depot/%
	$(RM) $@; $(INSTALL) -f $(@D) -m 0444 $<

$(ROOTSYSREPO)/%: sysrepo/%
	$(RM) $@; $(INSTALL) -f $(@D) -m 0444 $<

$(ROOTWEB)/repos.shtml: depot/repos.shtml
	$(RM) $@; $(INSTALL) -f $(@D) -m 0444 $<

$(ROOTDEPOTLOG)/%: depot/logs/%
	$(RM) $@; $(INSTALL) -f $(@D) -m 0644 $<

$(ROOTSYSREPOLOG)/%: sysrepo/logs/%
	$(RM) $@; $(INSTALL) -f $(@D) -m 0644 $<
