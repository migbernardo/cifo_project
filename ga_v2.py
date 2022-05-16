import numpy as np
from representation import get_rep, get_grid
from random import randint, random
from fitness_v2 import get_fitness
from selection_v2 import tournament
from crossover_v2 import tpco
from mutation_v2 import opm, npm, swap, rand_mut


class Solver:
    def __init__(self, item, pop_size):
        self.arr = np.array(item)
        self.pop_size = pop_size
        if self.arr.shape != (9, 9):
            print('INPUT A 9x9 GRID')
        elif np.where(self.arr == 0)[0].shape[0] == 0:
            print('INPUT NON GIVEN POSITIONS AS ZERO')
        else:
            self.rep = get_rep(self.arr)
            self.fixed = np.where(self.rep != 0)[0]
            self.not_fixed = np.where(self.rep == 0)[0]
            self.pop = []
            for i in range(self.pop_size):
                rep = self.rep.copy()
                for index in self.not_fixed:
                    rep[index] = randint(1, 9)
                self.pop.append(rep)

    def evolve(self, num_generations, t_size, co_p, mutation, mu_p, n_mutations=None):
        for gen in range(num_generations):
            new_pop = []
            while len(new_pop) < self.pop_size:
                p1 = tournament(self.pop, t_size)
                p2 = tournament(self.pop, t_size)
                if random() < co_p:
                    c1 = tpco(p1, p2)[0]
                    c2 = tpco(p1, p2)[1]
                else:
                    c1, c2 = p1, p2
                if random() < mu_p:
                    if mutation == 'opm':
                        c1 = opm(c1, self.not_fixed)
                    elif mutation == 'npm':
                        c1 = npm(c1, self.not_fixed, n_mutations)
                    elif mutation == 'swap':
                        c1 = swap(c1, self.not_fixed)
                    else:
                        c1 = rand_mut(c1, self.not_fixed)

                if random() < mu_p:
                    if mutation == 'opm':
                        c2 = opm(c2, self.not_fixed)
                    elif mutation == 'npm':
                        c2 = npm(c2, self.not_fixed, n_mutations)
                    elif mutation == 'swap':
                        c2 = swap(c2, self.not_fixed)
                    else:
                        c2 = rand_mut(c2, self.not_fixed)

                new_pop.append(c1)
                if len(new_pop) < self.pop_size:
                    new_pop.append(c2)

            self.pop = new_pop
            current_fitness = []
            for sol in new_pop:
                current_fitness.append(get_fitness(sol))
                if get_fitness(sol) == 243:
                    final_solution = sol
            print(f'best individual of generation {gen + 1}: {max(current_fitness)} fitness')
            if max(current_fitness) == 243:
                print(get_grid(final_solution))
                break


if __name__ == '__main__':
    puzzle = Solver(item=[
        [0, 0, 0, 1, 5, 0, 6, 9, 0],
        [0, 0, 1, 6, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 2, 0, 0, 0, 4],
        [8, 0, 0, 0, 0, 0, 3, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 8, 0],
        [0, 9, 4, 0, 0, 0, 0, 0, 5],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 3, 9, 0, 0],
        [0, 4, 2, 0, 8, 9, 0, 0, 0]
    ], pop_size=1000)

    puzzle.evolve(num_generations=400, t_size=4, co_p=0.9, mutation='swap', mu_p=0.9)
