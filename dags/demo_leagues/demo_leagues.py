import json
from datetime import datetime, timedelta
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


import pandas as pd
from utils import data_processing

BUCKET_NAME = "leagues-futboll-s3-bucket"
AWS_CONN_ID = "ExtractLeaguesFootballS3"
CSV_LIGAS = "/usr/local/airflow/data/df_ligas.csv"


def execute_etl():
    df_ligas = pd.read_csv(CSV_LIGAS)
    df_final = data_processing(df_ligas)
    df_final.to_csv(
        "/tmp/tabla_futbol.csv",
        index=False
    )

def upload_s3():
    hook = S3Hook(
        aws_conn_id = AWS_CONN_ID
    )

    hook.load_file(
        filename = "/tmp/tabla_futbol.csv",
        key = "leagues_tables/tabla_futbol.csv",
        bucket_name = BUCKET_NAME,
        replace = True
    )

    print(
        f"Archivo subido correctamente a "
        f"s3://{BUCKET_NAME}/tabla_futbol.csv"
    )

with DAG(
    dag_id ="FOOTBALL_LEAGUES",
    start_date = datetime(2026,9,29),
    schedule = "@daily",
    catchup = False,
) as dag:
    
    task_execute_etl = PythonOperator(
        task_id="execute_etl",
        python_callable = execute_etl
    )

    task_upload_s3 = PythonOperator(
        task_id = "upload_s3",
        python_callable = upload_s3
    )

    task_execute_etl >> task_upload_s3