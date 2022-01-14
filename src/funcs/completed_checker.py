from src.funcs.params_extractors import duration_min_extractor, sample_number_extractor
import os
from shutil import copy2

def temp_file_path_generator(file_path):
    """Function to generate a temporary file path for any .txt file passed.

    Args:
        file_path (str): path of file

    Returns:
        str: a string of the temporary file path.
    """
    
    index = file_path.find(".txt")
    temp_file_path = file_path[:index] + "_temp" + file_path[index:]
    
    return temp_file_path


