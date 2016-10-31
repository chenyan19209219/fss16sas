from __future__ import print_function, division
from math import *
import random
import sys

# TODO 1: Enter your unity ID here
__author__ = "smshah4"

class O:
    """
    Basic Class which
        - Helps dynamic updates
        - Pretty Prints
    """
    def __init__(self, **kwargs):
        self.has().update(**kwargs)
    def has(self):
        return self.__dict__
    def update(self, **kwargs):
        self.has().update(kwargs)
        return self
    def __repr__(self):
        show = [':%s %s' % (k, self.has()[k])
                for k in sorted(self.has().keys())
                if k[0] is not "_"]
        txt = ' '.join(show)
        if len(txt) > 60:
            show = map(lambda x: '\t' + x + '\n', show)
        return '{' + ' '.join(show) + '}'

print("Unity ID: ", __author__)

# Few Utility functions
def say(*lst):
    """
    Print whithout going to new line
    """
    print(*lst, end="")
    sys.stdout.flush()

def random_value(low, high, decimals=2):
    """
    Generate a random number between low and high.
    decimals incidicate number of decimal places
    """
    return round(random.uniform(low, high),decimals)

def gt(a, b): return a > b

def lt(a, b): return a < b

def shuffle(lst):
    """
    Shuffle a list
    """
    random.shuffle(lst)
    return lst

class Decision(O):
    """
    Class indicating Decision of a problem
    """
    def __init__(self, name, low, high):
        """
        @param name: Name of the decision
        @param low: minimum value
        @param high: maximum value
        """
        O.__init__(self, name=name, low=low, high=high)

class Objective(O):
    """
    Class indicating Objective of a problem
    """
    def __init__(self, name, do_minimize=True, low=0, high=1):
        """
        @param name: Name of the objective
        @param do_minimize: Flag indicating if objective has to be minimized or maximized
        """
        O.__init__(self, name=name, do_minimize=do_minimize, low=low, high=high)

    def normalize(self, val):
        return (val - self.low)/(self.high - self.low)

class Point(O):
    """
    Represents a member of the population
    """
    def __init__(self, decisions):
        O.__init__(self)
        self.decisions = decisions
        self.objectives = None
        self.energy = None

    def __hash__(self):
        return hash(tuple(self.decisions))

    def __eq__(self, other):
        return self.decisions == other.decisions

    def clone(self):
        new = Point(self.decisions[:])
        new.objectives = self.objectives[:]
        new.energy = self.energy
        return new

class Problem(O):
    """
    Class representing the cone problem.
    """
    def __init__(self, decisions, objectives):
        """
        Initialize Problem.
        :param decisions -  Metadata for Decisions
        :param objectives - Metadata for Objectives
        """
        O.__init__(self)
        self.decisions = decisions
        self.objectives = objectives

    @staticmethod
    def evaluate(point):
        assert False
        return point.objectives

    @staticmethod
    def is_valid(point):
        return True

    #might have to change this
    def generate_one(self, retries = 20):
        for _ in xrange(retries):
            point = Point([random_value(d.low, d.high) for d in self.decisions])
            if self.is_valid(point):
                self.evaluate(self, point)
                self.points.append(point)
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % 20)
