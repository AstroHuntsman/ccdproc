# Autogenerated by Astropy-affiliated package ccdproc's setup.py on 2013-08-21 19:04:27.314123

from astropy.version_helpers import update_git_devstr, get_git_devstr

_last_generated_version = '0.1.dev'

version = update_git_devstr(_last_generated_version)
githash = get_git_devstr(sha=True, show_warning=False)

major = 0
minor = 1
bugfix = 0

release = False
debug = False

try:
    from astropy.utils._compiler import compiler
except ImportError:
    compiler = "unknown"

try:
    from astropy.cython_version import cython_version
except ImportError:
    cython_version = "unknown"