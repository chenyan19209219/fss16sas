from __future__ import division
from Schaffer import *
import random
import math
import sys

class SA(O):
    def sa(self, model, pt, kmax=1000, emax=625):
        def set_min_or_max_energy(n=300):
            random_pt = model.any()
            max_e = random_pt.energy
            min_e = max_e
            for _ in xrange(n):
                random_pt = model.any()
                if random_pt.energy > max_e:
                    max_e = random_pt.energy
                if random_pt.energy < min_e:
                    min_e = random_pt.energy
            return max_e,min_e

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


        def P(old, new, ratio, emax):
            #say(math.exp((old-new)/ratio))
            #say(math.exp((old-new)/ratio))
            #print "\n"
            if ratio is 0:
                ratio = 0.001
            var = float(new - old) / math.fabs(emax) / ratio
            return math.exp(var)

        def neighbour(point,retries = 100):
            p = point.clone()
            while retries:
                decision = random.randint(0, len(p.decisions) - 1)
                p.decisions[decision] = random.uniform(int(model.decisions[decision].low),
                                                       int(model.decisions[decision].high))
                if model.is_valid(model, p):
                    model.evaluate(model, p)
                    model.points.append(p)
                    return p
                else:
                    p.decisions = point.decisions
                    retries -= 1
            print "here"
            return point

        def Energy(p):
            f1 = model.p.decisions[0]**2
            f2 = (model.p.decisions[0]-2)**2
            e = float((f1+f2)-model.lows[0])/float(model.highs[0] - models.lows[0])
            return e

        def any_point():
            while True:
                x=random.randint(-(10**5),(10**5))
                if x>-(10**5) and x<(10**5):
                    return x

        #def normalize(current, emax,emin):
        #    normalized_energy = []


        s = model.createPoint(pt)
        first = s
        sb = s
        k = 1                             # Energy evaluation count.
        emax,emin = set_min_or_max_energy()
        #emax = -1
        #sb.energy = normalize(sb.objective[:],emax, emin)
        #s.energy = normalize(s.objective[:],emax, emin)
        current_era = []
        previous_era = []
        output = []
        no_of_lives = 5
        while (k < kmax):         # While time remains & not good enough:
            sn = neighbour(s)                  #   Pick some neighbor.
            #en = Energy(sn)                        #   Compute its energy.
            if bdom(sn,sb):                       #   Is this a new best?
                sb = sn
                current_era.append(sn.objectives)
                #eb = en                         #     Yes, save it.
                output.append("!")
                say("!")

            if bdom(sn,s) :                     # Should we jump to better?
                s = sn
                #e = en            #    Yes!
                output.append("+")
                say("+")

            elif P(s.energy, sn.energy, k / kmax, emax) < random.random():# Should we jump to worse?
                s = sn
                #e = Energy(s)            #    Yes, change state.
                output.append("?")
                say("?")
            else:
                output.append(".")
                say(".")

            k = k + 1                        #   One more evaluation done,
            current_era.append(s.objectives[:])
            if not k % 100:
                if previous_era == [ ]:
                    first_era = current_era[:]
                no_of_lives = no_of_lives +  early_term(s, previous_era, current_era)
                previous_era = current_era[:]
                current_era = [ ]


                print ""
                print format(sb.energy, '12d'), ' ',
                print format(sn.energy, '12d'), ' ',

            #print ("best: %s emax:%s  ", sb.energy,emax)



        print_can = [ ]
        for can in sb.decisions:
         print_can.append(round(can,3))
        print "Best candidate: ", print_can
        #best_en_rounded = round(best_en,4)
        print "Corresponding objectives: " , sb.objectives
        #print "Final era ", prev_era
        #return prev_era, first_era


        return sb,first                           # Return the best solution found.
