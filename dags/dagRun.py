from datetime import datetime, timedelta

from src.funcs.database import Database
from src.funcs.completed_checker import get_txt_files, completed_checker
from src.funcs.params_extractors import sample_number_extractor, voltage_extractor, duration_min_extractor, user_extractor, get_mod_date_of_file
from src.funcs.data_extractors import txt_to_df, metrics_generator, summary_generator, parameters_generator

from airflow.models import DAG
from airflow.operators.python import PythonOperator

target_dir = "C:/Users/ben.chapman/Desktop/Udemy/Electrical_Results_ETL/mock_files"

default_args = {'owner': 'BC',
                'depends_on_past': False,

                }

def start():
    print('DAG started!')

def eligible_files(dir):

    txt_files = get_txt_files(dir)
    completed_files = [*map(completed_checker, txt_files)]

    return completed_files

with DAG(
    'electrical_etl_pipeline',
    default_args= default_args,
    schedule_interval= '*/15 * * * *',
    start_date= datetime(2022, 3, 3),
    catchup= False
) as dag:

    task_0 = PythonOperator(
        task_id = 'Start',
        python_callable= start,
        dag= dag
    )
    
    get_files = PythonOperator(
        task_id = 'get_files',
        op_wkargs={'dir': target_dir},
        python_callable= eligible_files,
        dag= dag

    )

task_0 >> get_files
