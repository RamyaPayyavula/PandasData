import sys
import pandas as pd
from PandasData.DataLoader import array_loading
from PandasData.MatrixDataLoader import matrix_loading
from PandasData.models import SKBTables
from PandasData.GeneFamily import gene_loading


def usage(argv):
    if len(argv) < 4:
        print("Usage: py database_name table_name in_file_path ")
        print("Example: python main.py test array_table array.tab")
        exit(0)


def main(argv):
    usage(argv)
    database_name = argv[1]
    table_name = argv[2]
    in_file_path = argv[3]

    # Loading data from file
    if in_file_path == "array.tab":
        data_loader = array_loading(in_file_path)
    elif in_file_path == "matrix.tab":
        data_loader = matrix_loading(in_file_path)
    elif in_file_path == "MuFamily.csv":
        data_loader = gene_loading(in_file_path)
    else:
        data_loader = pd.DataFrame()
    # Creating MySQL table based database name and file name
    db_table = SKBTables(database_name)
    db_table.create_skb_table(table_name, data_loader)

    # inserting data into given table in the database
    db_table.insert_table(table_name, data_loader)


if __name__ == "__main__":
    main(sys.argv)