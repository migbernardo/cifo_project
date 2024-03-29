import numpy as np


def get_rep(arr: np.array):
    """
    Convert puzzle into GA's representation

    :param arr: puzzle's 81 digits arr representation
    :return: flat array representation of the puzzle
    """
    rep = np.stack([
        arr[:3, :3].flatten(),
        arr[:3, 3:6].flatten(),
        arr[:3, 6:].flatten(),
        arr[3:6, :3].flatten(),
        arr[3:6, 3:6].flatten(),
        arr[3:6, 6:].flatten(),
        arr[6:, :3].flatten(),
        arr[6:, 3:6].flatten(),
        arr[6:, 6:].flatten()
    ], axis=0).flatten()
    return rep


def get_rep2(arr: np.array):
    """
    Convert puzzle into GA's representation for Inner Swap Mutation

    :param arr: puzzle's 81 digits arr representation
    :return: non-flat array representation of the puzzle
    """
    rep = np.stack([
        arr[:3, :3].flatten(),
        arr[:3, 3:6].flatten(),
        arr[:3, 6:].flatten(),
        arr[3:6, :3].flatten(),
        arr[3:6, 3:6].flatten(),
        arr[3:6, 6:].flatten(),
        arr[6:, :3].flatten(),
        arr[6:, 3:6].flatten(),
        arr[6:, 6:].flatten()
    ], axis=0)
    return rep


def get_grid(arr: np.array):
    """
    Convert puzzle's array representation into original grid

    :param arr: puzzle's 81 digits arr representation
    :return: Original puzzle's grid
    """
    arr = arr.reshape(9, 9)
    grid = np.zeros([9, 9])
    for i in range(3):
        row_stack = np.stack([arr[0].reshape(3, 3)[i],
                              arr[1].reshape(3, 3)[i],
                              arr[2].reshape(3, 3)[i]],
                             axis=0).flatten()
        grid[i] = row_stack

    for i in range(3):
        row_stack = np.stack([arr[3].reshape(3, 3)[i],
                              arr[4].reshape(3, 3)[i],
                              arr[5].reshape(3, 3)[i]],
                             axis=0).flatten()
        grid[i + 3] = row_stack

    for i in range(3):
        row_stack = np.stack([arr[6].reshape(3, 3)[i],
                              arr[7].reshape(3, 3)[i],
                              arr[8].reshape(3, 3)[i]],
                             axis=0).flatten()
        grid[i + 6] = row_stack

    grid = grid.astype('int32')
    return grid
