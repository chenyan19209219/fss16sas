import sys
from Schaffer import *
from Osyczka2 import *
from Kursawe import *
sys.dont_write_bytecode = True
epsilon = 0.001

class Maxwalksat(object):
    def mws(self, model, pt,max_tries=25, max_changes=25, p=0.5):
        """
        MaxWalkSat Optimization method
        """

        #BDOM
        def bdom(one, two):
            """
            Return if one dominates two
            """
            objs_one = one.objectives[:]
            objs_two = two.objectives[:]
            dominates = False
            # TODO 9: Return True/False based on the definition
            # of bdom above.
            for a in xrange(len(objs_two)):
                if(objs_one[a]>objs_two[a]):
                    return False
                if(objs_one[a]<objs_two[a]):
                    dominates =True
            return dominates

        def early_term(s, previous_era, current_era):
            if previous_era == [ ]:
                return 5

            better = False
            for each_obj in range(len(s.objectives)):
                previous_list = [ ]
                current_list = [ ]
                for each_pt in previous_era:
                    previous_list.append(each_pt[each_obj])
                for each_pt in current_era:
                    current_list.append(each_pt[each_obj])
                previous_mean = sum(previous_list)/len(previous_era)
                current_mean = sum(current_list)/len(current_era)

                if previous_mean - current_mean > 0.01*previous_mean:
                    better = True

            if better:
                return 5
            else:
                return -1



        best = model.createPoint(pt)
        first = best
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
            #say(format(best.energy, '12d'))
            #say(format(anymodel.energy, '12d'))
            #say('')
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
        return best,first
