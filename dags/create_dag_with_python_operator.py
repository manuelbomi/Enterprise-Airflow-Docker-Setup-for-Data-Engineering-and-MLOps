from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'manuelbomi',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(name, age):
    print(f"Hello world, my name is {name}, and I am {age} years old.")


with DAG(
    default_args=default_args,
    dag_id='dags_with_python_operator_v3',
    description='using python operator instead of bash operator',
    start_date=datetime(2024, 1, 1),
    schedule='@daily'                        # or a cron string like '0 2 * * *'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name': 'Emma', 'age': 20}
    )

    task1