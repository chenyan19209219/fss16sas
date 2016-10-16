from __future__ import division, print_function
import sys
import math
import random

Decision_bounds = [[0,10],[0,10],[1,5],[0,6],[1,5],[0,10]]

Max_tries = 20
Max_changes = 50

def say(x):
    sys.stdout.write(str(x))
    sys.stdout.flush()

#here we are changing all the decisions
def random_assignment():
    solution = [-1,-1,-1,-1,-1,-1]
    while True:
        for i in xrange(len(Decision_bounds)):
            dec = Decision_bounds[i]
            solution[i] = random.randint(dec[0],dec[1])
        if(check_constraints(solution)):
            return solution

def local_search(soln):
    solution = soln[:]
    while True:
        i = random.randint(0,5)
        dec = Decision_bounds[i]
        solution[i] = random.randint(dec[0],dec[1])
        if(check_constraints(solution) and score(solution)<score(soln)):
            return solution
        solution = soln[:]

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
    f1 = -25*(soln[0]-2)**2 + (soln[1]-2)**2 + (((soln[2]-1)**2)*(soln[3]-4))**2 + (soln[4]-1)**2
    f2 = soln[0]**2 + soln[1]**2 + soln[2]**2 + soln[3]**2 + soln[4]**2 + soln[5]**2
    return (f1 + f2)


def mws():
    best_solution = random_assignment()
    for i in xrange(Max_tries):
        current_solution = random_assignment()
        for j in xrange(Max_changes):
            if (score(current_solution) < score(best_solution)):
                say("!")
                best_solution = current_solution[:]

            if (0.5 < random.random()):
                prev_solution = current_solution[:]
                current_solution = random_assignment()
            else:
                prev_solution = current_solution[:]
                current_solution = local_search(current_solution)

            if (score(current_solution) < score(best_solution)):
                best_solution = current_solution[:]
                say("!")

            if (score(current_solution) < score(prev_solution)):
                say("+")
            else:
                say(".")

        print(", ", round(score(best_solution), 5))

    print("#iterations:", Max_tries)
    print("best solution:",  best_solution)
    print("best score:", score(best_solution))

mws()
