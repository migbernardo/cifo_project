import numpy as np
from random import choice
from fitness_v2 import get_fitness


def tpco(p1: np.array, p2: np.array):
    """
    Two Point Crossover

    :param p1: arr representation of parent 1
    :param p2: arr representation of parent 2
    :return: Children of the crossover process
    """
    c1 = list(p1)
    c2 = list(p2)
    # set crossover points within 3x3 sub-grids
    start_index = [9 * x for x in range(0, 9)]
    end_index = [9 * x - 1 for x in range(1, 10)]
    p_start = choice(start_index)
    p_end = choice(end_index)
    # keep selecting points until an allowed range is obtained
    while p_end - p_start <= 8:
        p_start = choice(start_index)
        p_end = choice(end_index)
    # swap positions
    c1[p_start:p_end + 1], c2[p_start:p_end + 1] = c2[p_start:p_end + 1], c1[p_start:p_end + 1]
    c1 = np.array(c1)
    c2 = np.array(c2)
    return c1, c2


def opco(p1: np.array, p2: np.array):
    """
    One Point Crossover

    :param p1: arr representation of parent 1
    :param p2: arr representation of parent 2
    :return: Children of the crossover process
    """
    p1_list = list(p1)
    p2_list = list(p2)
    # set crossover points within 3x3 sub-grids
    co_index = [9 * x for x in range(1, 9)]
    p_co = choice(co_index)
    # exchange at co point
    c1 = p1_list[:p_co] + p2_list[p_co:]
    c2 = p2_list[:p_co] + p1_list[p_co:]
    c1 = np.array(c1)
    c2 = np.array(c2)
    return c1, c2


def fitness_co(p1: np.array, p2: np.array, opt: str, iterations: int, fitness_type: str):
    """
    Fitness Crossver

    :param p1: arr representation of parent 1
    :param p2: arr representation of parent 2
    :param opt: type of optimization problem
    :param iterations: number of iterations to keep trying to improve the average fitness of the parents
    :param fitness_type: type of fitness function
    :return: Children of the crossover process
    """
    avg_parent_fitness = (get_fitness(p1, opt, fitness_type) + get_fitness(p2, opt, fitness_type)) / 2
    avg_child_fitness = 0
    n_iter = 0
    # keep crossover until average fitness has not improved and the number of iterations has not been reached
    while avg_child_fitness <= avg_parent_fitness and n_iter < iterations:
        avg_child_fitness = 0
        p1_list = list(p1)
        p2_list = list(p2)
        # set crossover points within 3x3 sub-grids
        co_index = [9 * x for x in range(1, 9)]
        p_co = choice(co_index)
        # exchange at co point
        c1 = p1_list[:p_co] + p2_list[p_co:]
        c2 = p2_list[:p_co] + p1_list[p_co:]
        c1 = np.array(c1)
        c2 = np.array(c2)
        avg_child_fitness += (get_fitness(c1, opt, fitness_type) + get_fitness(c2, opt, fitness_type)) / 2
        n_iter += 1
    return c1, c2
