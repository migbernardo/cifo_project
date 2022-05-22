import numpy as np
from random import randint, choice, choices


def opm(child, not_fixed_index):
    child = child.copy()
    index_to_change = choice(not_fixed_index)
    child[index_to_change] = randint(1, 9)
    return child


def npm(child, not_fixed_index, n_mutations):
    child = child.copy()
    indexes_to_change = choices(not_fixed_index, k=n_mutations)
    for index in indexes_to_change:
        child[index] = randint(1, 9)
    return child


def swap(child, not_fixed_index):
    c_list = list(child)
    indexes_to_swap = choices(not_fixed_index, k=2)
    c_list[indexes_to_swap[0]], c_list[indexes_to_swap[1]] = c_list[indexes_to_swap[1]], c_list[indexes_to_swap[0]]
    c_list = np.array(c_list)
    return c_list


def inner_swap(child, not_fixed_index_list):
    c_list = [list(x) for x in child.reshape(9, 9)]
    block_to_swap = choice(range(9))
    indexes_to_swap = choices(not_fixed_index_list[block_to_swap], k=2)
    c_list[block_to_swap][indexes_to_swap[0]], c_list[block_to_swap][indexes_to_swap[1]] = c_list[block_to_swap][indexes_to_swap[1]], c_list[block_to_swap][indexes_to_swap[0]]
    c_list = np.array(c_list).flatten()
    return c_list


def n_swap(child, not_fixed_index, num_swap):
    c_list = list(child)
    for i in range(num_swap):
        indexes_to_swap = choices(not_fixed_index, k=2)
        c_list[indexes_to_swap[0]], c_list[indexes_to_swap[1]] = c_list[indexes_to_swap[1]], c_list[indexes_to_swap[0]]
    c_list = np.array(c_list)
    return c_list


def rand_mut(child, not_fixed_index, not_fixed_index_list):
    chosen_mutation = choice(['swap', 'inner_swap'])
    if chosen_mutation == 'swap':
        return swap(child, not_fixed_index)
    else:
        return inner_swap(child, not_fixed_index_list)
