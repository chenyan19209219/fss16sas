import random
import math
import sys
import os
from global_variables import *

from hypervolume_runner import HyperVolume_wrapper
from loss import *
pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class GA(object):
    def __init__(self, model):
        self.model = model
        self.emin = [sys.maxint]*model.numberOfObjs
        self.emax = [-sys.maxint]*model.numberOfObjs
        self.n=5
        self.hi=[300, 500, 0.99, 0.09, 0.9]
        self.lo=[100, 100, 0.50, 0.01, 0.4]
        self.name="GA"
        self.lifes=5
        self.threshold =0

    def candidates(self,i,direction,old):
        if (direction==True):
            while True:
                can= old
                val=self.generate_decision(i)
                can[i]=val
                if (self.is_valid(can)):
                    return can
        else :
            new = self.dec()
        return new

    def generate_decision(self,i):
        #print i
        if (i==0) or (i==1):
            a=int(self.lo[i] + r()*(self.hi[i] - self.lo[i]))
        else :
            a= self.lo[i] + r()*(self.hi[i] - self.lo[i])
        return a

    def dec(self):
        while True:
            can= []
            for i in range(self.n):
                val=self.generate_decision(i)
                can.append(val)
            if (self.is_valid(can)):
                    return can

    def neighbour(self,point):
        i=random.randrange(0,4,1)
        value= self.candidates(i,True,point)
        return value


    def is_valid(self,can):
            flag=True
            return flag


    def bdom(self,can1,can2):
        #print can1,can2
        can1_obj=self.model.objectives(can1)
        can2_obj=self.model.objectives(can2)
        #print(can2_obj,can1_obj)
        if can1_obj==can2_obj:
            return False
        for i in xrange(self.model.numberOfObjs):
            if (can2_obj[i]<can1_obj[i]):
                return False
        return True

    def checkBestEnergy(self,population_frontier,model):
        best_sol=population_frontier[0]
        best_energy=model.Energy(population_frontier[0],self.emax,self.emin)
        for i in xrange (self.population_Size):
            tmp_energy=model.Energy(population_frontier[i],self.emax,self.emin)
            if(tmp_energy < best_energy):
                best_energy=tmp_energy
                best_sol=population_frontier[i]
        return best_energy,best_sol

    def selectParents(self,population_frontier,population_Size):
        i,j=random.randrange(0,population_Size,1),random.randrange(0,population_Size,1)

        return population_frontier[i],population_frontier[j]

    def crossover(self,parent1,parent2,crossover_prob,model):
        if(crossover_prob>random.random()):
            x= random.randint(1,model.n)
            child1=parent1[0:x]+parent2[x:model.n]
            child2=parent2[0:x]+parent1[x:model.n]
            return child1,child2
        else:
            return parent1,parent2


    def mutate(self,candidate,mutate_probability,model):
        if(mutate_probability>random.random()):
            x=random.randint(0,model.n-1)
            mutated_cand=candidate
            mutated_cand[x]=model.generate_decision()
            if(model.is_valid(mutated_cand)):
                return mutated_cand
            else:
                return candidate
        return candidate

    def makeNewFrontier(self,children,population_frontier):
        new_frontier=[]
        j=0
        k=0
        for i in xrange(self.population_Size):
            if(self.frontier_distribution>random.random):
                new_frontier.append(children[j])
                j=j+1
            else:
                new_frontier.append(population_frontier[k])
                k=k+1
        return new_frontier

    def evaluateChildren(self,frontier,model):
        dict_frontier_energy={}
        sorted_frontier=[]
        dict_frontier_energy[0]=model.Energy(frontier[0],self.emax,self.emin)
        sorted_frontier.append(frontier[0])
        for i in xrange(1,self.population_Size,1):
            energy_temp=model.Energy(frontier[i],self.emax,self.emin)
            j=0
            for j in xrange(len(sorted_frontier)):
                if j in dict_frontier_energy:
                    check_energy=dict[j]
                else:
                    check_energy=model.Energy(sorted_frontier[j],self.emax,self.emin)
                    dict[j]=check_energy
                if(energy_temp>check_energy):
                    sorted_frontier.insert(j,frontier[i])
                    break
            if (j==len(sorted_frontier)):
                sorted_frontier.insert(j,frontier[i])
        return sorted_frontier

    def calculate_best_frontier(self,population_frontier):

        pop_front_best=[]
        for can1 in population_frontier:
            flag=True
            for can2 in population_frontier:
                if(can1==can2):
                    continue
                if self.bdom(can2,can1):
                    flag=False
                    break
            if flag:
                pop_front_best.append(can1)
        population_frontier_old=pop_front_best[:]
        if(len(population_frontier_old)!=100):
            i=0
            while i<(100-len(pop_front_best)):
                can=population_frontier[random.randint(0,99)]
                if(can in population_frontier_old):
                    continue
                else:
                    population_frontier_old.append(can)
                    i=i+1
        return population_frontier_old


    def GA_f(self,model,parameters):
        model=self.model

        self.emin,self.emax=self.model.norm()
        self.kmax = parameters[0]
        self.population_Size = parameters[1]
        self.p_crossover=parameters[2]
        self.p_mutation=parameters[3]
        self.frontier_distribution=parameters[4]
        #print self.emin,self.emax
        population_frontier=[self.model.candidates(0,False,0) for _ in range(self.population_Size)]

        population_frontier_old=self.calculate_best_frontier(population_frontier)
        first_frontier=population_frontier_old
        pop_front_best=population_frontier_old[:]
        #print len(population_frontier_old)
        #print population_frontier_old

        k=0
        life=0
        while k<self.kmax :
            i=0
            children=[]
            for i in xrange(self.population_Size):
                parent1,parent2= self.selectParents(population_frontier_old,len(population_frontier_old))
                child1,child2=self.crossover(parent1, parent2,self.p_crossover,model)
                child1=self.mutate(child1,self.p_mutation,model)
                child2=self.mutate(child2,self.p_mutation,model)
                if(self.bdom(child1,child2)):
                    children.append(child1)
                elif(self.bdom(child1,child2)):
                    children.append(child2)
                else:
                    x=random.randint(0,100)
                    if(x%2==0):
                        children.append(child2)
                    else:
                        children.append(child1)
            population_frontier_new=[]
            for can1 in population_frontier:
                flag=True
                for can2 in population_frontier:
                    if(can1==can2):
                        continue
                    if(self.bdom(can1,can2)):
                        flag=False
                        break
                if flag:
                    population_frontier_new.append(can1)
            tmp=[]
            new_frontier=False
            for a in population_frontier_new:
                for b in pop_front_best:
                    if self.bdom(a,b):
                        tmp.append(a)
                        pop_front_best.remove(b)
            if tmp:
                pop_front_best.extend(tmp)
                new_frontier=True
            if new_frontier:
                life=0
            else:
                life=life+1
            if(life==self.lifes):
                break

            population_frontier=children
            population_frontier_old=population_frontier_new

            k=k+1
       # print population_frontier
        #print first_frontier
        x=loss(population_frontier[0],first_frontier[0])
        global_variable.pop_front_best=pop_front_best
        '''name='Pareto_Fronts/pareto.txt'
        f=open(name,'w')
        i=0
        for i in xrange(len(pop_front_best)):
            k=0
            for j in (self.model.objectives(pop_front_best[i])):
                j=(j - self.emin[k]) / (self.emax[k]- self.emin[k])
                k+=1
                s=str(j)
                f.write(s)
                f.write(" ")
            f.write("\n")
        f.close();

       # hypervol=HyperVolume_wrapper()
        os.remove('./Pareto_Fronts/pareto.txt')'''
        #print hypervol
        return x
