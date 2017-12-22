import pandas as pd

""" this is to load the csv file data """


def array_loading(file_path):
    data_frame = pd.read_csv(file_path, sep="\t")
    result = {}
    if "ID" in data_frame.columns:
        if any(data_frame.duplicated(subset='ID')):
            print("duplicate values in column values")
        else:
            # no duplicate values in columns
            if not (duplicate_columns(data_frame)):
                # no duplicate columns
                if datatype_check(data_frame):
                    # Data types are perfect
                    result = data_frame
            else:
                print("duplicate columns")
    else:

        print("No ID")

    return result


""" Checking for duplicate columns """


def duplicate_columns(frame):
    column_names = frame.columns.tolist()
    lcs = len(column_names)
    res = False
    for i in range(lcs):
        df = frame.filter(like=column_names[i])
        dup = len(df.columns.values.tolist())
        if dup > 1:
            res = True
            break
    return res


""" Checking the data types of the columns in file """


def datatype_check(frame):
    column_names = frame.columns.tolist()
    lcs = len(column_names)
    res = True
    # here object type in pandas is same as string type in native python
    if frame.SNP_ID.dtype == 'object' and frame.Chromosome.dtype == 'int64' and frame.Position.dtype == 'int64' and frame.strand.dtype == 'object' and frame.Ref.dtype == 'object':
        for i in range(5, lcs):
            s = frame.iloc[-1, i:i]
            if s.dtype != 'object':
                res = False
                break
    else:
        res = False
    return res

