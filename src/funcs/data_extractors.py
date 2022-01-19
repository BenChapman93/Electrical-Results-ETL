import pandas as pd
from src.funcs.params_extractors import sample_number_extractor

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
        
        return df