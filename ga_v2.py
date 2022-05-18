import numpy as np
import csv
from representation import get_rep, get_grid
from random import randint, random
from fitness_v2 import get_fitness
from selection_v2 import tournament, fps, ranking
from crossover_v2 import tpco, fitness_co
from mutation_v2 import opm, npm, swap, rand_mut, n_swap
from fitness_landscape import plot, export_csv


class Solver:
    def __init__(self, item, pop_size):
        self.arr = np.array(item)
        self.pop_size = pop_size
        if self.arr.shape != (9, 9):
            print('input a 9x9 grid (list of lists)')
        elif np.where(self.arr == 0)[0].shape[0] == 0:
            print('input non given positions as zero')
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
            self.fitness = []

    def evolve(self,
               num_generations,
               selection,
               crossover,
               co_p,
               mutation,
               mu_p,
               n_mutations=None,
               num_swap=None,
               t_size=None,
               elitism=False):
        for gen in range(num_generations):
            new_pop = []
            if elitism:
                fitness = []
                for sol in self.pop:
                    fitness.append(get_fitness(sol))
                # save best solution
                elite = self.pop[fitness.index(min(fitness))]
            while len(new_pop) < self.pop_size:
                if selection == 'tournament':
                    p1 = tournament(self.pop, t_size)
                    p2 = tournament(self.pop, t_size)
                elif selection == 'fps':
                    p1 = fps(self.pop)
                    p2 = fps(self.pop)
                else:
                    p1 = ranking(self.pop)
                    p2 = ranking(self.pop)
                if random() < co_p:
                    if crossover == 'tpco':
                        c1 = tpco(p1, p2)[0]
                        c2 = tpco(p1, p2)[1]
                    else:
                        c1 = fitness_co(p1, p2)[0]
                        c2 = fitness_co(p1, p2)[1]
                else:
                    c1, c2 = p1, p2
                if random() < mu_p:
                    if mutation == 'opm':
                        c1 = opm(c1, self.not_fixed)
                    elif mutation == 'npm':
                        c1 = npm(c1, self.not_fixed, n_mutations)
                    elif mutation == 'swap':
                        c1 = swap(c1, self.not_fixed)
                    elif mutation == 'n_swap':
                        c1 = n_swap(c1, self.not_fixed, num_swap)
                    else:
                        c1 = rand_mut(c1, self.not_fixed)

                if random() < mu_p:
                    if mutation == 'opm':
                        c2 = opm(c2, self.not_fixed)
                    elif mutation == 'npm':
                        c2 = npm(c2, self.not_fixed, n_mutations)
                    elif mutation == 'swap':
                        c2 = swap(c2, self.not_fixed)
                    elif mutation == 'n_swap':
                        c2 = n_swap(c2, self.not_fixed, num_swap)
                    else:
                        c2 = rand_mut(c2, self.not_fixed)

                new_pop.append(c1)
                if len(new_pop) < self.pop_size:
                    new_pop.append(c2)

            if elitism:
                new_sol_fitness = []
                for sol in new_pop:
                    new_sol_fitness.append(get_fitness(sol))
                # replace the worst solution by elite
                worst = new_sol_fitness.index(max(new_sol_fitness))
                new_pop.pop(worst)
                new_pop.append(elite)

            self.pop = new_pop
            current_fitness = []
            for sol in new_pop:
                current_fitness.append(get_fitness(sol))
                if get_fitness(sol) <= 4:
                    final_solution = sol
            self.fitness.append(min(current_fitness))
            print(f'best individual of generation {gen + 1}: {min(current_fitness)} fitness')
        print(plot(num_generations, self.fitness))
        print(get_grid(final_solution))
        export_csv(self.fitness, 'run10')


if __name__ == '__main__':
    puzzle = Solver(item=[
        [5, 0, 0, 1, 0, 0, 7, 0, 0],
        [0, 2, 0, 0, 0, 7, 1, 0, 0],
        [3, 0, 1, 4, 0, 0, 8, 5, 2],
        [6, 1, 0, 5, 7, 2, 4, 0, 8],
        [0, 0, 2, 9, 6, 0, 0, 0, 0],
        [0, 4, 0, 0, 3, 0, 6, 2, 7],
        [4, 5, 9, 0, 8, 0, 0, 7, 0],
        [1, 3, 0, 0, 0, 0, 9, 8, 6],
        [2, 0, 0, 0, 1, 0, 0, 4, 3]
    ], pop_size=1000)

    puzzle.evolve(num_generations=100,
                  selection='tournament',
                  crossover='tpco',
                  co_p=0.9,
                  mutation='swap',
                  mu_p=0.9,
                  t_size=4,
                  elitism=False)
