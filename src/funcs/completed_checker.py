from src.funcs.params_extractors import duration_min_extractor, sample_number_extractor
import os
from shutil import copy2

class TempFile():
    
    def __init__(self, path):
        self.path = path
        self.temp_file_path = temp_file_path_generator(path)
        
    def __enter__(self):
        return copy2(self.path, self.temp_file_path)
    
    def __exit__(self, types, value, traceback):
        os.remove(self.temp_file_path)

def get_txt_files(path):
    """Generates a list of absolute file paths corresponding to files withing the path,
       provided they end in .txt.        

    Args:
        path (str): Absolute path to the directory containing files.

    Returns:
        list: A list containing absolute file paths.
    """

    return [os.path.abspath(file) for file in os.listdir(path) if file.endswith('.txt')]

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

def completed_checker(file):

    duration = duration_min_extractor(file)
    sample_number = sample_number_extractor(file)

    if duration != None and sample_number != None:
        
        with TempFile(file) as temp_file:
            with open(temp_file, "r") as f:

                lines = f.readlines()
                last_line = lines[-1].split()
                timestamp = int(last_line[0]) / 60
                completed_channels = len(last_line) - 1

                if duration == timestamp and sample_number == completed_channels:
                    return file
                else:
                    return None
        
    else:
        return None
