import pandas as pd
import json
from datetime import datetime

# Configuración del logger
def ExtractSpotify(**kwargs):
    """
    Extrae los datos desde un archivo CSV y los convierte a JSON.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando extracción de datos de Spotify")
        df = pd.read_csv("/home/maria-fernanda/Desktop/workshop2/Data/spotify_dataset.csv")
        print(f"[{datetime.now()}] - Datos extraídos exitosamente")
        return df.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en ExtractSpotify: {err}")
        raise

def task_transform_dropna(**kwargs):
    """
    Elimina las filas con datos nulos.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando transformación: Eliminando nulos")
        ti = kwargs['ti']
        json_data = ti.xcom_pull(task_ids='extract_spotify_task')
        df = pd.read_json(json_data, orient="records")
        df_clean = df.dropna()
        print(f"[{datetime.now()}] - Filas nulas eliminadas")
        return df_clean.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en task_transform_dropna: {err}")
        raise

def task_transform_drop_columns(**kwargs):
    """
    Elimina las columnas 'Unnamed: 0' y 'track_id'.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando transformación: Eliminando columnas innecesarias")
        ti = kwargs['ti']
        json_data = ti.xcom_pull(task_ids='task_transform_dropna')
        df = pd.read_json(json_data, orient="records")
        df.drop(columns=["Unnamed: 0", "track_id"], inplace=True)
        print(f"[{datetime.now()}] - Columnas eliminadas")
        return df.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en task_transform_drop_columns: {err}")
        raise
