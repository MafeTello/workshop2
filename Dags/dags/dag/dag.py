from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

# Agregar la ruta a los archivos de funciones
sys.path.append("/home/maria-fernanda/Desktop/workshop2/Dags/dags/dag/dag.py") 

# Importar las funciones
from Spotify import ExtractSpotify, task_transform_dropna, task_transform_drop_columns
from Grammys import (
    ExtractGrammys,
    task_transform_drop_duplicates,
    task_transform_drop_columns as grammys_drop_columns,
    task_transform_drop_rows,
)
from Merge import merge_data
from Load import load_to_postgres
#from Store import Store_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'Spotify_Grammys_ETL',
    default_args=default_args,
    description='ETL process for Spotify and Grammys data',
    schedule_interval=timedelta(days=1),
)

def log_task_execution(task_name, **kwargs):
    print(f"Executing task: {task_name}")

with dag:
    # Tareas de Spotify
    extract_spotify_task = PythonOperator(
        task_id='extract_spotify_task',
        python_callable=ExtractSpotify,
        provide_context=True,
    )

    dropna_spotify_task = PythonOperator(
        task_id='task_transform_dropna',
        python_callable=task_transform_dropna,
        provide_context=True,
    )

    drop_columns_spotify_task = PythonOperator(
        task_id='task_transform_drop_columns',
        python_callable=task_transform_drop_columns,
        provide_context=True,
    )

    # Tareas de Grammys
    extract_grammys_task = PythonOperator(
        task_id='extract_grammys_task',
        python_callable=ExtractGrammys,
        provide_context=True,
    )

    drop_duplicates_grammys_task = PythonOperator(
        task_id='task_transform_drop_duplicates',
        python_callable=task_transform_drop_duplicates,
        provide_context=True,
    )

    drop_columns_grammys_task = PythonOperator(
        task_id='task_transform_drop_columns_grammys',
        python_callable=grammys_drop_columns,
        provide_context=True,
    )

    drop_rows_grammys_task = PythonOperator(
        task_id='task_transform_drop_rows',
        python_callable=task_transform_drop_rows,
        provide_context=True,
    )


    # Tarea de Merge
    merge_dataset = PythonOperator(
        task_id='merge_dataset',
        python_callable=merge_data,
        provide_context=True,
    )

    # Tarea de Carga
    load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_to_postgres,
        provide_context=True,
    )

    # Tarea de Almacenamiento en Drive
    Drive_upload = PythonOperator(
        task_id="Drive_upload",
        python_callable=Store_data,
        provide_context=True,
    )

    # Definir dependencias de Spotify
    extract_spotify_task >> dropna_spotify_task >> drop_columns_spotify_task >> merge_dataset

    # Definir dependencias de Grammys

    extract_grammys_task >> drop_duplicates_grammys_task >> drop_columns_grammys_task >> drop_rows_grammys_task >> merge_dataset

    # Dependencias finales
    merge_dataset >> load_data >> Drive_upload