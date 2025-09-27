from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'manuelbomi',
    'retries': 5,
    'retry_delay':timedelta(minutes=2)  # delay time for every retry is 2 minutes
}

with DAG(
    dag_id='new_dag_v5',
    default_args=default_args,
    description='A new DAG',
    start_date=datetime(2019, 9, 3, 2),      # start the DAG at Sept 3, 2019 at 2am
    #schedule_interval='daily'
    schedule='@daily'                        # or a cron string like '0 2 * * *'

) as dag:
    task1 = BashOperator(
        task_id='new_task_1',
        bash_command='echo hello, Airflow is great'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo , hello again, I am taks2, and I will run immediately after task_1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hellooooo, my name is task3, and I am depending on tasks 1 and 2'
    )

## TASK DEPENDENCIES

# task1.set_downstream(task2)
# task1.set_downstream(task3)

### Using bit shit operator
task1 >> task2
task1 >> task3

### COnvert the 2 line bit shift operator into 1

task1 >> [task2, task3]

