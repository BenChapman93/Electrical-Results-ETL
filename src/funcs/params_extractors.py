import os
from datetime import datetime

def sample_number_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        try:
            for i in lines[1].split():
                if i.isdigit():
                    return int(i)
        except:
            return None
                
def voltage_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        try:
            voltage = lines[2].split()[1]
            return float(voltage)
                
        except:
            return None
            
def duration_min_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        try:
            for i in lines[3].split():
                if i.isdigit():
                    return int(i)
        except:
            return None
            
def user_extractor(electrical_data_file):
    with open(electrical_data_file) as file:
        lines = file.readlines()
        try:
            if lines[4].split()[0] == 'User:':
                return lines[4].split()[1]
            else:
                return None
        except:
            return None
    
def get_mod_date_of_file(electrical_data_file):
    epoc_time = os.path.getmtime(electrical_data_file)
    date = datetime.fromtimestamp(epoc_time).strftime('%d-%m-%Y')
    return date