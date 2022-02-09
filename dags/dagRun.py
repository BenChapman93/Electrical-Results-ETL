from datetime import datetime, timedelta

from src.funcs.database import Database
from src.funcs.completed_checker import get_txt_files, completed_checker
from src.funcs.params_extractors import sample_number_extractor, voltage_extractor, duration_min_extractor, user_extractor, get_mod_date_of_file
from src.funcs.data_extractors import txt_to_df, metrics_generator, summary_generator, parameters_generator

from airflow.models import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

target_dir = "C:/Users/ben.chapman/Desktop/Udemy/Electrical_Results_ETL/mock_files"
processed_dir = ''

default_args = {'owner': 'BC',
                'depends_on_past': False,

                }

def start():
    print('DAG started!')

def eligible_files(dir):

    txt_files = get_txt_files(dir)
    completed_files = [file for file in[*map(completed_checker, txt_files)] if file != None]

    return completed_files

def count_files_branch(ti):

    completed_files = ti.xcom_pull(task_ids= 'get_files')
    
    if len(completed_files) > 0:
        return 'process_files'
    else:
        return 'no_files'

def process_files(ti):

    files = ti.xcom_pull(task_ids= 'get_files')

    print(f'{files} are eligible for processing')


with DAG(
    'elect_test_etl',
    default_args= default_args,
    schedule_interval= '@daily',
    start_date= datetime(2021, 1, 1),
    catchup= False) as dag:

        task_0 = PythonOperator(
            task_id = 'Start',
            python_callable= start,
            dag= dag
        )
        
        get_files = PythonOperator(
            task_id = 'get_files',
            op_args=[target_dir],
            python_callable= eligible_files,
            dag= dag

        )

        count_files = BranchPythonOperator(
            task_id= 'any_files_branch',
            python_callable= count_files_branch
        )

        no_files = BashOperator(
            task_id= 'no_files',
            bash_command= 'echo no files to process'
        )

        process = PythonOperator(
            task_id = 'process_files',
            python_callable= process_files
        )

task_0 >> get_files >> count_files >> [no_files, process]