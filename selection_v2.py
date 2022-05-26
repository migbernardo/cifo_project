from random import choices, uniform
from scipy import stats
from fitness_v2 import get_fitness


def tournament(solutions: list, t_size: int, opt: str, fitness_type: str):
    """
    Tournament Selection

    :param solutions: list of solutions in arr representation
    :param t_size: tournament size
    :param opt: type of optimization problem
    :param fitness_type: type of fitness function
    :return: Returns the best individual of a subset of solutions
    """
    sol_subset = choices(solutions, k=t_size)
    fitness = []
    for sol in sol_subset:
        fitness.append(get_fitness(sol, opt, fitness_type))
    if opt == 'min':
        return sol_subset[fitness.index(min(fitness))]
    else:
        return sol_subset[fitness.index(max(fitness))]


def fps(solutions: list, opt: str, fitness_type: str):
    """
    Fitness Proportionate Selection

    :param solutions: list of solutions in arr representation
    :param opt: type of optimization problem
    :param fitness_type: type of fitness function
    :return: Returns an individual according to its probability of being selected
    """
    fitness = []
    for sol in solutions:
        fitness.append(get_fitness(sol, opt, fitness_type))
    spin = uniform(0, max(fitness))
    position = 0
    for fit, sol in enumerate(solutions):
        position += fitness[fit]
        if position > spin:
            return sol


def ranking(solutions: list, opt: str, fitness_type: str):
    """
    Ranking Selection

    :param solutions: list of solutions in arr representation
    :param opt: type of optimization problem
    :param fitness_type: type of fitness function
    :return: Returns an individual according to its probability of being selected
    """
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
