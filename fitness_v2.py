import numpy as np
from representation import get_grid


def get_fitness(arr: np.array, opt: str, fitness_type: str):
    """
    Get Fitness

    :param arr: puzzle's 81 digits arr representation
    :param opt: type of optimization problem
    :param fitness_type: type of fitness function
    :return: Fitness of the evaluated individual
    """
    arr_1 = arr.reshape(9, 9)
    arr_2 = get_grid(arr)
    list_sub = [list(x) for x in arr_1]

    # minimization problem
    if opt == 'min':
        # non-unique numbers by 3x3 sub-grid
        sum_list_1 = []
        for sub in list_sub:
            sum_list_1.append(9 - len(set(sub)))

        # non-unique numbers by row and column
        sum_list_2 = []
        for i in range(9):
            row = 9 - len(np.unique(arr_2[i]))
            col = 9 - len(np.unique(arr_2[:, i]))
            sum_list_2.append(row + col)
        if fitness_type == 'sum':
            # sum
            return sum(sum_list_1) + sum(sum_list_2)
        else:
            # average
            return int((sum(sum_list_1) + sum(sum_list_2)) / 3)

    # maximization problem
    else:
        # unique numbers by 3x3 sub-grid
        sum_list_1 = []
        for sub in list_sub:
            sum_list_1.append(len(set(sub)))

        # unique numbers by row and column
        sum_list_2 = []
        for i in range(9):
            row = len(np.unique(arr_2[i]))
            col = len(np.unique(arr_2[:, i]))
            sum_list_2.append(row + col)
        if fitness_type == 'sum':
            # sum
            return sum(sum_list_1) + sum(sum_list_2)
        else:
            # average
            return int((sum(sum_list_1) + sum(sum_list_2)) / 3)
