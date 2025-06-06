# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
from contextlib import suppress

from django.conf import settings

with suppress(Exception):
    from django.utils.deprecation import MiddlewareMixin

sys.path.append(settings.CUCKOO_PATH)

from lib.cuckoo.common.constants import CUCKOO_VERSION


class CuckooHeaders(MiddlewareMixin):
    """Set Cuckoo custom response headers."""

    def __init__(self, get_response):
        self.get_response = get_response
        self._is_coroutine = False
        self.async_mode = False

    def process_response(self, request, response):
        response["Server"] = "Machete Server"
        response["X-Cuckoo-Version"] = CUCKOO_VERSION
        response["X-Content-Type-Options"] = "nosniff"
        response["X-Frame-Options"] = "DENY"
        response["X-XSS-Protection"] = "1; mode=block"
        response["Pragma"] = "no-cache"
        response["Cache-Control"] = "no-cache"
        response["Expires"] = "0"
        response["Permissions-Policy"] = (
            "accelerometer=(); autoplay=(); camera=(); encrypted-media=(); fullscreen=(); geolocation=(); gyroscope=(); magnetometer=(); microphone=(); midi=(); payment=(); picture-in-picture=(); sync-xhr=(); usb=();"
        )
        return response
