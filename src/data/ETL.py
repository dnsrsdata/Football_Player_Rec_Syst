# Importing the libraries
import pandas as pd
import numpy as np

import sys
import warnings

warnings.filterwarnings('ignore')


def load_data(passes_filepath_bg5, passes_filepath_eredivisie, passes_filepath_ligaportugal, passes_filepath_brasileiro,
              shoots_filepath_bg5, shoots_filepath_eredivisie, shoots_filepath_ligaportugal, shoots_filepath_brasileiro,
              defense_acts_filepath_bg5, defense_acts_filepath_eredivisie, defense_acts_filepath_ligaportugal,
              defense_acts_filepath_brasileiro, goalkeeping_filepath_bg5, goalkeeping_filepath_eredivisie,
              goalkeeping_filepath_ligaportugal, goalkeeping_filepath_brasileiro):
    """
    Concatenate a list of datasets

    Args:
        passes_filepath_bg5 (str): Path of the file containing the pass data of the big 5 European leagues.
        passes_filepath_eredivisie (str): Path of the file containing the pass data of the Eredivisie.
        passes_filepath_ligaportugal (str): Path of the file containing the pass data of the Primeira Liga.
        passes_filepath_brasileiro (str): Path of the file containing the pass data of the Brasileiro Serie A.
        shoots_filepath_bg5 (str): Path of the file containing the shoot data of the big 5 European leagues.
        shoots_filepath_eredivisie (str): Path of the file containing the shoot data of the Eredivisie.
        shoots_filepath_ligaportugal (str): Path of the file containing the shoot data of the Primeira Liga.
        shoots_filepath_brasileiro (str): Path of the file containing the shoots data of the Brasileiro Serie A.
        defense_acts_filepath_bg5 (str): Path of the file containing the defense acts data of the big 5 European leagues.
        defense_acts_filepath_eredivisie (str): Path of the file containing the defense acts data of the Eredivisie.
        defense_acts_filepath_ligaportugal (str): Path of the file containing the defense acts data of the Primeira Liga.
        defense_acts_filepath_brasileiro (str): Path of the file containing the defense acts data of the Brasileiro Serie A.
        goalkeeping_filepath_bg5 (str): Path of the file containing the goalkeeping data of the big 5 European leagues.
        goalkeeping_filepath_eredivisie (str): Path of the file containing the goalkeeping data of the Eredivisie.
        goalkeeping_filepath_ligaportugal (str): Path of the file containing the goalkeeping data of the Primeira Liga.
        goalkeeping_filepath_brasileiro (str): Path of the file containing the goalkeeping data of the Brasileiro Serie A.

    Returns:
        df_passes: dataset containing all passes data
        df_shoots: dataset containing all shoots data
        df_defense_act: dataset containing all defense acts data
        df_goalkeeping: dataset containing all goalkeeping data
    """
    # Loading passes datasets
    passes_bg5_df = pd.read_csv(passes_filepath_bg5)
    passes_eredivisie_df = pd.read_csv(passes_filepath_eredivisie)
    passes_primeiraL_df = pd.read_csv(passes_filepath_ligaportugal)
    passes_brasileiro_df = pd.read_csv(passes_filepath_brasileiro)

    # Loading shoots datasets
    shoots_bg5_df = pd.read_csv(shoots_filepath_bg5)
    shoots_eredivisie_df = pd.read_csv(shoots_filepath_eredivisie)
    shoots_primeiraL_df = pd.read_csv(shoots_filepath_ligaportugal)
    shoots_brasileiro_df = pd.read_csv(shoots_filepath_brasileiro)

    # Loading defense acts datasets
    defense_acts_bg5_df = pd.read_csv(defense_acts_filepath_bg5)
    defense_acts_eredivisie_df = pd.read_csv(defense_acts_filepath_eredivisie)
    defense_acts_primeiraL_df = pd.read_csv(defense_acts_filepath_ligaportugal)
    defense_acts_brasileiro_df = pd.read_csv(defense_acts_filepath_brasileiro)

    # Loading goalkeeping datasets
    goalkeeping_bg5_df = pd.read_csv(goalkeeping_filepath_bg5)
    goalkeeping_eredivisie_df = pd.read_csv(goalkeeping_filepath_eredivisie)
    goalkeeping_primeiraL_df = pd.read_csv(goalkeeping_filepath_ligaportugal)
    goalkeeping_brasileiro_df = pd.read_csv(goalkeeping_filepath_brasileiro)

    # Creating a col with competition name
    passes_eredivisie_df['Comp'] = 'Eredivisie'
    shoots_eredivisie_df['Comp'] = 'Eredivisie'
    defense_acts_eredivisie_df['Comp'] = 'Eredivisie'
    goalkeeping_eredivisie_df['Comp'] = 'Eredivisie'

    # Creating a col with competition name
    passes_primeiraL_df['Comp'] = 'Primeira Liga'
    shoots_primeiraL_df['Comp'] = 'Primeira Liga'
    defense_acts_primeiraL_df['Comp'] = 'Primeira Liga'
    goalkeeping_primeiraL_df['Comp'] = 'Primeira Liga'

    # Creating a col with competition name
    passes_brasileiro_df['Comp'] = 'Brasileiro Serie A'
    shoots_brasileiro_df['Comp'] = 'Brasileiro Serie A'
    defense_acts_brasileiro_df['Comp'] = 'Brasileiro Serie A'
    goalkeeping_brasileiro_df['Comp'] = 'Brasileiro Serie A'

    # Correcting the Comp column values
    passes_bg5_df['Comp'] = passes_bg5_df['Comp'].str.slice(start=3)
    shoots_bg5_df['Comp'] = shoots_bg5_df['Comp'].str.slice(start=3)
    defense_acts_bg5_df['Comp'] = defense_acts_bg5_df['Comp'].str.slice(start=3)
    goalkeeping_bg5_df['Comp'] = goalkeeping_bg5_df['Comp'].str.slice(start=3)

    # Creating lists with datasets to concatenate
    passes_df_list = [passes_bg5_df, passes_eredivisie_df, passes_primeiraL_df, passes_brasileiro_df]
    shoots_df_list = [shoots_bg5_df, shoots_eredivisie_df, shoots_primeiraL_df, shoots_brasileiro_df]
    defense_act_df_list = [defense_acts_bg5_df, defense_acts_eredivisie_df, defense_acts_primeiraL_df,
                           defense_acts_brasileiro_df]
    goalkeeping_df_list = [goalkeeping_bg5_df, goalkeeping_eredivisie_df, goalkeeping_primeiraL_df,
                           goalkeeping_brasileiro_df]

    # Concatenating data from each category
    df_passes = pd.concat(passes_df_list)
    df_shoots = pd.concat(shoots_df_list)
    df_defense_act = pd.concat(defense_act_df_list)
    df_goalkeeping = pd.concat(goalkeeping_df_list)

    return df_passes, df_shoots, df_defense_act, df_goalkeeping


