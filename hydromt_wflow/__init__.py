"""hydroMT plugin for wflow models."""

from os.path import join, dirname, abspath

__version__ = "0.3.1.dev0"

try:
    import pcraster as pcr

    HAS_PCRASTER = True
except ImportError:
    HAS_PCRASTER = False

DATADIR = join(dirname(abspath(__file__)), "data")

from .wflow import *
from .wflow_sediment import *
from .utils import *
