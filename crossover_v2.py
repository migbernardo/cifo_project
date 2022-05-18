import numpy as np
from random import choice, sample
from representation import get_rep
from fitness_v2 import get_fitness


def tpco(p1, p2):
    c1 = list(p1)
    c2 = list(p2)
    start_index = [9 * x for x in range(0, 9)]
    end_index = [9 * x - 1 for x in range(1, 10)]
    p_start = choice(start_index)
    p_end = choice(end_index)
    while p_end - p_start <= 8:
        p_start = choice(start_index)
        p_end = choice(end_index)
    c1[p_start:p_end + 1], c2[p_start:p_end + 1] = c2[p_start:p_end + 1], c1[p_start:p_end + 1]
    c1 = np.array(c1)
    c2 = np.array(c2)
    return c1, c2


def fitness_co(p1, p2):
    avg_parent_fitness = (get_fitness(p1) + get_fitness(p2)) / 2
    avg_child_fitness = 0
    n_iter = 0
    while avg_child_fitness <= avg_parent_fitness and n_iter < 20:
        avg_child_fitness = 0
        c1 = list(p1)
        c2 = list(p2)
        start_index = [9 * x for x in range(0, 9)]
        end_index = [9 * x - 1 for x in range(1, 10)]
        p_start = choice(start_index)
        p_end = choice(end_index)
        while p_end - p_start <= 8:
            p_start = choice(start_index)
            p_end = choice(end_index)
        c1[p_start:p_end + 1], c2[p_start:p_end + 1] = c2[p_start:p_end + 1], c1[p_start:p_end + 1]
        c1 = np.array(c1)
        c2 = np.array(c2)
        avg_child_fitness += (get_fitness(c1) + get_fitness(c2)) / 2
        n_iter += 1
    return c1, c2


if __name__ == '__main__':
    a1 = [
        [8, 4, 2, 9, 6, 3, 7, 5, 1],
        [4, 8, 3, 6, 9, 1, 7, 2, 5],
        [5, 1, 2, 7, 6, 3, 8, 9, 4],
        [6, 5, 8, 3, 7, 4, 9, 2, 1],
        [6, 7, 4, 2, 5, 8, 3, 1, 9],
        [8, 2, 1, 9, 6, 5, 4, 7, 3],
        [8, 4, 7, 1, 3, 5, 2, 6, 9],
        [4, 1, 2, 5, 8, 9, 3, 6, 7],
        [7, 8, 6, 9, 2, 4, 1, 3, 5]]

    a2 = [
        [8, 4, 2, 9, 6, 3, 7, 5, 1],
        [4, 8, 3, 6, 9, 1, 7, 2, 5],
        [5, 1, 2, 7, 6, 3, 8, 9, 4],
        [6, 5, 8, 3, 7, 4, 9, 2, 1],
        [6, 7, 4, 2, 5, 8, 3, 1, 9],
        [8, 2, 1, 9, 6, 5, 4, 7, 3],
        [8, 4, 7, 1, 3, 5, 2, 6, 9],
        [4, 1, 2, 5, 8, 9, 3, 6, 7],
        [7, 8, 6, 9, 2, 4, 1, 3, 5]]

    rep1 = get_rep(np.array(a1))

    rep2 = get_rep(np.array(a2))

    b1 = tpco(rep1, rep2)[0]

    b2 = tpco(rep1, rep2)[1]
