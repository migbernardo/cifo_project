import numpy as np
from representation import get_grid


def get_fitness(arr, opt, fitness_type):
    arr_1 = arr.reshape(9, 9)
    arr_2 = get_grid(arr)
    list_sub = [list(x) for x in arr_1]
    if opt == 'min':
        sum_list_1 = []
        for sub in list_sub:
            sum_list_1.append(9 - len(set(sub)))

        sum_list_2 = []
        for i in range(9):
            row = 9 - len(np.unique(arr_2[i]))
            col = 9 - len(np.unique(arr_2[:, i]))
            sum_list_2.append(row + col)
        if fitness_type == 'sum':
            return sum(sum_list_1) + sum(sum_list_2)
        else:
            return int((sum(sum_list_1) + sum(sum_list_2)) / 3)

    else:
        sum_list_1 = []
        for sub in list_sub:
            sum_list_1.append(len(set(sub)))

        sum_list_2 = []
        for i in range(9):
            row = len(np.unique(arr_2[i]))
            col = len(np.unique(arr_2[:, i]))
            sum_list_2.append(row + col)
        if fitness_type == 'sum':
            return sum(sum_list_1) + sum(sum_list_2)
        else:
            return int((sum(sum_list_1) + sum(sum_list_2)) / 3)
