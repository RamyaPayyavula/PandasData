import pandas as pd

""" this is to load the csv file data """


def gene_loading(file_path):
    data_frame = pd.read_csv(file_path, sep=",")
    column_names = data_frame.columns.tolist()
    lcs = len(column_names)
    if lcs == 2:
        result = data_frame
    else:
        result = pd.DataFrame()
    return result


gene_loading("MuFamily.csv")