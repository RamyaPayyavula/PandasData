from orator import DatabaseManager,Schema

from PandasData.settings import Configuration
import warnings as W
import MySQLdb as Database
""" This function is used to check before creating a primary key value """
W.simplefilter('ignore')

def duplicate_column_valuecheck(data_frame, column_name):
    column_data = data_frame[column_name].tolist()
    lcs = len(column_data)
    res = False
    for i in range(lcs):
        count = 0
        for j in range(lcs):
            if column_data[i] == column_data[j]:
                count = count+1
        if count > 1:
            res = True
            break
    return res


class SKBTables(Configuration):
    """ creating database tables  """

    def __init__(self, database):

        # initializing the configuration
        super(self.__class__, self).__init__()

        self.config['mysql']['database'] = database
        db = DatabaseManager(self.config)

        # define the orator schema builder
        self.schema = Schema(db)
        self.db = db
        self.database = database

    def create_skb_table(self, skb_table_name, data_frame):

        # data frame is empty
        if len(data_frame) < 1:
            return False

        # list of columns
        columns_names = data_frame.columns.values
        self.schema.drop_if_exists(skb_table_name)
        with self.schema.create(skb_table_name) as table:
            # create tables according to the columns in the file and type of columns
            for column_name in columns_names:
                table_column = data_frame[column_name][0]
                # as we have only int float string we are checking for only them
                if column_name == columns_names[0]:
                    if not duplicate_column_valuecheck(data_frame, column_name):
                        table.primary(column_name)
                    else:
                        table.primary([columns_names[0], columns_names[1]])

                if isinstance(table_column, str):
                    table.string(column_name, 50)

                if isinstance(table_column, int):
                    table.integer(column_name, False)

                if isinstance(table_column, bool):
                    table.boolean(column_name)

                if isinstance(table_column, float):
                    table.double(column_name, 10, 6)


        return skb_table_name, data_frame

    """ inserting data into KBC tables """

    def insert_table(self, skb_table_name, data_frame):

        if len(data_frame) < 1:
            return False

        # to_dict method in frame.py convert data frame to dictionary
        data_dict = data_frame.to_dict(orient='records')

        # we need to check whether the table exists or not before inserting data
        if self.schema.has_table(skb_table_name):
            self.db.table(skb_table_name).insert(data_dict)
        else:
            return False
