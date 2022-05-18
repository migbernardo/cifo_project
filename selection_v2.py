from random import choices, uniform
from scipy import stats
from fitness_v2 import get_fitness


def tournament(solutions, t_size):
    sol_subset = choices(solutions, k=t_size)
    fitness = []
    for sol in sol_subset:
        fitness.append(get_fitness(sol))
    return sol_subset[fitness.index(min(fitness))]


def fps(solutions):
    fitness = []
    for sol in solutions:
        fitness.append(get_fitness(sol))
    spin = uniform(0, max(fitness))
    position = 0
    for fit, sol in enumerate(solutions):
        position += fitness[fit]
        if position > spin:
            return sol


def ranking(solutions):
    fitness = []
    for sol in solutions:
        fitness.append(get_fitness(sol))
    rank_fitness = list(stats.rankdata(fitness))
    spin = uniform(0, max(rank_fitness))
    position = 0
    for fit, sol in enumerate(solutions):
        position += rank_fitness[fit]
        if position > spin:
            return sol