def joining_datasets(passes_dataframe, shoots_dataframe, defense_dataframe, goalkeeping_dataframe):
    """
    Join the datasets

    Args:
        passes_dataframe (dataframe): dataset containing pass data.
        shoots_dataframe (dataframe): dataset containing shoots data.
        defense_dataframe (dataframe): dataset containing defense actions data.
        goalkeeping_dataframe (dataframe): dataset containing goalkeeping data.

    Returns:
        all_players_data: dataset containing all joined data
    """
    # Renaming the columns
    passes_dataframe = passes_dataframe.rename(columns={'Att': 'Att_Passes'})
    defense_dataframe = defense_dataframe.rename(columns={'Att': 'Att_DefenseActs'})

    # Merging the data
    all_players_data = passes_dataframe.copy()
    df_list = [shoots_dataframe, defense_dataframe, goalkeeping_dataframe]
    for dataset in df_list:
        cols_to_use = dataset.columns.difference(all_players_data.columns).to_list()
        cols_to_use.append('-9999')
        all_players_data = all_players_data.merge(dataset[cols_to_use], how='outer', on='-9999')

    # Removing prefixes on 'Nation' column values
    all_players_data['Nation'] = all_players_data['Nation'].str.slice(start=3)
    all_players_data['Nation'] = all_players_data['Nation'].str.strip()

    # Removing obvious duplicates
    all_players_data = all_players_data.drop_duplicates()

    return all_players_data


