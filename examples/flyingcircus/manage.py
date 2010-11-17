#!/usr/bin/env python
import sys
import os

from djangoconfig import setup_environment

try:
    setup_environment(__file__)
except KeyboardInterrupt:
    print ""
    print "Exiting script."
    sys.exit(0)

import settings
from django.core import management

if __name__ == "__main__":
    management.execute_manager(settings)
