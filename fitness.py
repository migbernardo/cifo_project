import numpy as np


def get_fitness(arr):
    # convert sub-grid matrix into puzzle matrix
    sol = np.zeros([9, 9])
    for i in range(3):
        row_stack = np.stack([arr[0].reshape(3, 3)[i],
                              arr[1].reshape(3, 3)[i],
                              arr[2].reshape(3, 3)[i]],
                             axis=0).flatten()
        sol[i] = row_stack

    for i in range(3):
        row_stack = np.stack([arr[3].reshape(3, 3)[i],
                              arr[4].reshape(3, 3)[i],
                              arr[5].reshape(3, 3)[i]],
                             axis=0).flatten()
        sol[i + 3] = row_stack

    for i in range(3):
        row_stack = np.stack([arr[6].reshape(3, 3)[i],
                              arr[7].reshape(3, 3)[i],
                              arr[8].reshape(3, 3)[i]],
                             axis=0).flatten()
        sol[i + 6] = row_stack

    sol = sol.astype('int32')

    # calculate fitness of the filled puzzle matrix
    total = []
    for i in range(9):
        row = len(np.unique(sol[i]))
        col = len(np.unique(sol[:, i]))
        total.append(row + col)
    return sum(total)
