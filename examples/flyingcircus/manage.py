#!/usr/bin/env python
import sys
import os

# Add the "src" directory of this project to the python path.
os.sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

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
