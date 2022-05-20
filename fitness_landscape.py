import matplotlib.pyplot as plt
import numpy as np


def plot(n_gen, fitness, opt):
    generations = list(range(1, n_gen + 1))
    plt.plot(generations, fitness, 'b', label=opt)
    plt.title('Fitness landscape')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.legend()
    return plt.show()


def export_csv(fitness, name):
    return np.savetxt(f'{name}.csv', fitness, delimiter=", ", fmt='% s')
