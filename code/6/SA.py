from __future__ import division
from Schaffer import *
import random
import math
import sys

class SA(O):
    def sa(self, model, kmax=1000, emax=625):
        def set_min_or_max_energy(n=300):
                random_pt = model.any()
                max_e = random_pt.energy
                for _ in xrange(n):
                    random_pt = model.any()
                    if random_pt.energy > max_e:
                        max_e = random_pt.energy
                return max_e

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
                p.decisions[decision] = random.randint(int(model.decisions[decision].low),
                                                       int(model.decisions[decision].high))
                if model.is_valid(model, p):
                    model.evaluate(model, p)
                    model.points.append(p)
                    return p
                else:
                    p.decisions = point.decisions
                    retries -= 1
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

        s = model.any()
        #e = Energy(s)                      # Initial state, energy.
        sb = s
        #eb = e                              # Initial "best" solution
        k = 1                             # Energy evaluation count.
        emax = set_min_or_max_energy()
        while (k < kmax and sb.energy < emax):         # While time remains & not good enough:
            sn = neighbour(s)                  #   Pick some neighbor.
            #en = Energy(sn)                        #   Compute its energy.
            if sn.energy > sb.energy:                       #   Is this a new best?
                sb = sn
                #eb = en                         #     Yes, save it.
                say("!")

            if sn.energy > s.energy :                     # Should we jump to better?
                s = sn
                #e = en            #    Yes!
                say("+")

            elif P(s.energy, sn.energy, k / kmax, emax) < random.random():# Should we jump to worse?
                s = sn
                #e = Energy(s)            #    Yes, change state.
                say("?")
            else:
                say(".")

            k = k + 1                        #   One more evaluation done,

            if not k % 25:
                print ""
                print format(sb.energy, '12d'), ' ',
                print format(sn.energy, '12d'), ' ',

        return sb                           # Return the best solution found.
