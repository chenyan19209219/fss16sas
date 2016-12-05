from __future__ import division
from DTLZ import *
import random
import math
import sys

class DE(object):


    def de(self, model,front, repeats     = 100,  # number of repeats
           np      = 100,  # number of candidates
           f       = 0.75, # extrapolate amount
           cf      = 0.3,  # prob of cross-over
           epsilon = 0.01):

        min_obj = [sys.maxint,sys.maxint]
        max_obj = [-sys.maxint-1,-sys.maxint-1]

        s = model.any()                     #generating a random candidate
        #e = Energy(s)                      # Initial state, energy.
        sb = s
        frontier= [ ]
        first_era =[ ]
        current_era = [ ]
        previous_era = [ ]
        output = [ ]
        k=0
        no_of_lives = 5


        print "---------------------------------------------------------------"
        print front

        def bdom(one, two):
            """
            Return if one dominates two
            """
            objs_one = one.objectives
            objs_two = two.objectives
            dominates = False
            # TODO 9: Return True/False based on the definition
            # of bdom above.
            for i in xrange(len(objs_two)):
                if(objs_one[i]>objs_two[i]):
                    return False
                if(objs_one[i]<objs_two[i]):
                    dominates = True
            return dominates


        def early_term(s,prev,curr):
            if prev == [ ]:
                return 5
            bettered = False
            for each_obj in range(len(s.objectives)):
                prev_lst = [ ]
                curr_lst = [ ]
                for each_can in prev:
                    prev_lst.append(each_can.objectives[each_obj])

                for each_can in curr:
                    curr_lst.append(each_can.objectives[each_obj])

                prev_mean = sum(prev_lst)/len(prev)
                curr_mean = sum(curr_lst)/len(curr)

                if prev_mean-curr_mean > 0.01*prev_mean:
                    bettered = True
            if bettered == True:
                return 5
            else:
                return -1


        def threeOthers(lst, avoid):
            def oneOther():
                x = avoid
                while 1:                                            #limit later if needed
                    index = random.randint(0,len(frontier)-1)
                    if index not in seen_pos:
                        seen_pos.append(index)
                        return frontier[index]
    # -----------------------
            seen_pos = [i for i,x in enumerate(frontier) if x == avoid] #enumerate will give index that needs to be avoided
            this = oneOther()
            that = oneOther()
            theOtherThing = oneOther()
            return this, that, theOtherThing

        # generating 100(np) candidates and appending to frontier
        for i in range(np):
            candidate = model.createPoint(front[i])
            f1,f2 = candidate.objectives[:]
            if f1 < min_obj[0]:
                min_obj[0] = f1
            if f2 < min_obj[1]:
                min_obj[1] = f2
            if f1 > max_obj[0]:
                max_obj[0] = f1
            if f2 > max_obj[1]:
                max_obj[1] = f2

            frontier.append(candidate)

        for _ in range(repeats):
            new_frontier = [ ]
            for one in frontier:
                if no_of_lives < 1:
                    break
                while 1:
                    two,three,four = threeOthers(frontier,one)
                    ran = random.randint(0,len(one.decisions)-1)
                    sn = model.any()                    #new candidate
                    for i in range(len(one.decisions)):
                        if random.random() < cf or i == ran:
                            sn.decisions[i] = two.decisions[i] + f * (three.decisions[i]-four.decisions[i])
                        else:
                            sn.decisions[i]=one.decisions[i]

                    if model.is_valid(model,sn):
                        break
                #wanna use bdom ?
                if bdom(sn,sb):                       #   Is this a new best? or
                    sb = sn
                    output.append("!")
                    #say("!")

                if bdom(sn,one) :                     # Should we jump to better?
                    output.append("+")
                    #say("+")

                else:
                    output.append(".")
                    #say(".")
                new_frontier.append(sn)
                current_era.append(sn)
                #print "len: ",len(current_era)
                #print "flen:", len(front)
                k=k+1
                if k%len(front) == 0:
                    #print "inside k : ",k
                    if previous_era == [ ]:
                        first_era = current_era

                    no_of_lives = no_of_lives + early_term(sn,previous_era,current_era)  # yet to implement type 2
                    #print len(previous_era)
                    previous_era = current_era[:]
                    current_era = [ ]
                    #print current_era
                    output = [ ]

        print sb
        #print first_era
        return first_era,previous_era
