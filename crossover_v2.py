import numpy as np
from random import choice


def tpco(p1, p2):
    c1 = list(p1)
    c2 = list(p2)
    start_index = [9 * x for x in range(0, 9)]
    end_index = [9 * x - 1 for x in range(1, 10)]
    p_start = choice(start_index)
    p_end = choice(end_index)
    while p_end - p_start <= 8:
        p_start = choice(start_index)
        p_end = choice(end_index)
    c1[p_start:p_end + 1], c2[p_start:p_end + 1] = c2[p_start:p_end + 1], c1[p_start:p_end + 1]
    c1 = np.array(c1)
    c2 = np.array(c2)
    return c1, c2
