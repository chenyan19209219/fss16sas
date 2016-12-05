from Schaffer import *
from Osyczka2 import *
from Kursawe import *
from DTLZ import *
from SA import *
from Maxwalksat import *
from DE import *

import statistics
import sys
from performance import make_reference,igd,report
from sk import rdivDemo

#from helper.sk import *

sys.dont_write_bytecode = True
repeats = 10
pop_size = 100
sa = SA()
de = DE()
mws = Maxwalksat()
IGD = []

p = DTLZ()
#baseline = []
#for x in xrange(pop_size):

baseline = [[DTLZ().any().decisions for _ in range(pop_size)] for _ in xrange(repeats)]    #WE run de to get baseline population !! !

igd_ss = [ ]
igd0 =[ ]
igd1 =[ ]
igd2 = [ ]
final_era = [[ ], [ ], [ ]]
zero_era = [[ ], [ ], [ ]]
data = [['sa'],['mws'],['de']]
def type3(final_era, zero_era):
    i=0
    for final_opt, zero_opt in zip(final_era,zero_era):
        losses = [ ]
        length = min(len(final_opt), len(zero_opt))
        for each in range(length):
            final_cand = final_opt[each]
            zero_cand = zero_opt[each]
            num = (final_cand.objectives[1]-zero_cand.objectives[1])**2 + (final_cand.objectives[0]-zero_cand.objectives[0])**2
            den = 2
            rms_dist = math.sqrt(num/den)
            #print rms_dist
            losses.append(rms_dist)
        for each in losses:
            data[i].append(each)
        i=i+1
    #print "_____________________)))))))))))))))))))______________________________"
    #print data

    rdivDemo(data)


for model in [DTLZ]:
    for reps in xrange(repeats):
        final = []                                                       #array of array of final pop
        for optimizer in [de.de]:
            print ""
            sys.stdout.flush()
            #print(optimizer)
            #print(model)
            first,last = optimizer(model(), baseline[0],100,pop_size)
            for each in xrange(len(last)):
                final_era[0].append(last[each])
            for each in xrange(len(first)):
                zero_era[0].append(first[each])


            frontier1 = []
            for i in range(pop_size):
                frontier1.append(last[i].objectives)
            final.append(frontier1)
            print final

        last = []
        for psize in xrange(pop_size):

            for optimizer in [sa.sa]:
                print ""
                sys.stdout.flush()
                #print(optimizer)
                #print(model)
                best,first = optimizer(model(), baseline[0][psize])
                zero_era[1].append(first)
                final_era[1].append(best)
                last.append(best.objectives)
                #print "last"
                #print last
        final.append(last)

        last = []
        print "mws"
        for psize in xrange(pop_size):

            for optimizer in [mws.mws]:
                print ""
                sys.stdout.flush()
                #print(optimizer)
                #print(model)
                best,first = optimizer(model(), baseline[0][psize])
                zero_era[2].append(first)
                final_era[2].append(best)
                last.append(best.objectives)
                #print "last"
            #print last
        final.append(last)

        reference = make_reference(model(),final[0],final[1],final[2])
        #print reference
        #print len(reference)
        #i0 = igd(final[0],reference)
        igd0.append(igd(final[0],reference))
        igd1.append(igd(final[1],reference))
        igd2.append(igd(final[2],reference))

#IGD for DE , SA , MWS
igd0.sort()
igd1.sort()
igd2.sort()

print "final !!! "
print final



#report(model(),final,igd)
#

for j in xrange(repeats):
    igd0[j] = igd0[j]*100
    igd1[j] = igd1[j]*100
    igd2[j] = igd2[j]*100
    reference[j] = reference[j]*100





print "ref:"
print reference
print "de : igds"

print igd0
print "sa : igds"
print igd1
print "mws: igds"
print igd2

igd0 = ['de'] + igd0
igd1 = ['sa'] + igd1
igd2 = ['mws'] + igd2


igd_ss.append(igd0)
igd_ss.append(igd1)
igd_ss.append(igd2)

#print "TRUE PARETO FRONTIER"
#print reference

#print "All IGDS "


print "-----------------IGD MEDIAN--------------------------------"
print "DE: ",statistics.median(igd0)
print "SA: ", statistics.median(igd1)
print "MWS: ",statistics.median(igd2)
print "-----------------a12 and bootstrap -----------------------------"
type3(final_era,zero_era)
#rdivDemo(igd_ss)
#print "final: ",len(final[0])
#print final


# print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-"
# print final[1]
# print "**************************************************"
# #print last
# #print baseline[0]
