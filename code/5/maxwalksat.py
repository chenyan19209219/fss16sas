import sys
import math
import random
Decision_bounds = [[0,10],[0,10],[1,5],[0,6],[1,5],[0,10]]

Max_tries = 20
Max_changes = 50

def say(x):
    sys.stdout.write(str(x))
    sys.stdout.flush()

def random_assignment():
    solution[]
    while True:
        for i in range(len(Decision_bounds)):
            dec = Decision_bounds[i]
            solution[i] = random.randint(dec[0],dec[1])
        if(check_constraints(solution)):
            return solution



def check_constraints(soln):
    if(soln[0]+soln[1]-2 < 0):
        return False
    if(6-soln[0]-soln[1] < 0):
        return False
    if(2-soln[1]+soln[1] < 0):
        return False
    if(2-soln[0]+3*soln[1] < 0):
        return False
    if(4-(soln[2]-3)**2-soln[3] <0):
        return False
    if((soln[4]-3)**3 + soln[5] - 4 <0):
        return False

    return True

def score(soln):
    f1 = -25*(soln[0]-2)**2 + (soln[1]-2)**2 + ((soln[2]-1)**2)*(soln[3]-4)**2 + (soln[4]-1)**2
    f2 = soln[0]**2 + soln[1]**2 + soln[2]**2 + soln[3]**2 + soln[4]**2 + soln[5]**2

    return f1 + f2


def mws():
    for i in xrange(Max_tries):
        best_solution = random_assignment()
        for j in xrange(Max_changes):
            new_solution = random_assignment()
            if(score(new_solution) < score(best_solution)):
                say("!")
                best_solution = new_solution[:]
            else





FOR i = 1 to Max_tries DO
  solution = random assignment
  FOR j =1 to Max_changes DO
    IF  score(solution) > threshold
        THEN  RETURN solution
    FI
    c = random part of solution
    IF    p < random()
    THEN  change a random setting in c
    ELSE  change setting in c that maximizes score(solution)
    FI
RETURN failure, best solution found
