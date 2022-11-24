
"""
**Defaults for running tests.**

Adds source folder to run tests locally.
Disables logging.
"""

from os.path import join, dirname
import sys
import logging

sys.path.insert(0, join(dirname(__file__), '../src/'))

logging.disable(logging.CRITICAL)

