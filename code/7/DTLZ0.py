import sys
from Problem import *

class DTLZ(Problem):
    def __init__(self):
        names = ['x1', 'x2', 'x3','x4','x5','x6','x7','x8','x9','x10']
        lows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        highs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.points = []
        decisions = [Decision(n, l, h) for n, l, h in zip(names, lows, highs)]
        objectives = [Objective("f1", True), Objective("f2", True)]
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(self, point):
        def minimize(i):
            return -1 if self.objectives[i].do_minimize else 1
        x = point.decisions[:]
        f1, f2 = 0, 0
        f1 = x[0]
        f2 = (1+self.g(self,x))*self.h(self,f1,self.g(self,x),2)
        point.objectives = [f1, f2]
        #print point.objectives
        point.energy = int(f1 * minimize(0) + f2 * minimize(1))
        return point.objectives

    @staticmethod
    def g(self,x):
        s = sum(x)
        return 1+ ((9/len(x))*s)

    @staticmethod
    def h(self,f,g,M):
        angle = 3*math.pi*f
        return M - ((f/(1+g))* (1+math.sin(angle)))

    @staticmethod
    def is_valid(self, point):
        return True


    def any(self, retries=500):
        for _ in xrange(retries):
            point = Point([random.uniform(int(d.low), d.high) for d in self.decisions])
            if self.is_valid(self, point):
                self.evaluate(self, point)
                self.points.append(point)
                #print point.energy
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % retries)
