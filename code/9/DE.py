
import random
import math
import sys
from hypervolume_runner import HyperVolume_wrapper

import Model

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

from GA import *
from sk import *
from global_variables import *
from loss import *

from hypervolume_runner import HyperVolume_wrapper

class de(object):
    def __init__(self, model,submodel,no_of_obj,no_of_decs):
        self.model = model
        self.submodel=submodel
        self.kmax = 10
        self.max_changes = 20
        self.lifes=5
        self.threshold =0
        self.p=0.5
        self.f=0.75
        self.crossover=0.3
        self.epsilon=0.01
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.no_of_obj=no_of_obj
        self.no_of_decs=no_of_decs
        self.de_f()

        self.name='de'

    def de_f(self):

        submodel=self.submodel(self.no_of_obj,self.no_of_decs)

        model=self.model(submodel)

        re = ""
        frontier=[model.candidates(0,False,0) for _ in range(self.max_changes)]

        best_energy=model.GA_f(submodel,frontier[0])
        best_solution=frontier[0]
        k=0
        d_energy=dict()
        count_dict=0
        list_energy=[]

        prev_energy=[0 for _ in range(21)]

        a12_small=0.56
        prev_energy=[0 for _ in range(21)]
        while k<self.kmax :
            re=""

            if(best_energy==self.threshold):
                break

            for i, solution in enumerate(frontier):
                seen = []
                while len(seen) < 3:
                    rand_index = random.randint(0, 19)
                    if rand_index == i:
                        continue
                    if rand_index not in seen:
                        seen.append(rand_index)
                mutation=frontier[seen[0]]

                current_energy=model.GA_f(self.submodel,solution)
                append=" ."
                if(self.crossover < random.random()):
                    if((model.GA_f(self.submodel,frontier[0]))>current_energy):
                        current_energy=model.GA_f(self.submodel,mutation)
                        frontier[i] = mutation
                        append = " +"

                else:
                    mutation=[]
                    for j in xrange(model.n):
                        l=model.lo[j]
                        m=model.hi[j]
                        inter = (frontier[seen[0]][j] + self.f* (frontier[seen[1]][j] - frontier[seen[2]][j]))
                        if inter >= l and inter <= m:
                            if (j==0)or (j==1):
                                inter=int(inter)
                            mutation.append(inter)
                        else:
                            mutation.append(frontier[seen[random.randint(0, 2)]][j])


                    if(model.is_valid(mutation) and model.GA_f(self.submodel,mutation)>current_energy) :
                        frontier[i]=mutation
                        current_energy=model.GA_f(self.submodel,mutation)
                        append=" +"

                if(current_energy>best_energy  and current_energy>=self.threshold):
                    append=" ?"
                    best_energy=current_energy
                    best_solution=frontier[i]
                list_energy.append(current_energy)
                re=re+append
                k+=1
                global_variable.best_energy= best_energy
                if (k>0):
                    if (k==25):
                                first_energy=prev_energy
                    if k % 25 is 0:
                        #print k,best_energy,re
                        re = ""

        pop_front_best=global_variable.pop_front_best

        name='Pareto_Fronts/pareto.txt'
        f=open(name,'w')
        i=0
        for i in xrange(len(pop_front_best)):
            k=0
            for j in (submodel.objectives(pop_front_best[i])):
                j=(j - model.emin[k]) / (model.emax[k]- model.emin[k])
                k+=1
                s=str(j)
                f.write(s)
                f.write(" ")
            f.write("\n")
        f.close();
        print best_solution

        hypervol=HyperVolume_wrapper()
        global_variable.best_energy= hypervol
        os.remove('./Pareto_Fronts/pareto.txt')
        ##print("\nBest Solution : " + str(best_solution))
        ##print("Best Energy : " + str((model.GA_f(self.submodel,best_solution))))
