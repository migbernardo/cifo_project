import numpy as np
from random import randint, choice, choices


def opm(child: np.array, not_fixed_index: list):
    """
    One Point Mutation

    :param child: child 81 digits arr representation
    :param not_fixed_index: list of not fixed positions
    :return: Mutated child
    """
    child = child.copy()
    index_to_change = choice(not_fixed_index)
    child[index_to_change] = randint(1, 9)
    return child


def npm(child: np.array, not_fixed_index: list, n_mutations: int):
    """
    N Point Mutation (Generalization of the One Point Mutation)

    :param child: child 81 digits arr representation
    :param not_fixed_index: list of not fixed positions
    :param n_mutations: number of mutations to perform
    :return: Mutated child
    """
    child = child.copy()
    indexes_to_change = choices(not_fixed_index, k=n_mutations)
    for index in indexes_to_change:
        child[index] = randint(1, 9)
    return child


def swap(child: np.array, not_fixed_index: list):
    """
    Swap Mutation

    :param child: child 81 digits arr representation
    :param not_fixed_index: list of not fixed positions
    :return: Mutated child
    """
    c_list = list(child)
    indexes_to_swap = choices(not_fixed_index, k=2)
    c_list[indexes_to_swap[0]], c_list[indexes_to_swap[1]] = c_list[indexes_to_swap[1]], c_list[indexes_to_swap[0]]
    c_list = np.array(c_list)
    return c_list


def inner_swap(child: np.array, not_fixed_index_list: list):
    """
    Inner Swap Mutation

    :param child: child 81 digits arr representation
    :param not_fixed_index_list: list of lists of the not fixed positions of each 3x3 sub-grid
    :return: Mutated child
    """
    c_list = [list(x) for x in child.reshape(9, 9)]
    block_to_swap = choice(range(9))
    indexes_to_swap = choices(not_fixed_index_list[block_to_swap], k=2)
    c_list[block_to_swap][indexes_to_swap[0]], c_list[block_to_swap][indexes_to_swap[1]] = c_list[block_to_swap][indexes_to_swap[1]], c_list[block_to_swap][indexes_to_swap[0]]
    c_list = np.array(c_list).flatten()
    return c_list


def n_swap(child: np.array, not_fixed_index: list, num_swap: int):
    """
    N Swap Mutation (Generalization of the Swap Mutation)

    :param child: child 81 digits arr representation
    :param not_fixed_index: list of not fixed positions
    :param num_swap: number of swaps to perform
    :return: Mutated child
    """
    c_list = list(child)
    for i in range(num_swap):
        indexes_to_swap = choices(not_fixed_index, k=2)
        c_list[indexes_to_swap[0]], c_list[indexes_to_swap[1]] = c_list[indexes_to_swap[1]], c_list[indexes_to_swap[0]]
    c_list = np.array(c_list)
    return c_list


def rand_mut(child: np.array, not_fixed_index: list, not_fixed_index_list: list):
    """
    Random Mutation (Swap or Inner Swap)

    :param child: child 81 digits arr representation
    :param not_fixed_index: list of not fixed positions
    :param not_fixed_index_list: list of lists of the not fixed positions of each 3x3 sub-grid
    :return: Mutated child
    """
    chosen_mutation = choice(['swap', 'inner_swap'])
    if chosen_mutation == 'swap':
        return swap(child, not_fixed_index)
    else:
        return inner_swap(child, not_fixed_index_list)
