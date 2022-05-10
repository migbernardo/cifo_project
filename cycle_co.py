import random


def shuffle(parent, not_fixed_index):
    num_to_shuffle = [parent[index] for index in not_fixed_index]
    shuffled = random.sample(num_to_shuffle, k=len(num_to_shuffle))

    for i, j in enumerate(not_fixed_index):
        parent[j] = shuffled[i]

    return parent


def cycle_co(p1, p2):
    c1 = [None] * len(p1)
    c2 = [None] * len(p2)

    while None in c1:
        index = c1.index(None)
        val1 = p1[index]
        val2 = p2[index]

        while val1 != val2:
            c1[index] = p1[index]
            c2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        for element in c1:
            if element is None:
                index = c1.index(None)
                if c1[index] is None:
                    c1[index] = p2[index]
                    c2[index] = p1[index]
    return c1, c2


if __name__ == '__main__':
    p1 = [8, 4, 2, 5, 6, 9, 7, 3, 1]
    p2 = [8, 4, 2, 9, 6, 5, 7, 3, 1]
    p1 = shuffle(p1, [1, 3, 5, 7])
    p2 = shuffle(p2, [1, 3, 5, 7])
    c1 = cycle_co(p1, p2)[0]
    c2 = cycle_co(p1, p2)[1]
