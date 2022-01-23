import pandas as pd
from src.funcs.params_extractors import sample_number_extractor

def total_measurements(column):
    
    return len(column)

def initial_value(column):
    
    return column.iloc[0]

def final_value(column):
    
    return column.iloc[-1]

def total_sub_100MΩ(column):
    
    return len(column[column < 100000000])

def total_sub_10MΩ(column):
    
    return len(column[column < 10000000])

def total_sub_1MΩ(column):
    
    return len(column[column < 1000000])

def max_consec_sub_1MΩ(column):
    
    values_less_than_1MΩ = column[column < 1000000]
    iterable = list(values_less_than_1MΩ.index)
    
    lengths = []
                            
    for a in [list(group) for group in mit.consecutive_groups(iterable)]:
        lengths.append(len(a))

    try:
        return max(lengths)

    except ValueError:
        return 0
    
def time_sub_1MΩ(column):
    
    return total_sub_1MΩ(column) * 20

def minimum_value(column):
    
    return min(column)

def maximum_value(column):
    
    return max(column)

def geomean(column):
    
    return gmean(column)

def last_four_geomean(column):
    
    return gmean(column.tail(4))

def first_four_geomean(column):
    
    return gmean(column.head(4))

def stdev(column):
    
    return column.std()

def txt_to_df(file):
    """A function to convert any text file that contains a completed set of electrical test data to a pandas DataFrame.

    Args:
        file (str): A text file containing a complete set of electrical resistance data

    Returns:
        pandas.DataFrame: A df composed of the raw electrical resistance data
    """
    with open(file, "r") as f:
        lines = f.readlines()
        data = [row.split() for row in lines[7:]]
        columns = [str(i) for i in range(1, sample_number_extractor(file) + 1)]
        columns.insert(0, 'Time')

        df = pd.DataFrame(data, columns= columns).apply(pd.to_numeric)
        df.insert(0, 'File', file.split('\\')[-1])
        
        return df

def metrics_generator(df):
    
    func_list = [total_measurements, initial_value, final_value, total_sub_100MΩ, total_sub_10MΩ, total_sub_1MΩ,
                 max_consec_sub_1MΩ, time_sub_1MΩ, minimum_value, maximum_value, geomean, last_four_geomean,
                first_four_geomean, stdev]
    
    file_name = df['File'].iloc[0]
    df = df[df.columns[2:]]
    
    data = [list(df.apply(func)) for func in func_list]    
    channels = [str(i) for i in range(1,len(df.columns) + 1)]
    
    metrics_df = pd.DataFrame(data).T
    metrics_df.columns = [func.__name__ for func in func_list]
    metrics_df.insert(0, 'File', file_name)
    metrics_df.insert(1, 'Channel', channels)
        
    return metrics_df