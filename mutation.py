import numpy as np
from random import sample
from fitness import get_fitness


def swap_mutation(child, not_fixed_index):
    mutated = []
    for subgrid, indexes in zip(child, not_fixed_index):
        subgrid = subgrid.copy()
        pos = sample(indexes, k=2)
        subgrid[pos[0]], subgrid[pos[1]] = subgrid[pos[1]], subgrid[pos[0]]
        mutated.append(subgrid)
    return mutated


def fitness_mutation(child, not_fixed_index):
    child_fitness = get_fitness(np.array(child))
    mutated_fitness = 0
    while child_fitness >= mutated_fitness:
        mutated = []
        mutated_fitness = 0
        for subgrid, indexes in zip(child, not_fixed_index):
            subgrid = subgrid.copy()
            pos = sample(indexes, k=2)
            subgrid[pos[0]], subgrid[pos[1]] = subgrid[pos[1]], subgrid[pos[0]]
            mutated.append(subgrid)
        mutated_fitness += get_fitness(np.array(mutated))
    return mutated


if __name__ == '__main__':
    p1 = [
        [8, 4, 2, 9, 6, 3, 7, 5, 1],
        [4, 8, 3, 6, 9, 1, 7, 2, 5],
        [5, 1, 2, 7, 6, 3, 8, 9, 4],
        [6, 5, 8, 3, 7, 4, 9, 2, 1],
        [6, 7, 4, 2, 5, 8, 3, 1, 9],
        [8, 2, 1, 9, 6, 5, 4, 7, 3],
        [8, 4, 7, 1, 3, 5, 2, 6, 9],
        [4, 1, 2, 5, 8, 9, 3, 6, 7],
        [7, 8, 6, 9, 2, 4, 1, 3, 5]]

si1 = [
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 3],
]

m = fitness_mutation(p1, si1)

p1_arr = np.array(p1)

pi_list = [list(x) for x in p1_arr]
