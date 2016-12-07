import Model
import math
import random
from Model import *

pi  = math.pi
ee  = math.e
cos = math.cos
sqrt= math.sqrt
r   = random.random

class DTLZ1(Model):
    def __init__(self,obj,dec):
        self.candidate=[]
        self.emin =[sys.maxint]*obj
        self.emax = [-sys.maxint]*obj
        self.n=dec
        self.numberOfObjs=obj
        self.hi=1
        self.lo=0
        self.name="DTLZ1"


    def g(self,array):
        sum1=0
        for i in xrange(len(array)):
            sum1+= ((array[i]-0.5)**2 -cos(20*pi*(array[i]-0.5)))
        return 100*(self.n+sum1)


    def f(self,array,g_value):

        f1=1
        objs=[]
        for i in xrange(self.numberOfObjs):

            f1=(float)(0.5*(1+g_value))
            for j in xrange (0,self.numberOfObjs-1-i):
                f1=f1*(float)(array[j])
            f1=f1*(float)(1-(float)(array[j]))
            objs.append(f1)
        return objs

    def is_valid(self,can):
        ok_bool=True
        for i in xrange(self.n):
            ok_bool=ok_bool and (can[i]>=self.lo and can[i]<=self.hi)

        return ok_bool


    def candidates(self,i,direction,old):
        if (direction==True):
            while True:
                can= old
                val=self.generate_decision()
                can[i]=val
                if (self.is_valid(can)):
                    return can
        else :
            new = self.dec()
        return new

    def generate_decision(self):
        #print i
        return self.lo + r()*(self.hi - self.lo)

    def dec(self):
        while True:
            can= []
            for i in range(self.n):
                val=self.generate_decision()
                can.append(val)
            if (self.is_valid(can)):
                    return can


    def objectives(self,can):
        g_value=self.g(can)

        return self.f(can,g_value)

    def neighbour(self,point):
        i=random.randrange(0,self.n,1)
        value= self.candidates(i,True,point)
        return value

    def norm(self):

        for i in range(1,10000):
            var=self.candidates(0,False,0)
            k=0
            for en in self.objectives(var):
                if (en>self.emax[k]):
                    self.emax[k]=en
                if (en<self.emin[k]):
                    self.emin[k]=en
                k+=1
        return self.emin, self.emax

    def Energy(self,can,emax,emin):
        norm_energy =  ((self.objectives(can)) - emin) / (emax- emin)
        return norm_energy
