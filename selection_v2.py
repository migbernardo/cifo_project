from random import choices
from fitness_v2 import get_fitness


def tournament(solutions, t_size):
    sol_subset = choices(solutions, k=t_size)
    fitness = []
    for sol in sol_subset:
        fitness.append(get_fitness(sol))
    return sol_subset[fitness.index(max(fitness))]
