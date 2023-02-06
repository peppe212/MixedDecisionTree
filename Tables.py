import pandas as pd
import re
import os


def _max_depth_varies(couple, tree_type, criterion, mode, bins, mss, msl):
    # leggo il nome dei file .csv appartenenti allo stesso dataset su cui andrò ad effettuare l'analisi
    mixed_csv = couple[0]
    sklearn_csv = couple[1]

    # dataset name:
    temp_ds_name = re.split('/', couple[0])[1]
    ds_name = re.split('_', temp_ds_name)[0]

    # distinguo i due alberi
    if tree_type == 'MixedDecisionTree':
        df = pd.read_csv(mixed_csv)
    elif tree_type == 'SklearnDT':
        df = pd.read_csv(sklearn_csv)
    else:
        raise Exception("Wrong Decision Tree name...")
    df.insert(0, 'DATASET', ds_name)
    df.insert(1, 'DT_TYPE', tree_type)

    # qui parte la query
    if mode != 'classic':
        df_queried = df[(df['Tree_Mode'] == mode) & (df['Criterion'] == criterion)
                        & (df['Bins'] == bins) & (df['Min_sample_split'] == mss) &
                        (df['Min_sample_leaf'] == msl)]
    else:
        if bins != 20:
            return
        else:
            bins = 0
            df_queried = df[(df['Tree_Mode'] == mode) & (df['Criterion'] == criterion)
                            & (df['Bins'] == bins) & (df['Min_sample_split'] == mss) &
                            (df['Min_sample_leaf'] == msl)]
        # end_if
    # end_if

    # CREO LE DIRECTORIES dove andare a salvare le tabelle:
    dir_path = 'Tables/' + ds_name + '/'
    try:
        os.makedirs(dir_path, exist_ok=True)
    except OSError as error:
        print(error)
        print("Path '%s' can not be created" % dir_path)

    table_path = dir_path + 'max_depth_varies.csv'
    df_queried.to_csv(table_path, index=False, header=True, mode='a')

    return


def _msl_varies(couple, tree_type, criterion, mode, bins, max_depth, mss):
    # leggo il nome dei file .csv appartenenti allo stesso dataset su cui andrò ad effettuare l'analisi
    mixed_csv = couple[0]
    sklearn_csv = couple[1]

    # dataset name:
    temp_ds_name = re.split('/', couple[0])[1]
    ds_name = re.split('_', temp_ds_name)[0]

    # distinguo i due alberi
    if tree_type == 'MixedDecisionTree':
        df = pd.read_csv(mixed_csv)
    elif tree_type == 'SklearnDT':
        df = pd.read_csv(sklearn_csv)
    else:
        raise Exception("Wrong Decision Tree name...")
    df.insert(0, 'DATASET', ds_name)
    df.insert(1, 'DT_TYPE', tree_type)

    # qui parte la query
    if mode != 'classic':
        df_queried = df[(df['Min_sample_split'] > df['Min_sample_leaf']) &
                        (df['Tree_Mode'] == mode) & (df['Criterion'] == criterion)
                        & (df['Bins'] == bins) & (df['Max_Depth'] == max_depth)
                        & (df['Min_sample_split'] == mss)]
    else:
        if bins != 20:
            return
        else:
            bins = 0
            df_queried = df[(df['Min_sample_split'] > df['Min_sample_leaf']) &
                            (df['Tree_Mode'] == mode) & (df['Criterion'] == criterion)
                            & (df['Bins'] == bins) & (df['Max_Depth'] == max_depth)
                            & (df['Min_sample_split'] == mss)]
        # end_if
    # end_if

        # CREO LE DIRECTORIES dove andare a salvare le tabelle:
        dir_path = 'Tables/' + ds_name + '/'
        try:
            os.makedirs(dir_path, exist_ok=True)
        except OSError as error:
            print(error)
            print("Path '%s' can not be created" % dir_path)

        table_path = dir_path + 'min_sample_leaf_varies.csv'
        df_queried.to_csv(table_path, index=False, header=True, mode='a')

    return


