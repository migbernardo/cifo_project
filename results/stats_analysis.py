import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def group_merge(group_name):
    files = []
    for i in range(10):
        f_name = group_name + f'_{i+1}.csv'
        files.append(pd.read_csv(f_name, header=None))
    return pd.concat(files, axis=0)


if __name__ == '__main__':
    # SELECTION COMPARISON PLOT
    selection_fps = group_merge('selection_test_fps')
    selection_fps.reset_index(inplace=True)
    selection_fps.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    selection_fps['generation'] = selection_fps['generation'].apply(lambda x: x + 1)
    selection_fps['selection'] = 'fps'

    selection_ranking = group_merge('selection_test_ranking')
    selection_ranking.reset_index(inplace=True)
    selection_ranking.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    selection_ranking['generation'] = selection_ranking['generation'].apply(lambda x: x + 1)
    selection_ranking['selection'] = 'ranking'

    selection_tournament = group_merge('selection_test_tournament')
    selection_tournament.reset_index(inplace=True)
    selection_tournament.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    selection_tournament['generation'] = selection_tournament['generation'].apply(lambda x: x + 1)
    selection_tournament['selection'] = 'tournament'

    df_selection = pd.concat([selection_fps, selection_ranking, selection_tournament])
    df_selection.sort_values(by='generation', inplace=True)
    df_selection.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', hue='selection', palette='viridis', data=df_selection)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 101, 10))
    plt.ylabel('Best Fitness')
    plt.yticks(range(0, 101, 10))
    plt.legend().set_title(None)
    plt.show()

    # CROSSOVER COMPARISON PLOT
    crossover_opco = group_merge('crossover_test_tournament_opco')
    crossover_opco.reset_index(inplace=True)
    crossover_opco.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    crossover_opco['generation'] = crossover_opco['generation'].apply(lambda x: x + 1)
    crossover_opco['crossover'] = 'opco'

    crossover_tpco = selection_tournament.copy()
    crossover_tpco['selection'] = crossover_tpco['selection'].apply(lambda x: 'tpco')
    crossover_tpco.rename(columns={'selection': 'crossover'}, inplace=True)

    crossover_f_co = group_merge('crossover_test_tournament_f_co')
    crossover_f_co.reset_index(inplace=True)
    crossover_f_co.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    crossover_f_co['generation'] = crossover_f_co['generation'].apply(lambda x: x + 1)
    crossover_f_co['crossover'] = 'f_co'

    df_crossover = pd.concat([crossover_opco, crossover_tpco, crossover_f_co])
    df_crossover.sort_values(by='generation', inplace=True)
    df_crossover.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', hue='crossover', palette='viridis', data=df_crossover)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 101, 10))
    plt.ylabel('Best Fitness')
    plt.yticks(range(0, 66, 5))
    plt.legend().set_title(None)
    plt.show()

    # MUTATION COMPARISON PLOT
    mutation_2pm = group_merge('mutation_test_tournament_2pm')
    mutation_2pm.reset_index(inplace=True)
    mutation_2pm.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    mutation_2pm['generation'] = mutation_2pm['generation'].apply(lambda x: x + 1)
    mutation_2pm['mutation'] = '2pm'

    mutation_3pm = group_merge('mutation_test_tournament_3pm')
    mutation_3pm.reset_index(inplace=True)
    mutation_3pm.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    mutation_3pm['generation'] = mutation_3pm['generation'].apply(lambda x: x + 1)
    mutation_3pm['mutation'] = '3pm'

    mutation_swap = group_merge('mutation_test_tournament_swap')
    mutation_swap.reset_index(inplace=True)
    mutation_swap.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    mutation_swap['generation'] = mutation_swap['generation'].apply(lambda x: x + 1)
    mutation_swap['mutation'] = 'swap'

    mutation_2swap = group_merge('mutation_test_tournament_2swap')
    mutation_2swap.reset_index(inplace=True)
    mutation_2swap.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    mutation_2swap['generation'] = mutation_2swap['generation'].apply(lambda x: x + 1)
    mutation_2swap['mutation'] = '2swap'

    mutation_inner_swap = group_merge('mutation_test_tournament_inner_swap')
    mutation_inner_swap.reset_index(inplace=True)
    mutation_inner_swap.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    mutation_inner_swap['generation'] = mutation_inner_swap['generation'].apply(lambda x: x + 1)
    mutation_inner_swap['mutation'] = 'inner_swap'

    mutation_rand_mut = group_merge('mutation_test_tournament_rand_mut')
    mutation_rand_mut.reset_index(inplace=True)
    mutation_rand_mut.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    mutation_rand_mut['generation'] = mutation_rand_mut['generation'].apply(lambda x: x + 1)
    mutation_rand_mut['mutation'] = 'rand_mut'

    df_mutation = pd.concat([mutation_2pm, mutation_3pm, mutation_swap, mutation_2swap, mutation_inner_swap,  mutation_rand_mut])
    df_mutation.sort_values(by='generation', inplace=True)
    df_mutation.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', hue='mutation', palette='viridis', data=df_mutation)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 101, 10))
    plt.ylabel('Best Fitness')
    plt.yticks(range(0, 66, 5))
    plt.legend().set_title(None)
    plt.show()

    # EASY PUZZLE COMPARISON PLOT
    easy_opco = group_merge('easy_test_opco')
    easy_opco.reset_index(inplace=True)
    easy_opco.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    easy_opco['generation'] = easy_opco['generation'].apply(lambda x: x + 1)
    easy_opco['crossover'] = 'opco'

    easy_tpco = group_merge('easy_test_tpco')
    easy_tpco.reset_index(inplace=True)
    easy_tpco.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    easy_tpco['generation'] = easy_tpco['generation'].apply(lambda x: x + 1)
    easy_tpco['crossover'] = 'tpco'

    easy_f_co = group_merge('easy_test_f_co')
    easy_f_co.reset_index(inplace=True)
    easy_f_co.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    easy_f_co['generation'] = easy_f_co['generation'].apply(lambda x: x + 1)
    easy_f_co['crossover'] = 'f_co'

    easy_opco_rand_mut = group_merge('easy_test_opco_rand_mut')
    easy_opco_rand_mut.reset_index(inplace=True)
    easy_opco_rand_mut.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    easy_opco_rand_mut['generation'] = easy_opco_rand_mut['generation'].apply(lambda x: x + 1)
    easy_opco_rand_mut['crossover'] = 'opco + rand_mut'

    df_easy = pd.concat([easy_opco, easy_tpco, easy_f_co, easy_opco_rand_mut])
    df_easy.sort_values(by='generation', inplace=True)
    df_easy.reset_index(drop=True, inplace=True)
    df_easy['fitness'] = df_easy['fitness'].apply(lambda x: str(x).split(';;;;')[0]).astype('int')

    sns.lineplot(x='generation', y='fitness', hue='crossover', palette='viridis', data=df_easy)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 101, 10))
    plt.ylabel('Best Fitness')
    plt.yticks(range(0, 51, 5))
    plt.axhline(y=0.0, color='black', linestyle='dotted')
    plt.legend().set_title(None)
    plt.show()

    # VERY HARD PUZZLE PLOTS
    # fitness crossover
    very_hard_opco = group_merge('very_hard_test_opco')
    very_hard_opco.reset_index(inplace=True)
    very_hard_opco.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    very_hard_opco['generation'] = very_hard_opco['generation'].apply(lambda x: x + 1)
    very_hard_opco['crossover'] = 'opco'
    df_very_hard_opco = very_hard_opco.copy()
    df_very_hard_opco.sort_values(by='generation', inplace=True)
    df_very_hard_opco.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', palette='viridis', data=df_very_hard_opco)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 201, 20))
    plt.ylabel('Best Fitness')
    plt.yticks(range(0, 61, 5))
    plt.axhline(y=15.0, color='black', linestyle='dotted')
    plt.show()

    # average fitness function
    very_hard_avg = group_merge('very_hard_test_opco_avg')
    very_hard_avg.reset_index(inplace=True)
    very_hard_avg.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    very_hard_avg['generation'] = very_hard_avg['generation'].apply(lambda x: x + 1)
    very_hard_avg['function'] = 'avg'
    df_very_hard_avg = very_hard_avg.copy()
    df_very_hard_avg.sort_values(by='generation', inplace=True)
    df_very_hard_avg.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', palette='viridis', data=df_very_hard_avg)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 201, 20))
    plt.ylabel('Average Best Fitness')
    plt.yticks(range(0, 21, 2))
    plt.axhline(y=4.0, color='black', linestyle='dotted')
    plt.show()

    # final attempt
    very_hard = group_merge('very_hard_test_opco_avg_500')
    very_hard.reset_index(inplace=True)
    very_hard.rename(columns={'index': 'generation', 0: 'fitness'}, inplace=True)
    very_hard['generation'] = very_hard['generation'].apply(lambda x: x + 1)
    very_hard['function'] = 'avg'
    df_very_hard = very_hard.copy()
    df_very_hard.sort_values(by='generation', inplace=True)
    df_very_hard.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', palette='viridis', data=df_very_hard)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 501, 50))
    plt.ylabel('Average Best Fitness')
    plt.yticks(range(0, 21, 2))
    plt.axhline(y=1.0, color='black', linestyle='dotted')
    plt.show()
