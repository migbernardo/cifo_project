from random import uniform


def fps(solutions, fitness):
    spin = uniform(0, max(fitness))
    position = 0
    for fit, sol in enumerate(solutions):
        position += fitness[fit]
        if position > spin:
            return sol
