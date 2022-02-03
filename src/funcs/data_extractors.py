import pandas as pd
import more_itertools as mit
from scipy.stats.mstats import gmean
import os
from src.funcs.params_extractors import sample_number_extractor, user_extractor, voltage_extractor, get_mod_date_of_file, duration_min_extractor

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
        columns = [f'Channel_{str(i)}' for i in range(1, sample_number_extractor(file) + 1)]
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
    channels = [str(i) for i in range(1,len(df.columns) + 1)]
    
    metrics_df = df.agg([func for func in func_list]).T
    metrics_df.insert(0, 'File', file_name)
    metrics_df.insert(1, 'Channel', channels)
    metrics_df.reset_index(drop= True, inplace= True)
        
    return metrics_df

def pass_rate_calculator(df, threshold= 1000000):
    """Takes in a Pandas DataFrame containing raw resistance data and returns an overall pass rate
       (referenced against the threshold value)

    Args:
        df (pandas.DataFrame): DataFrame containing raw resistance data
        threshold (int, optional): Defaults to 1000000.

    Returns:
        float: % pass rate
    """
    if 'File' in df.columns:
        df = df[[col for col in df.columns if col != 'Time' and col != 'File']]

    series = df.apply(last_four_geomean)
    passed = len(series[series > threshold])

    return (passed/len(series)) * 100

def summary_generator(df):
    """Takes in a Pandas DataFrame containing raw resistance data and returns a tuple containing summary data -
       ready for insertion into database.

    Args:
        df (pandas.DataFrame): DataFrame containing raw resistance data

    Returns:
        tuple: Tuple containing summary statistics
    """
    file = df['File'].iloc[0]
    df = df[[col for col in df.columns if col != 'Time' and col != 'File']]
    
    one_Mohms_passrate = pass_rate_calculator(df)
    ten_Mohms_passrate = pass_rate_calculator(df, threshold=10000000)
    onehundred_Mohms_passrate = pass_rate_calculator(df, threshold=100000000)
    
    values = df.values
    
    maximum = values.max()
    minimum = values.min()
    average = values.mean()
    
    return (file, average, maximum, minimum, one_Mohms_passrate, ten_Mohms_passrate, onehundred_Mohms_passrate)

def parameters_generator(file):
    """Returns a tuple of all test parameters associated with the file -
       ready for insertion into database.

    Args:
        file (str): file path

    Returns:
        Tuple: containings data to be inserted into the database
    """
    
    file_path = os.path.abspath(file)
    file_name = file_path.split('\\')[-1]
    
    samples = sample_number_extractor(file_path)
    user = user_extractor(file_path)
    voltage = voltage_extractor(file_path)
    duration = duration_min_extractor(file_path)
    date = get_mod_date_of_file(file_path)
    
    return (file_name, samples, user, voltage, duration, date)