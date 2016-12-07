import math 
import random 
import sys

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class Model(object):
    
    def __init__(self):
        self.emin = sys.maxint
        self.emax = -sys.maxint