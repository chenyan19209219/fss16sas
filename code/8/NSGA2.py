from __future__ import division
from DTLZ import *
#from pom3_ga import *
from Problem import *
from hypervolume import *
import random
import math
import sys

def random_value(low, high, decimals=2):
    """
    Generate a random number between low and high.
    decimals incidicate number of decimal places
    """
    return round(random.uniform(low, high), decimals)

def bdom(problem, one, two):
    """
    Return if one dominates two
    """
    objs_one = problem.evaluate(problem,one)
    objs_two = problem.evaluate(problem,two)
    dominates = False
    # TODO 9: Return True/False based on the definition
    # of bdom above.
    for i in xrange(len(objs_two)):
        if(objs_one[i]>objs_two[i]):
            return False
        if(objs_one[i]<objs_two[i]):
            dominates = True
    return dominates


def cdom(problem, one, two):
    def expLoss(w, x1, y1, n):
        return -1 * (w * (x1 - y1) / n)

    def loss(x, y):
        losses = []
        n = min(len(x), len(y))
        for obj in range(n):
            x1, y1 = x[obj], y[obj]
            losses += [expLoss(-1, x1, y1, n)]
        return sum(losses) / n

    x = problem.evaluate(problem,one)
    y = problem.evaluate(problem,two)
    l1 = loss(x, y)
    return int(l1)


def fast_non_dominated_sort(problem,population,dom_func=bdom):
    fronts = []
    first_front = []

    for p in population:
        p.dom_set = []
        p.dom_count = 0
        for q in population:
            if(dom_func(problem,p,q)):
                p.dom_set.append(q)
            elif(bdom(problem,p,q)):
                p.dom_count+=1
        if p.dom_count==0:
            p.rank = 0
            first_front.append(p)
    fronts.append(first_front)

    curr = 0
    while(curr<len(fronts)):
        next_front = []
        for p1 in fronts[curr]:
            for p2 in p1.dom_set:
                p2.dom_count-=1
                if(p2.dom_count == 0):
                    p2.rank = curr+1
                    next_front.append(p2)
        curr+=1
        if(len(next_front)>0):
            fronts.append(next_front)
    return fronts


def reproduce(problem,population,pop_size,mutation,crossover_rate):
    children = []
    for _ in xrange(pop_size):
        mom = random.choice(population)
        dad = random.choice(population)
        while mom == dad:
            dad = random.choice(population)

        child = mutate(problem, crossover(mom,dad,crossover_rate),mutation)
        if problem.is_valid(problem,child) and child not in population + children:
            children.append(child)

    return children

def calculate_crowding_distance(problem, population):
    for point in population:
        point.dist = 0.0

    for i in xrange(len(problem.objectives)):
        population.sort(key=lambda point: point.objectives[i])              #Sort the candidates on that objective
        rge = population[-1].objectives[i] - population[0].objectives[i]
        population[0].dist = float("inf")
        population[-1].dist = float("inf")
        if rge == 0:
            continue
        for j in xrange(1,len(population)-1):
            population[j].dist += (population[j+1].objectives[i] - population[j-1].objectives[i]) / rge

def compare(a,b):
    return (a>b) - (a<b)

def crowded_comp_operator(x,y):
    if(x.rank == y.rank):
        return compare(y.dist,x.dist)
    return compare(x.rank,y.rank)


def select_parents(problem,fronts,pop_size):
    [calculate_crowding_distance(problem,front) for front in fronts]
    offspring = []
    last_front = 0
    for front in fronts:
        if((len(offspring)+ len(front)) > pop_size):
            break
        for point in front:
            offspring.append(point)
        if(fronts.index(front) < len(fronts)-1):
            last_front+=1
    remaining = pop_size - len(offspring)

    if remaining > 0 :
        fronts[last_front].sort(cmp=crowded_comp_operator)
        offspring += fronts[last_front][0:remaining]
    return offspring

def populate(problem, size):
    population = []
    # TODO 6: Create a list of points of length 'size'
    for _ in xrange(size):
        population.append(problem.any())
    return population


