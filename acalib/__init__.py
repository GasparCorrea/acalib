from . import core
from .core import *
from . import algorithms

import warnings
from astropy.utils.exceptions import AstropyWarning
warnings.simplefilter('ignore', category=AstropyWarning)
warnings.filterwarnings('ignore', category=UserWarning, append=True)

#from __future__ import absolute_import, print_function

#__all__ = []	

#from . import core
#from .core import *

#__all__.extend(core.__all__)
