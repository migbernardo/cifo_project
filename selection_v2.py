from random import choices, uniform
from scipy import stats
from fitness_v2 import get_fitness


def tournament(solutions, t_size, opt, fitness_type):
    sol_subset = choices(solutions, k=t_size)
    fitness = []
    for sol in sol_subset:
        fitness.append(get_fitness(sol, opt, fitness_type))
    if opt == 'min':
        return sol_subset[fitness.index(min(fitness))]
    else:
        return sol_subset[fitness.index(max(fitness))]


def fps(solutions, opt, fitness_type):
    fitness = []
    for sol in solutions:
        fitness.append(get_fitness(sol, opt, fitness_type))
    spin = uniform(0, max(fitness))
    position = 0
    for fit, sol in enumerate(solutions):
        position += fitness[fit]
        if position > spin:
            return sol


def ranking(solutions, opt, fitness_type):
    fitness = []
    for sol in solutions:
        fitness.append(get_fitness(sol, opt, fitness_type))
    rank_fitness = list(stats.rankdata(fitness))
    spin = uniform(0, max(rank_fitness))
    position = 0
    for fit, sol in enumerate(solutions):
        position += rank_fitness[fit]
        if position > spin:
            return sol
