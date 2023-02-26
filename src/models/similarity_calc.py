# Importing the libraries
import sys
import pandas as pd


def load_data(path_binarized_dataset):
    """
    load the data

    Args:
        path_binarized_dataset (str): path with the location of the file with the binarized data

    Returns:
        binarized_data: dataset containing the binarized data
    """

    # Importing the data
    binarized_data = pd.read_csv(f'{path_binarized_dataset}', index_col=0)

    return binarized_data


def similarity_calculation(binarized_dataset):
    """
    Calculates the product of a dataframe, thus obtaining the level of similarity between each player

    Args:
        binarized_dataset (dataframe): dataset containing binary data

    Returns:
        similarity_df: dataset containing similarity between players
    """
    # Calculating the similarity
    similarity_df = binarized_dataset.dot(binarized_dataset.T)
    return similarity_df


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
    if len(sys.argv) == 2:
        binarized_data_path = sys.argv[1]
        print('Loading the data............ \n')
        binarized_data = load_data(binarized_data_path)
        print('Calculating the matrix product............. \n')
        similarity_df = similarity_calculation(binarized_data)
        print('Saving data.................\n')
        save_data(similarity_df, './similarity_results', 'similarity_df')
    else:
        print('An error occurred, please check if the paths are correct')


if __name__ == '__main__':
    main()