def cleaning_data(players_dataset):
    """
    Cleans the data by removing duplicates and trying to calculate missing values

    Args:
        players_dataset (dataframe): dataset containing all data of all players.

    Returns:
        players_dataset: clean dataset, no duplicate data
    """
    # Calculating Cmp%
    players_dataset['Cmp%'] = round((players_dataset.Cmp / players_dataset.Att_Passes) * 100, 1)

    # Calculating Cmp%.1
    players_dataset['Cmp%.1'] = round((players_dataset['Cmp.1'] / players_dataset['Att.1']) * 100, 1)

    # Calculating Cmp%.2
    players_dataset['Cmp%.2'] = round((players_dataset['Cmp.2'] / players_dataset['Att.2']) * 100, 1)

    # Calculating Cmp%.3
    players_dataset['Cmp%.3'] = round((players_dataset['Cmp.3'] / players_dataset['Att.3']) * 100, 1)

    # Calculating A-xAG
    players_dataset['A-xAG'] = round(players_dataset['Ast'] - players_dataset['xAG'], 1)

    # Calculating G-xG
    players_dataset['G-xG'] = round(players_dataset['Gls'] - players_dataset['xG'], 1)

    # Calculating Min
    players_dataset['Min'] = players_dataset['90s'] * 90

    # Calculating G/Sh
    players_dataset['G/Sh'] = round(players_dataset['Gls'] / players_dataset['Sh'], 2)

    # Calculating G/SoT
    players_dataset['G/SoT'] = round(players_dataset['Gls'] / players_dataset['SoT'], 2)

    # Calculating SoT%
    players_dataset['SoT%'] = round((players_dataset['SoT'] / players_dataset['Sh']) * 100, 1)

    # Calculating np:G-xG
    players_dataset['np:G-xG'] = round((players_dataset['Gls'] - players_dataset['PK']) - players_dataset['npxG'], 1)

    # Calculating Lost
    players_dataset['Past'] = round(players_dataset['Att_DefenseActs'] - players_dataset['Tkl.1'], 1)

    # Calculating Tkl%
    players_dataset['Tkl%'] = round((players_dataset['Tkl.1'] / players_dataset['Att_DefenseActs']) * 100, 1)

    # Calculating Tkl+Int
    players_dataset['Tkl+Int'] = round((players_dataset['Tkl'] + players_dataset['Int']), 1)

    # Calculating CS%
    players_dataset['CS%'] = round(players_dataset['GA'] / (players_dataset['Min'] / 90), 1)

    # Calculating Save%
    players_dataset['Save%'] = round((players_dataset['SoTA'] - players_dataset['GA']) / players_dataset['SoTA'], 1)

    # Calculating Save%.1
    players_dataset['Save%.1'] = round((players_dataset['PKsv'] / players_dataset['PKatt']) * 100, 1)

    # Creating a list with column name to remove
    columns_to_remove = ['Rk', 'Nation', 'Starts', 'Comp', 'Born', '90s', 'W', 'D', 'L', 'Matches']

    # Dropping the columns
    players_dataset = players_dataset.drop(columns=columns_to_remove)

    # Renaming the columns
    players_dataset = players_dataset.rename(columns={'-9999': 'id',
                                                      'Past': 'Lost'})
    # Counting and acquiring indexes that appear more than once
    count_ids = players_dataset.id.value_counts()
    greaterThanOneIndexes = count_ids[count_ids > 1].index.to_list()

    # Cleaning up duplicate data
    for identifier in greaterThanOneIndexes:

        # Fetching id records
        records = players_dataset.query(f"id == '{identifier}'").index.to_list()

        # Getting the amount of missing values per row
        sum_nans = players_dataset.query(f"id == '{identifier}'").isna().sum(axis=1)

        # Getting the minimum amount of missing values in records
        min_qtd_nan = players_dataset.query(f"id == '{identifier}'").isna().sum(axis=1).min()

        # Searching for the record with the least amount of NaNs
        indexes_to_explore = sum_nans[sum_nans == min_qtd_nan].index.to_list()

        # Calculating the number of zeros per line
        sum_zeros = players_dataset.loc[indexes_to_explore].isin([0]).sum(axis=1)

        # Getting the least amount of zeros
        min_qtd_zeros = players_dataset.loc[indexes_to_explore].isin([0]).sum(axis=1).min()

        # Getting the index to keep and adding the result to the list
        index_to_keep = sum_zeros[sum_zeros == min_qtd_zeros].index.to_list()

        # Reducing ids number to 1
        if len(index_to_keep) > 1:
            # Adding the row values
            register_sum = players_dataset.loc[index_to_keep].sum(axis=1).sort_values()

            # Getting the index of the record with the highest value and adding the result to the list
            index_to_keep = register_sum.index[-1]

        # Getting index to drop and adding the result to the list
        if isinstance(index_to_keep, list) is True:
            row_to_keep = index_to_keep[0]
        else:
            row_to_keep = index_to_keep

        # Getting indexes to drop
        records.remove(row_to_keep)
        players_dataset = players_dataset.drop(records)

    return players_dataset


