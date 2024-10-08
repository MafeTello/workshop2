import pandas as pd
import json
from datetime import datetime

def merge_data(**kwargs):
    """
    Fusiona los datos procesados de Spotify y Grammys.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando la fusión de datos de Spotify y Grammys")
        ti = kwargs['ti']
        
        # Obtener los datos de Spotify desde XCom
        spotify_json = ti.xcom_pull(task_ids='task_transform_drop_columns')
        if not spotify_json:
            raise ValueError("No se encontraron datos de Spotify en XCom")
        df_spotify = pd.read_json(spotify_json, orient="records")
        print(f"[{datetime.now()}] - Datos de Spotify obtenidos correctamente")
        
        # Obtener los datos de Grammys desde XCom
        grammys_json = ti.xcom_pull(task_ids='task_transform_convert_winner')
        if not grammys_json:
            raise ValueError("No se encontraron datos de Grammys en XCom")
        df_grammys = pd.read_json(grammys_json, orient="records")
        print(f"[{datetime.now()}] - Datos de Grammys obtenidos correctamente")
        
        # Realizar la fusión de los DataFrames
        df_merge = pd.merge(df_grammys, df_spotify, left_on="nominee", right_on="track_name", how="inner")
        print(f"[{datetime.now()}] - Fusión de datos completada. Número de registros resultantes: {len(df_merge)}")
        
        # Guardar el DataFrame fusionado como JSON para pasar al siguiente paso
        merged_json = df_merge.to_json(orient="records")
        
        return merged_json
    except Exception as err:
        print(f"[{datetime.now()}] - Error en merge_data: {err}")
        raise
