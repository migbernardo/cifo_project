import numpy as np
from random import sample, random
from fitness import get_fitness
from selection import fps, tournament, ranking
from cycle_co import shuffle, cycle_co
from mutation import swap_mutation, fitness_mutation


class Solutions:
    def __init__(self, item, num_solutions):
        self.item = item
        self.num_solutions = num_solutions
        self.rep = np.array(item)
        # break puzzle into each respective sub-grid from left to right and top to bottom
        # create a matrix representation of the flat sub-grids
        self.subgrids = np.stack([
            self.rep[:3, :3].flatten(),
            self.rep[:3, 3:6].flatten(),
            self.rep[:3, 6:].flatten(),
            self.rep[3:6, :3].flatten(),
            self.rep[3:6, 3:6].flatten(),
            self.rep[3:6, 6:].flatten(),
            self.rep[6:, :3].flatten(),
            self.rep[6:, 3:6].flatten(),
            self.rep[6:, 6:].flatten()
        ], axis=0)

        # get fixed and non-fixed indexes of each sub-grid
        self.fixed_index = []
        self.not_fixed_index = []
        for row in range(self.subgrids.shape[0]):
            self.fixed_index.append(list(np.where(self.subgrids[row] != 0)[0]))
            self.not_fixed_index.append(list(np.where(self.subgrids[row] == 0)[0]))

        # get fixed numbers of each sub-grid
        self.fixed_num = []
        for row, indexes in enumerate(self.fixed_index):
            num = []
            for index in indexes:
                num.append(self.subgrids[row][index])
            self.fixed_num.append(num)

        # get list of numbers to select for each sub-grid
        self.num_to_sel = []
        for numbers in self.fixed_num:
            pop = list(range(1, 10))
            for number in numbers:
                pop.remove(number)
            self.num_to_sel.append(pop)

        # generate a set of solutions
        self.solutions = []
        for n_sol in range(self.num_solutions):
            sol = self.subgrids.copy()
            # sample list of numbers to select for each sub-grid
            self.sel_num = []
            for numbers in self.num_to_sel:
                self.sel_num.append(sample(numbers, k=len(numbers)))

            # replaced non-fixed positions with selected numbers (generate a solution)
            for row in range(sol.shape[0]):
                for i, index in enumerate(self.not_fixed_index[row]):
                    sol[row][index] = self.sel_num[row][i]
            self.solutions.append(sol)

    def evolve(self, num_generations, selection, elitism, crossover, co_p, mutation, mu_p, t_size=None):
        if self.num_solutions % 2 != 0:
            print('input even num_solutions')
        else:
            for gen in range(num_generations):
                new_sol = []
                if elitism:
                    fitness = []
                    for sol in self.solutions:
                        fitness.append(get_fitness(sol))
                    elite = self.solutions[fitness.index(max(fitness))]

            while len(new_sol) < self.num_solutions:
                # selection
                if selection == 'fps':
                    p1, p2 = fps(self.solutions), fps(self.solutions)
                elif selection == 'tournament':
                    if t_size is None:
                        print('t_size input value missing')
                        break
                    elif t_size > self.num_solutions:
                        print('set t_size <= num_solutions')
                        break
                    else:
                        p1, p2 = tournament(self.solutions, t_size), tournament(self.solutions, t_size)
                elif selection == 'ranking':
                    p1, p2 = ranking(self.solutions), ranking(self.solutions)
                else:
                    print("input a valid selection method: 'fps', 'tournament', 'ranking'")
                    break

                # crossover
                if random() < co_p:
                    if crossover == 'cycle_co':
                        s_p1, s_p2 = shuffle(p1, self.not_fixed_index), shuffle(p2, self.not_fixed_index)
                        c1, c2 = cycle_co(s_p1, s_p2)[0], cycle_co(s_p1, s_p2)[1]
                    elif crossover == 'p_mapped_co':
                        pass
                    else:
                        print("input a valid crossover method: 'cycle_co', 'p_mapped_co'")
                        break
                # create a copy of the parents if crossover doesn't happen (reproduction)
                else:
                    c1, c2 = p1, p2

                # mutation
                if random() < mu_p:
                    if mutation == 'swap':
                        c1 = swap_mutation(c1, self.not_fixed_index)
                    elif mutation == 'fitness_mutation':
                        c1 = fitness_mutation(c1, self.not_fixed_index)
                    else:
                        print("input a valid mutation method: 'swap', 'to be defined'")
                        break
                if random() < mu_p:
                    if mutation == 'swap':
                        c2 = swap_mutation(c2, self.not_fixed_index)
                    elif mutation == 'fitness_mutation':
                        c2 = fitness_mutation(c2, self.not_fixed_index)
                    else:
                        print("input a valid mutation method: 'swap', 'fitness_mutation'")
                        break

                new_sol.append(c1)
                if len(new_sol) < self.num_solutions:
                    new_sol.append(c2)


if __name__ == '__main__':
    puzzle = Solutions(item=[
        [8, 0, 2, 0, 0, 3, 5, 1, 0],
        [0, 6, 0, 0, 9, 1, 0, 0, 3],
        [7, 0, 1, 0, 0, 0, 8, 9, 4],
        [6, 0, 8, 0, 0, 4, 0, 2, 1],
        [0, 0, 0, 2, 5, 8, 0, 6, 0],
        [9, 2, 0, 3, 1, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 2, 7, 8, 0],
        [0, 0, 5, 0, 8, 9, 0, 0, 0],
        [2, 0, 0, 0, 0, 7, 1, 0, 0]
    ], num_solutions=4)

    puzzle.evolve(num_generations=1, elitism=False, selection='ranking')
