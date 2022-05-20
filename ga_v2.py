import numpy as np
from representation import get_rep, get_rep2, get_grid
from random import randint, random
from fitness_v2 import get_fitness
from selection_v2 import tournament, fps, ranking
from crossover_v2 import tpco, opco, fitness_co
from mutation_v2 import opm, npm, swap, rand_mut, n_swap, inner_swap
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
            self.rep2 = get_rep2(self.arr)
            self.not_fixed_block = []
            for block in self.rep2:
                self.not_fixed_block.append(list(np.where(block == 0)[0]))
            self.final_solution = None

    def evolve(self,
               num_generations,
               selection,
               crossover,
               co_p,
               mutation,
               mu_p,
               opt,
               fitness_type,
               n_mutations=None,
               num_swap=None,
               t_size=None,
               elitism=False,
               global_optimum=None,
               iterations=None,
               export=False,
               file_name=None):

        # SAFEGUARDS
        if selection not in ['tournament', 'fps', 'ranking']:
            print("input a valid selection method: 'tournament', 'fps', 'ranking'")

        elif crossover not in ['tpco', 'opco', 'fitness_co']:
            print("input a valid crossover method: 'tpco', 'opco', 'fitness_co'")

        elif mutation not in ['opm', 'npm', 'swap', 'n_swap', 'inner_swap', 'rand_mut']:
            print("input a valid mutation method: 'opm', 'npm', 'swap', 'n_swap', 'inner_swap', 'rand_mut'")

        elif fitness_type not in ['sum', 'avg']:
            print("input a valid fitness type: 'sum', 'avg'")

        elif opt not in ['max', 'min']:
            print("input valid optimization problem: 'max', 'min'")

        elif selection == 'tournament' and t_size is None:
            print('input t_size value')

        elif crossover == 'fitness_co' and iterations is None:
            print('input iterations value')

        elif mutation == 'npm' and n_mutations is None:
            print('input n_mutations value')

        elif mutation == 'n_swap' and num_swap is None:
            print('input num_swap value')

        elif export and file_name is None:
            print('input file_name')

        elif self.pop_size % 2 != 0:
            print('input even pop_size')

        else:
            # iterate for the chosen number of generations
            for gen in range(num_generations):
                new_pop = []

                # save the best individual of the current population (elite)
                if elitism:
                    # get fitness of all individuals of the current population
                    fitness = []
                    for sol in self.pop:
                        fitness.append(get_fitness(sol, opt, fitness_type))
                    # save best solution
                    if opt == 'min':
                        elite = self.pop[fitness.index(min(fitness))]
                    else:
                        elite = self.pop[fitness.index(max(fitness))]

                # select, cross and mutate individuals of the current population until there's a new one with the same size
                while len(new_pop) < self.pop_size:
                    # SELECTION
                    if selection == 'tournament':
                        p1 = tournament(self.pop, t_size, opt, fitness_type)
                        p2 = tournament(self.pop, t_size, opt, fitness_type)
                    elif selection == 'fps':
                        p1 = fps(self.pop, opt, fitness_type)
                        p2 = fps(self.pop, opt, fitness_type)
                    else:
                        p1 = ranking(self.pop, opt, fitness_type)
                        p2 = ranking(self.pop, opt, fitness_type)

                    # CROSSOVER
                    if random() < co_p:
                        if crossover == 'tpco':
                            c1 = tpco(p1, p2)[0]
                            c2 = tpco(p1, p2)[1]
                        elif crossover == 'opco':
                            c1 = opco(p1, p2)[0]
                            c2 = opco(p1, p2)[1]
                        else:
                            c1 = fitness_co(p1, p2, opt, iterations)[0]
                            c2 = fitness_co(p1, p2, opt, iterations)[1]
                    # reproduce parents if mutation doesn't happen
                    else:
                        c1, c2 = p1, p2

                    # MUTATION
                    # child 1 mutation
                    if random() < mu_p:
                        if mutation == 'opm':
                            c1 = opm(c1, self.not_fixed)
                        elif mutation == 'npm':
                            c1 = npm(c1, self.not_fixed, n_mutations)
                        elif mutation == 'swap':
                            c1 = swap(c1, self.not_fixed)
                        elif mutation == 'n_swap':
                            c1 = n_swap(c1, self.not_fixed, num_swap)
                        elif mutation == 'inner_swap':
                            c1 = inner_swap(c1, self.not_fixed_block)
                        else:
                            c1 = rand_mut(c1, self.not_fixed, self.not_fixed_block)

                    # child 2 mutation
                    if random() < mu_p:
                        if mutation == 'opm':
                            c2 = opm(c2, self.not_fixed)
                        elif mutation == 'npm':
                            c2 = npm(c2, self.not_fixed, n_mutations)
                        elif mutation == 'swap':
                            c2 = swap(c2, self.not_fixed)
                        elif mutation == 'n_swap':
                            c2 = n_swap(c2, self.not_fixed, num_swap)
                        elif mutation == 'inner_swap':
                            c2 = inner_swap(c2, self.not_fixed_block)
                        else:
                            c2 = rand_mut(c2, self.not_fixed, self.not_fixed_block)

                    # add offspring into new population
                    new_pop.append(c1)
                    if len(new_pop) < self.pop_size:
                        new_pop.append(c2)

                # replace worse solution of the new population by the best individual of the original population (elite)
                if elitism:
                    new_sol_fitness = []
                    for sol in new_pop:
                        new_sol_fitness.append(get_fitness(sol, opt, fitness_type))
                    if opt == 'min':
                        worst = new_sol_fitness.index(max(new_sol_fitness))
                    else:
                        worst = new_sol_fitness.index(min(new_sol_fitness))
                    new_pop.pop(worst)
                    new_pop.append(elite)

                # replace original population by the new population
                self.pop = new_pop
                # save fitness of all individuals of the new population
                current_fitness = []
                for sol in new_pop:
                    current_fitness.append(get_fitness(sol, opt, fitness_type))
                    # save final solution if global optimum is reached
                    if get_fitness(sol, opt, fitness_type) == global_optimum:
                        self.final_solution = sol

                # print the fitness value of the best individual of each generation
                if opt == 'min':
                    self.fitness.append(min(current_fitness))
                    print(f'best individual of generation {gen + 1}: {min(current_fitness)} fitness')
                else:
                    self.fitness.append(max(current_fitness))
                    print(f'best individual of generation {gen + 1}: {max(current_fitness)} fitness')

            # plot fitness landscape after reaching the defined number of generations
            print(plot(num_generations, self.fitness, opt))

            # print final solution if found
            if self.final_solution is not None:
                print(get_grid(self.final_solution))

            # export data into csv file saved in the current directory
            if export:
                export_csv(self.fitness, file_name)


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
    ], pop_size=100)

    puzzle.evolve(num_generations=100,
                  selection='tournament',
                  crossover='opco',
                  co_p=0.9,
                  mutation='swap',
                  mu_p=0.9,
                  opt='min',
                  t_size=10,
                  n_mutations=None,
                  num_swap=None,
                  elitism=False,
                  global_optimum=0,
                  export=True,
                  file_name='selection_test_tournament_opco_10',
                  fitness_type='sum')
