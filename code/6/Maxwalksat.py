import sys
from Schaffer import *
from Osyczka2 import *
from Kursawe import *
sys.dont_write_bytecode = True
epsilon = 0.001

class Maxwalksat(object):
    def mws(self, model, max_tries=25, max_changes=25, p=0.5):
        """
        MaxWalkSat Optimization method
        """
        best = model.any()
        def change_decision(point, c):
            """
            Randomly change a point and return the point if valid
            """
            newpoint = point.clone()
            while True:
                newpoint.decisions = point.decisions
                newpoint.decisions[int(c.name[1]) - 1] = random.randint(int(c.low), int(c.high))
                if model.is_valid(model, newpoint):
                    model.evaluate(model, newpoint)
                    model.points.append(newpoint)
                    say('!')
                else:
                    say('.')
                return newpoint

        def update_best(point, best):
            if point.energy > best.energy:
                say('+')
                return point
            return best

        def maximize_decision_score(point, c):
            mypoint = point.clone()
            bestpoint = point
            id = int(c.name[1]) - 1
            for val in xrange(int(math.ceil(c.low)), int(math.floor(c.high))):
                mypoint.decisions[id] = val
                if model.is_valid(model, mypoint):
                    if mypoint.energy > bestpoint.energy:
                        bestpoint = mypoint
            print_char = ',' if bestpoint.energy is point.energy else '|'
            say(print_char)
            return bestpoint

        for i in xrange(max_tries):
            anymodel = model.any()
            say(format(best.energy, '12d'))
            say(format(anymodel.energy, '12d'))
            say('')
            best = update_best(anymodel, best)
            for _ in xrange(max_changes):
                randomchoice = random.choice(model.decisions)
                if p < random.random():
                    anymodel = change_decision(anymodel, randomchoice)
                    best = update_best(anymodel, best)
                else:
                    anymodel = maximize_decision_score(anymodel, randomchoice)
                    best = update_best(anymodel, best)
            print ""
        return best
