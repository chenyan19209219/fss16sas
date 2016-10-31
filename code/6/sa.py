from __future__ import division
from Schaffer import *
import random
import math
import sys

class SA(O):
    def sa(self, model, kmax=1000, emax=625):
        set_min_or_max_energy():
            rand_point = model.any()
            max_e = rand_point.energy
            for _ in xrange(n_times):
                rand_point = model.any()
                if rand_point.energy > max_e:
                    max_e = rand_point.energy
            return max_e

    def P(old, new, ratio):
        #say(math.exp((old-new)/ratio))
        #say(math.exp((old-new)/ratio))
        #print "\n"
        return math.exp((old-new)/ratio)

    def neighbour(p,retries = 100):
        point = p.clone()
        no_of_dec = len(point.decisions) - 1
        int i = 0
        while i != retries :
            dec = point.random.randint(0, no_of_dec)
            point.decisions[dec] = random.randint(int(model.decisions[dec].low), int(model.decisions[dec].high))

            if point.is_valid():
                model.evaluate(model,point)
                model.points.append(point)
                return point
            else:
                i = i+1
        return p

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

    def sa(s0):
        s = s0;
        e = Energy(s)                      # Initial state, energy.
        sb = s
        eb = e                              # Initial "best" solution
        k = 1                             # Energy evaluation count.
        kmax = 1000
        emax = -1
        while (k < kmax and e > emax):         # While time remains & not good enough:
            sn = neighbour(s)                  #   Pick some neighbor.
            en = Energy(sn)                        #   Compute its energy.
            if en < eb:                       #   Is this a new best?
                sb = sn
                eb = en                         #     Yes, save it.
                say("!")

            if en < e :                     # Should we jump to better?
                s = sn
                e = en            #    Yes!
                say("+")

            elif (P(e, en, float(k)/float(kmax)) < random.random()): # Should we jump to worse?
                s = randomNeighbour()
                e = Energy(s)            #    Yes, change state.
                say("?")
            else:
                say(".")

            k = k + 1                        #   One more evaluation done,

            if k % 50 == 0:
                print "\n",sb

        return sb                           # Return the best solution found.