def _mss_varies(couple, tree_type, criterion, mode, bins, max_depth, msl):
    # leggo il nome dei file .csv appartenenti allo stesso dataset su cui andrò ad effettuare l'analisi
    mixed_csv = couple[0]
    sklearn_csv = couple[1]

    # dataset name:
    temp_ds_name = re.split('/', couple[0])[1]
    ds_name = re.split('_', temp_ds_name)[0]

    # distinguo i due alberi
    if tree_type == 'MixedDecisionTree':
        df = pd.read_csv(mixed_csv)
    elif tree_type == 'SklearnDT':
        df = pd.read_csv(sklearn_csv)
    else:
        raise Exception("Wrong Decision Tree name...")
    df.insert(0, 'DATASET', ds_name)
    df.insert(1, 'DT_TYPE', tree_type)

    # qui parte la query
    if mode != 'classic':
        df_queried = df[(df['Min_sample_split'] > df['Min_sample_leaf']) &
                        (df['Tree_Mode'] == mode) & (df['Criterion'] == criterion)
                        & (df['Bins'] == bins) & (df['Max_Depth'] == max_depth)
                        & (df['Min_sample_leaf'] == msl)]
    else:
        if bins != 20:
            return
        else:
            bins = 0
            df_queried = df[(df['Min_sample_split'] > df['Min_sample_leaf']) &
                            (df['Tree_Mode'] == mode) & (df['Criterion'] == criterion)
                            & (df['Bins'] == bins) & (df['Max_Depth'] == max_depth)
                            & (df['Min_sample_leaf'] == msl)]
        # end_if
    # end_if

    # CREO LE DIRECTORIES dove andare a salvare le tabelle:
    dir_path = 'Tables/' + ds_name + '/'
    try:
        os.makedirs(dir_path, exist_ok=True)
    except OSError as error:
        print(error)
        print("Path '%s' can not be created" % dir_path)

    table_path = dir_path + 'min_sample_split_varies.csv'
    df_queried.to_csv(table_path, index=False, header=True, mode='a')

    return


def max_depth_varies(couples_list, tree_type_list, criterion_list, tree_mode_list, bins_list,
                     mss_list, msl_list):
    for couple in couples_list:
        for criterion in criterion_list:
            for mode in tree_mode_list:
                for bins in bins_list:
                    for mss in mss_list:
                        for msl in msl_list:
                            for tree_type in tree_type_list:
                                if mss > msl:
                                    _max_depth_varies(couple, tree_type, criterion, mode, bins, mss, msl)

    return


def msl_varies(couples_list, tree_type_list, criterion_list, tree_mode_list, bins_list, max_depth_list,
               mss_list):
    for couple in couples_list:
        for criterion in criterion_list:
            for mode in tree_mode_list:
                for bins in bins_list:
                    for max_depth in max_depth_list:
                        for mss in mss_list:
                            for tree_type in tree_type_list:
                                if mss < 10:
                                    continue
                                else:
                                    _msl_varies(couple, tree_type, criterion, mode, bins, max_depth, mss)

    return


def mss_varies(couples_list, tree_type_list, criterion_list, tree_mode_list, bins_list, max_depth_list,
               msl_list):
    for couple in couples_list:
        for criterion in criterion_list:
            for mode in tree_mode_list:
                for bins in bins_list:
                    for max_depth in max_depth_list:
                        for msl in msl_list:
                            for tree_type in tree_type_list:
                                if msl > 5:
                                    continue
                                else:
                                    _mss_varies(couple, tree_type, criterion, mode, bins, max_depth, msl)

    return


