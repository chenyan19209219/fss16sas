from NSGA2 import *
from DTLZ import *
from performance import *

from hypervolume import *
from stats import rdivDemo as sk
#from sk import rdivDemo

#for dtlz_name, dtlz_definitions in zip(["dtlz1"], "dtlz3", "dtlz5", "dtlz7"], [DTLZ1(), DTLZ3(), DTLZ5(), DTLZ7()]):
for dtlz_name, dtlz_definitions in zip(["dtlz1","dtlz3","dtlz5","dtlz7"], [DTLZ1, DTLZ3, DTLZ5,DTLZ7]):
    for num_obj in [2, 4, 6, 8]:

        hv_stats = []
        for num_dec in [10, 20, 40]:
            for dom in [bdom,cdom]:#, "cdom"]:
                avg_vol = 0
                repeats = 20
                info_hv = [dtlz_name + " " + str(num_obj) + " " + str(num_dec) + " " + dom.__name__]
                for x in range(repeats): #repeats
                    problem = dtlz_definitions(num_obj, num_dec)
                    hypervolume = nsga2(problem,dom_func=dom)

                    info_hv.append(hypervolume)
                hv_stats.append(info_hv)
                #print hv_stats

        sk(hv_stats)
        print str(num_obj) +" Objectives done for  " + dtlz_name + " !! "
print "Done"
