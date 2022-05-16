import matplotlib.pyplot as plt


def plot(n_gen, fitness):
    generations = list(range(0, n_gen + 1))
    plt.plot(generations, fitness, 'b', label='Fitness')
    plt.title('Fitness landscape')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.legend()
    return plt.show()