def categorize_data(dataset_players):
    """
    Transform numeric data into categorical

    Args:
        dataset_players (dataframe): dataset with player data.

    Returns:
        dataset: dataset with all categorical type data.

    """
    # Dropping the column
    dataset_players = dataset_players.drop(columns='Squad')

    # Copying the dataset
    dataset = dataset_players.copy()

    # Selecting columns by type
    columns = dataset.select_dtypes(['int', 'float']).columns

    # Defining the conditions for categorization
    categorizer_func = lambda x: 0 if x <= q1 else (1 if q1 < x <= q2 else (2 if q2 < x <= q3 else (
        3 if q3 < x <= q4 else (4 if q4 < x <= q5 else (5 if q5 < x <= q6 else (6 if q6 < x else 7))))))

    # Categorizing the data
    for col in columns:
        q1 = np.quantile(dataset[col].dropna(), 0.15)
        q2 = np.quantile(dataset[col].dropna(), 0.30)
        q3 = np.quantile(dataset[col].dropna(), 0.45)
        q4 = np.quantile(dataset[col].dropna(), 0.60)
        q5 = np.quantile(dataset[col].dropna(), 0.75)
        q6 = np.quantile(dataset[col].dropna(), 0.90)
        dataset[col] = dataset[col].apply(categorizer_func)

    return dataset


def data_binarizer(categorized_dataset):
    """
    Transforms categorical data into binary

    Args:
        categorized_dataset (dataframe): dataset with all categorical type data.

    Returns:
        dataset: Dataset containing all binarized data

    """
    # Removing the Player column
    categorized_data = categorized_dataset.drop(columns=['Player'])

    # Setting a new index
    categorized_data = categorized_data.set_index('id')

    # Binarizing the data
    binarized_data = pd.get_dummies(categorized_data, columns=categorized_data.columns)

    return binarized_data


def save_data(dataset, path, filename):
    """
    Save the data in csv format

    Args:
        dataset (dataframe): dataset to save
        path (str): path to save the file
        filename (str): name for the file

    Returns:
        None
    """
    dataset.to_csv(f"{path}/{filename}.csv")
    return None


def main():
    if len(sys.argv) == 17:
        (passes_filepath_bg5, passes_filepath_eredivisie, passes_filepath_ligaportugal, passes_filepath_brasileiro,
         shoots_filepath_bg5, shoots_filepath_eredivisie, shoots_filepath_ligaportugal, shoots_filepath_brasileiro,
         defense_acts_filepath_bg5, defense_acts_filepath_eredivisie, defense_acts_filepath_ligaportugal,
         defense_acts_filepath_brasileiro, goalkeeping_filepath_bg5, goalkeeping_filepath_eredivisie,
         goalkeeping_filepath_ligaportugal, goalkeeping_filepath_brasileiro) = sys.argv[1:]

        print('Loading data......................... \n')
        passes, shoots, defense_acts, goalkeeping = load_data(passes_filepath_bg5,
                                                              passes_filepath_eredivisie,
                                                              passes_filepath_ligaportugal,
                                                              passes_filepath_brasileiro,
                                                              shoots_filepath_bg5,
                                                              shoots_filepath_eredivisie,
                                                              shoots_filepath_ligaportugal,
                                                              shoots_filepath_brasileiro,
                                                              defense_acts_filepath_bg5,
                                                              defense_acts_filepath_eredivisie,
                                                              defense_acts_filepath_ligaportugal,
                                                              defense_acts_filepath_brasileiro,
                                                              goalkeeping_filepath_bg5,
                                                              goalkeeping_filepath_eredivisie,
                                                              goalkeeping_filepath_ligaportugal,
                                                              goalkeeping_filepath_brasileiro)

        print('Joining data..................... \n')
        joined_df = joining_datasets(passes, shoots, defense_acts, goalkeeping)

        print('Cleaning data................... \n')
        cleaned_data = cleaning_data(joined_df)

        print('Saving interim data................ \n')
        save_data(cleaned_data, './data/interim', 'all_players_data_withoutDuplicates')

        print('Categorizing the data................... \n')
        categorized_data = categorize_data(cleaned_data)

        print('Binarizing the data..................... \n')
        binarized_data = data_binarizer(categorized_data)

        print('Saving final data................ \n')
        save_data(binarized_data, './data/processed', 'binarized_data')

    else:
        print('An error occurred, please check if the paths are correct')


if __name__ == '__main__':
    main()
