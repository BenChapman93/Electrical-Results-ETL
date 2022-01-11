import os
from datetime import datetime

def sample_number_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        for i in lines[1].split():
            if i.isdigit():
                return int(i)

def voltage_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        for i in lines[2].split():
            try:
                return float(i)
            except:
                pass
            
def duration_min_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        for i in lines[3].split():
            if i.isdigit():
                return int(i)
            
def user_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        return lines[4].split()[1]
    
def get_mod_date_of_file(electrical_data_file):
    epoc_time = os.path.getmtime(electrical_data_file)
    date = datetime.fromtimestamp(epoc_time).strftime('%d-%m-%Y')
    return date