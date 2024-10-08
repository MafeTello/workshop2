import pandas as pd
import json
from datetime import datetime

# Configuración del logger
def ExtractGrammys(**kwargs):
    """
    Extrae los datos desde la base de datos Postgres y los convierte a JSON.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando extracción de datos de Grammys")
        query = "SELECT * FROM grammys"
        db_connection = kwargs.get('db_connection')  # Asumiendo que tienes una conexión disponible
        df = pd.read_sql(sql=query, con=db_connection.connection())
        print(f"[{datetime.now()}] - Datos extraídos exitosamente")
        return df.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en ExtractGrammys: {err}")
        raise

def task_transform_drop_duplicates(**kwargs):
    """
    Elimina las filas duplicadas del DataFrame.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando transformación: Eliminando duplicados")
        ti = kwargs['ti']
        json_data = ti.xcom_pull(task_ids='extract_grammys_task')
        df = pd.read_json(json_data, orient="records")
        df_clean = df.drop_duplicates()
        print(f"[{datetime.now()}] - Duplicados eliminados")
        return df_clean.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en task_transform_drop_duplicates: {err}")
        raise

def task_transform_drop_columns(**kwargs):
    """
    Elimina las columnas 'img', 'title', 'updated_at' y 'workers'.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando transformación: Eliminando columnas innecesarias")
        ti = kwargs['ti']
        json_data = ti.xcom_pull(task_ids='task_transform_drop_duplicates')
        df = pd.read_json(json_data, orient="records")
        columns_to_drop = ['img', 'title', 'updated_at', 'workers']
        df.drop(columns=columns_to_drop, inplace=True)
        print(f"[{datetime.now()}] - Columnas eliminadas: {columns_to_drop}")
        return df.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en task_transform_drop_columns: {err}")
        raise

def task_transform_drop_rows(**kwargs):
    """
    Elimina filas específicas basadas en sus índices.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando transformación: Eliminando filas específicas")
        ti = kwargs['ti']
        json_data = ti.xcom_pull(task_ids='task_transform_drop_columns')
        df = pd.read_json(json_data, orient="records")
        rows_to_drop = [2261, 2359, 2454, 2547, 4525, 4573]
        df.drop(index=rows_to_drop, inplace=True, errors='ignore')
        print(f"[{datetime.now()}] - Filas eliminadas: {rows_to_drop}")
        return df.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en task_transform_drop_rows: {err}")
        raise

def task_transform_convert_winner(**kwargs):
    """
    Convierte los valores booleanos de la columna 'winner' a 1 y 0.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando transformación: Convertir 'winner' a 1 y 0")
        ti = kwargs['ti']
        json_data = ti.xcom_pull(task_ids='task_transform_drop_rows')
        df = pd.read_json(json_data, orient="records")
        df['winner'] = df['winner'].map({True: 1, False: 0})
        print(f"[{datetime.now()}] - Conversión completada para la columna 'winner'")
        return df.to_json(orient="records")
    except Exception as err:
        print(f"[{datetime.now()}] - Error en task_transform_convert_winner: {err}")
        raise