def crossover(mom, dad, crossover_rate=0.9):
    """
    Create a new point which contains decisions from
    the first half of mom and second half of dad
    """
    if random.random() > crossover_rate:
        return mom
    n = len(mom.decisions)
    return Point(mom.decisions[:n // 2] + dad.decisions[n // 2:])

#pop = populate(cone,5)
#crossover(pop[0],pop[1])

def mutate(problem, point, mutation_rate=0.01):
    # TODO 8: Iterate through all the decisions in the point
    # and if the probability is less than mutation rate
    # change the decision(randomly set it between its max and min).
    for i,d in enumerate(problem.decisions):
        if random.random() < mutation_rate:
            point.decisions[i] = random_value(d.low,d.high)
    return point



def fitness(problem, population, point):
    dominates = 0
    # TODO 10: Evaluate fitness of a point.
    # For this workshop define fitness of a point
    # as the number of points dominated by it.
    # For example point dominates 5 members of population,
    # then fitness of point is 5.
    for pt in population:
        if(bdom(problem,point,pt)):
            dominates = dominates+1


    return dominates

def elitism(problem, population, retain_size):
    # TODO 11: Sort the population with respect to the fitness
    # of the points and return the top 'retain_size' points of the population
    fitnesses = []
    for n in population:
        fitnesses.append((n, fitness(problem,population,n)))

    fitnesses = sorted(fitnesses, key = lambda x:x[1])

    final = []
    for p in fitnesses:
        final.append(p[0])
    #print(fitnes)
    return final[:retain_size]

#mutate(cone, point)
#print(bdom(cone,point,point1))


def ga(pop_size = 100, gens = 250):
    problem = Problem()
    population = populate(problem, pop_size)
    [problem.evaluate(point) for point in population]
    initial_population = [point.clone() for point in population]
    gen = 0
    while gen < gens:
        say(".")
        children = []
        for _ in range(pop_size):
            mom = random.choice(population)
            dad = random.choice(population)
            while (mom == dad):
                dad = random.choice(population)
            child = mutate(problem, crossover(mom, dad))
            if problem.is_valid(problem,child) and child not in population+children:
                children.append(child)
        population += children
        population = elitism(problem, population, pop_size)
        gen += 1
    print("")
    return initial_population, population

def plot_pareto(initial, final):
    initial_objs = [point.objectives for point in initial]
    final_objs = [point.objectives for point in final]
    initial_x = [i[0] for i in initial_objs]
    initial_y = [i[1] for i in initial_objs]
    final_x = [i[0] for i in final_objs]
    final_y = [i[1] for i in final_objs]
    plt.scatter(initial_x, initial_y, color='b', marker='+', label='initial')
    plt.scatter(final_x, final_y, color='r', marker='o', label='final')
    plt.title("Scatter Plot between initial and final population of GA")
    plt.ylabel("Total Surface Area(T)")
    plt.xlabel("Curved Surface Area(S)")
    plt.legend(loc=9, bbox_to_anchor=(0.5, -0.175), ncol=2)
    plt.show()

#initial, final = ga(10,20)

def hv(population, num_objectives):
    referencePoint = [11 for _ in range(num_objectives)]
    hv = InnerHyperVolume(referencePoint)

    volume = hv.compute(individual.objectives for individual in population)
    return volume


def norm_hypervol(hv, obj):
    exp = 1 if obj == 2 else obj / 2
    return hv / (122 ** exp)

def nsga2(problem = DTLZ1(), pop_size=100, gens=2, mutation=0.01, crossover_rate=0.9,  dom_func=cdom):
    #print "oksdf"
    #problem = DTLZ7()
    #print problem
    population = populate(problem, pop_size)
    #print "askdhk"
    #print population
    [problem.evaluate(problem,point) for point in population]
    initial_population = [point.clone for point in population]              #initialize Population
    fast_non_dominated_sort(problem,population,dom_func)
    children = reproduce(problem,population,pop_size,mutation,crossover_rate)
    gen = 0

    while gen < gens:
        say(".")
        union = population + children
        fronts = fast_non_dominated_sort(problem,union,dom_func)
        parents = select_parents(problem,fronts,pop_size)
        population = children
        children = reproduce(problem,parents,pop_size,mutation,crossover_rate)


        gen = gen+1
    union = population + children
    fronts = fast_non_dominated_sort(problem,union,dom_func)
    parents = select_parents(problem,fronts,pop_size)
    print("")
    hypervolume = norm_hypervol(hv(parents, len(problem.objectives)), len(problem.objectives))
    return hypervolume



# def write_results(filename, problem, population):
#     try:
#         os.mkdir('Pareto_Fronts')
#     except Exception:
#         pass
#     refresh_objectives(problem, population)
#     f = open('Pareto_Fronts/' + filename, 'w')
#     for point in population:
#         for i, obj in enumerate(point.objectives):
#             f.write(str(problem.objectives[i].normalize(obj)) + " ")
#         f.write("\n")
#     f.close()
#
#
# # this will run hypervolume on all of the previously saved results in the Pareto Fronts folder
# # returns a list of hypervolumes
# def get_hypervolume_list():
#     from hypervolume_runner import HyperVolume_wrapper
#     hypervol = HyperVolume_wrapper()
#     # clean up files
#     for f in os.listdir('./Pareto_Fronts/'):
#         os.remove('./Pareto_Fronts/' + f)
#     return hypervol
#
# try:
#     os.mkdir('results')
# except Exception:
#     pass

# initial, final = ga(gens=50, problem=DTLZ1())
# write_results('results/GA_DTLZ1.out', DTLZ1(), final)

# initial, final = nsgaii(problem=DTLZ1(), crossover_rate=1.0, mutation=(1 / 20.0), dom_func=cdom)
# write_results('results/NSGA_DTLZ1.out', DTLZ1(), final)

# initial, final = ga(gens=50, problem=POM3())
# write_results('results/GA_POM3.out', POM3(), final)

# initial, final = ga(gens=50, problem=DTLZ3())
# write_results('results/GA_DTLZ3.out', DTLZ3(), final)

# results_file = open('results/results.txt', 'w')
# obj_list = [2, 4, 6]
# decisions_list = [10, 20, 40]
# dom_func_list = [bdom, cdom]
# prob_func_list = [DTLZ1, DTLZ3, DTLZ5, DTLZ7]
#
# for prob in prob_func_list:
#     for func in dom_func_list:
#         for obj_num in obj_list:
#             for dec_num in decisions_list:
#                 print('NSGA_{3}_{2}({0}, {1})'.format(obj_num, dec_num, func.__name__, prob.__name__))
#                 for i in xrange(20):
#                     say("Run " + str(i + 1).zfill(2) + ": ")
#                     problem = prob(obj_num, dec_num)
#                     initial, final = nsgaii(gens=50, problem=problem, dom_func=func)
#                     # writing results of the frontier for hypervol to calculate
#                     write_results('NSGA_{1}_{0}.txt'.format(i, prob.__name__), problem, final)
#                 results_file.write('NSGA_{3}_{2}_{0}_{1}\n'.format(obj_num, dec_num, func.__name__, prob.__name__))
#                 h_list = get_hypervolume_list()
#                 for item in h_list:
#                     results_file.write(str(item) + " ")
#                     results_file.write("\n")
#                 results_file.flush()
#                 say("Hypervolumes: ")
#                 print(h_list)
#                 print()
#
# results_file.close()
