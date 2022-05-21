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
    plt.ylabel('Average Best Fitness')
    plt.yticks(range(0, 101, 10))
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

    df_crossover = pd.concat([crossover_opco, crossover_tpco])
    df_crossover.sort_values(by='generation', inplace=True)
    df_crossover.reset_index(drop=True, inplace=True)

    sns.lineplot(x='generation', y='fitness', hue='crossover', palette='viridis', data=df_crossover)
    plt.title('Fitness Landscape')
    plt.xlabel('Generations')
    plt.xticks(range(0, 101, 10))
    plt.ylabel('Average Best Fitness')
    plt.yticks(range(0, 71, 10))
    plt.show()

    # MUTATION COMPARISON PLOT
