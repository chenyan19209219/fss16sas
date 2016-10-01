from __future__ import division
import random
import math
import sys

def say(x):
  sys.stdout.write(str(x)); sys.stdout.flush()

def neighbour(s):
    while True:
        step = 5
        xn = s + random.randint(-1*step, step)
        if xn > -(10**5) and xn < (10**5):
            return xn

def P(old, new, ratio):
    #say(math.exp((old-new)/ratio))
    #say(math.exp((old-new)/ratio))
    #print "\n"
    return math.exp((old-new)/ratio)


def Energy(x):
    f1 = x**2
    f2 = (x-2)**2
    min_x = -(10**5)
    max_x = (10**5)
    e = float((f1+f2)-min_x)/float(max_x - min_x)
    return e

def randomNeighbour():
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


sa(random.randint(int(pow(-10,5)),int(pow(10,5)),))
