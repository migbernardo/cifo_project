from random import sample


def shuffle(parent, not_fixed_index):
    suffled_parent = []
    for subgrid, indexes in zip(parent, not_fixed_index):
        subgrid = subgrid.copy()
        num_to_shuffle = [subgrid[index] for index in indexes]
        shuffled = sample(num_to_shuffle, k=len(num_to_shuffle))

        for i, j in enumerate(indexes):
            subgrid[j] = shuffled[i]
        suffled_parent.append(subgrid)
    return suffled_parent


def cycle_co(p1, p2):
    c1 = []
    c2 = []
    for subgrid in range(len(p1)):
        subc1 = [None] * len(p1)
        subc2 = [None] * len(p2)

        while None in subc1:
            index = subc1.index(None)
            val1 = p1[subgrid][index]
            val2 = p2[subgrid][index]

            while val1 != val2:
                subc1[index] = p1[subgrid][index]
                subc2[index] = p2[subgrid][index]
                val2 = p2[subgrid][index]
                index = p1[subgrid].index(val2)

            for element in subc1:
                if element is None:
                    index = subc1.index(None)
                    if subc1[index] is None:
                        subc1[index] = p2[subgrid][index]
                        subc2[index] = p1[subgrid][index]
            c1.append(subc1)
            c2.append(subc2)
    return c1, c2


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

    p2 = [
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

    p1s = shuffle(p1, si1)

    p2s = shuffle(p2, si2)

    c1 = cycle_co(p1s, p2s)[0]

    c2 = cycle_co(p1s, p2s)[1]
