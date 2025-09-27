from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'manuelbomi',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

def load_data():
    print("Loading data from source (e.g., database or API)")

def train_model():
    print("Training ML model...")

def evaluate_model():
    print("Evaluating model performance...")

with DAG(
    dag_id='mlops_training_pipeline_v1',
    default_args=default_args,
    description='MLOps pipeline DAG: data loading -> model training -> evaluation',
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['mlops', 'ml', 'training']
) as dag:

    task_load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    task_train = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    task_evaluate = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model
    )

    task_load >> task_train >> task_evaluate
