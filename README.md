## Computational intelligence for optimization course project 

Repository for storing the course project for the NOVA IMS master course Computational Intelligence for Optimization (academic year 2021/2022)

### Description

This project is about the development of a genetic algorithm implementation to solve sudoku puzzles for learning purposes.

### Repo's structure

```
cifo_project
|
├── content <-------------------------- contains the project's report
|
├── results <-------------------------- contains all .png fitness plots
|
|             ┌── stats_analysis.py <-- script that contains the generation of the stat analysis plots
├── results ──┤
|             └── 'name'.csv <--------- all raw fitness files
|
├── README.md <------------------------ info file
|
├── crossover_v2.py <------------------ script that contains the crossover algorithms
|
├── data.py <-------------------------- script that contains the chosen "easy" and "very hard" puzzles to solve
|
├── fitness_landscape.py <------------- script that contains the function which plots the fitness landscape
|                                       and exports the values to .csv files
|
├── fitness_v2.py <-------------------- script that contains the fitness functions
|
├── ga_v2.py <------------------------- main script of the solver genetic algorithm
|
├── mutation_v2.py <------------------- script that contains the mutation algorithms
|
├── representation.py <---------------- script that contains all the representation functions
|
├── requeriments.txt <----------------- list of all packages used in the project can be installed on the virtual 
|                                       environment with the terminal command: "pip install -r requirements.txt"
|
└── selection_v2.py <------------------ script that contains the selection algorithms
```
