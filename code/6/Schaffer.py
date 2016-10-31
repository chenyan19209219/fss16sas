import sys
from Problem import *

class Schaffer(Problem):
    def __init__(self):
        names = ['x']
        lows =[-10**5]
        high =[10**5]
        decisions = [Decision(n,l,h) for n,l,h in zip(names,lows,highs)]
        objectives = [Objective("f1",True), Objective("f2", True)]
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(point):
        def minimize(i):
            if self.objectives[i].do_minimize:
                return 1
            return -1
        f1 = point.decisions[0]**2
        f2 = (point.decisions[0]-2)**2
        point.objectives = [f1,f2]
        point.energy = int(f1 * minimize(0) + f2 * minimize(1))
        return point.objectives

    @staticmethod
    def is_valid(point):
        x = point.decisions[0]
        if x >= lows[0] and x <= highs[0]:
            return True
        return False