def main():
    print("Qui verranno generate tabelle e grafici per ogni dataset")
    print("Lo scopo è di visualizzare le differenze più importanti tra il mio MDT e il DT di Sklearn")
    folder_name = 'Results/'
    #                 prima coppia
    couples_list = [(folder_name + 'Iris_Mixed_DT_result.csv',
                     folder_name + 'Iris_Sklearn_DT_result.csv'),
                    # seconda coppia
                    (folder_name + 'breast-cancer_Mixed_DT_result.csv',
                     folder_name + 'breast-cancer_Sklearn_DT_result.csv'),
                    # terza coppia
                    (folder_name + 'Carseats_Mixed_DT_result.csv',
                     folder_name + 'Carseats_Sklearn_DT_result.csv'),
                    # quarta coppia
                    (folder_name + 'diabetes_Mixed_DT_result.csv',
                     folder_name + 'diabetes_Sklearn_DT_result.csv'),
                    # quinta coppia
                    (folder_name + 'HouseVotes84_Mixed_DT_result.csv',
                     folder_name + 'HouseVotes84_Sklearn_DT_result.csv'),
                    # sesta coppia
                    (folder_name + 'prostate_Mixed_DT_result.csv',
                     folder_name + 'prostate_Sklearn_DT_result.csv'),
                    # settima coppia
                    (folder_name + 'parkinsons_Mixed_DT_result.csv',
                     folder_name + 'parkinsons_Sklearn_DT_result.csv'),
                    # ottava coppia
                    (folder_name + 'Sacramento_Mixed_DT_result.csv',
                     folder_name + 'Sacramento_Sklearn_DT_result.csv'),
                    # nona coppia
                    (folder_name + 'Auto_Mixed_DT_result.csv',
                     folder_name + 'Auto_Sklearn_DT_result.csv'),
                    # decima coppia
                    (folder_name + 'churn_Mixed_DT_result.csv',
                     folder_name + 'churn_Sklearn_DT_result.csv')]  # end list

    tree_type_list = ['MixedDecisionTree', 'SklearnDT']
    tree_mode_list = ['classic', 'median', 'binned']
    criterion_list = ['entropy', 'gini']
    bins_list = [20, 11]  # [20,15,11,7] ma ho sovuto accorciarla
    max_depth_list = [2, 3, 4, 5, 6, 7, 8, 25]  # [2,3,4,5,6,7,8,25] ho tolto il valore 50
    mss_list = [2, 3, 5, 10, 25, 50]  # min_sample_split list
    msl_list = [1, 3, 5, 10, 25, 50]  # min_sample_leaf list

    max_depth_varies(couples_list, tree_type_list, criterion_list, tree_mode_list, bins_list, mss_list, msl_list)
    msl_varies(couples_list, tree_type_list, criterion_list, tree_mode_list, bins_list, max_depth_list, mss_list)
    mss_varies(couples_list, tree_type_list, criterion_list, tree_mode_list, bins_list, max_depth_list, msl_list)

    return


# ovviamente quando varia mss, e quindi tengo fissi depth e msl, quando msl vale 25 ho un punto solo
# quando msl vale 50 ho zero punti sulla tabella, quindi queste tab elle non voglio che si creino

# stesso discorso a specchio si può fare quando varia msl, per valori di mss < 10 non ho più casi interessanti
if __name__ == '__main__':
    main()

"""
TABELLA CHE DESCRIVE I DATASETS: 
descrizione sommaria della tabella che descrive i datasets
numero di colonne contine, numero di colonne categoriche, numero di classi, descrizione dei dataset basta una riga, 
nel nome dei dataset devo togliere il .csv metto solo il nome senza l'estensione.

TABELLE DELLE PERFORMANCE dei peaks and sinks:
mi devo fare 2 file per tipo di albero, una tabella per i peaks e una per i sinks dove uso tutti i datasets
verranno parecchie righe, io da quelle righe mi faccio le viste che ritengo opportune creando configurazioni 
di parametri interessanti.
metto colonne:

"""
