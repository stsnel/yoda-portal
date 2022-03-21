#!/usr/bin/env python3

__copyright__ = 'Copyright (c) 2021, Utrecht University'
__license__   = 'GPLv3, see LICENSE'

import sys
import traceback

def log_error(message, print_exception = False):
    """Writes an error message, and optionally an exception trace to the
       web server error log.
    """
    print( message, file=sys.stderr)
    if print_exception:
        traceback.print_exc()
