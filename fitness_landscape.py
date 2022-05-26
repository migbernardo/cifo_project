import matplotlib.pyplot as plt
import numpy as np


def plot(n_gen: int, fitness: list, opt: str):
    """
    Fitness Plot

    :param n_gen: number of chosen generations to evolve the initial population
    :param fitness: list of fitness values for each generation
    :param opt: type of optimization problem
    :return: Fitness plot of the experiment
    """
    generations = list(range(1, n_gen + 1))
    plt.plot(generations, fitness, 'b', label=opt)
    plt.title('Fitness landscape')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.legend()
    return plt.show()


def export_csv(fitness: list, name: str):
    """
    Export fitness values

    :param fitness: list of fitness values for each generation
    :param name: file's name
    :return: .csv with fitness values of the experiment
    """
    return np.savetxt(f'{name}.csv', fitness, delimiter=", ", fmt='% s')
