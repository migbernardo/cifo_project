import numpy as np
from random import sample


def shuffle(parent, not_fixed_index):
    parent_list = [list(x) for x in parent]
    suffled_parent = []
    for subgrid, indexes in zip(parent_list, not_fixed_index):
        subgrid = subgrid.copy()
        num_to_shuffle = [subgrid[index] for index in indexes]
        shuffled = sample(num_to_shuffle, k=len(num_to_shuffle))

        for i, j in enumerate(indexes):
            subgrid[j] = shuffled[i]
        suffled_parent.append(subgrid)
    return np.array(suffled_parent)


def cycle_co(p1, p2):
    p1_list = [list(x) for x in p1]
    p2_list = [list(x) for x in p2]
    c1_list = []
    c2_list = []
    for subgrid in range(len(p1_list)):
        subc1 = [None] * len(p1_list)
        subc2 = [None] * len(p1_list)

        while None in subc1:
            index = subc1.index(None)
            val1 = p1_list[subgrid][index]
            val2 = p2_list[subgrid][index]

            while val1 != val2:
                subc1[index] = p1_list[subgrid][index]
                subc2[index] = p2_list[subgrid][index]
                val2 = p2_list[subgrid][index]
                index = p1_list[subgrid].index(val2)

            for element in subc1:
                if element is None:
                    index = subc1.index(None)
                    if subc1[index] is None:
                        subc1[index] = p2_list[subgrid][index]
                        subc2[index] = p1_list[subgrid][index]
            c1_list.append(subc1)
            c2_list.append(subc2)
    return np.array(c1_list), np.array(c2_list)


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

    si2 = [
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

    a1s = shuffle(np.array(a1), si1)

    a2s = shuffle(np.array(a2), si2)

    b1 = cycle_co(a1s, a2s)[0]

    b2 = cycle_co(a1s, a2s)[1]
