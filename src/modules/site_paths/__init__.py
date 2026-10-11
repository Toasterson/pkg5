#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#

#
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.
# Copyright 2022 OmniOS Community Edition (OmniOSce) Association.
#

"""Exclude system and user site-packages on Solaris during command startup.

OpenIndiana uses the interpreter's vendor-packages directory for pkg and its
system dependencies. Other platforms retain their normal module search paths.
"""

from site import getsitepackages, getusersitepackages
import sys


def strip_zip():
    sys.path = [d for d in sys.path if not d.endswith(".zip")]


def strip_site():
    strip = getsitepackages()
    strip.append(getusersitepackages())
    sys.path = [d for d in sys.path if d not in strip]


def init():
    if sys.platform == "sunos5":
        strip_site()


# Vim hints
# vim:ts=4:sw=4:et:fdm=marker
