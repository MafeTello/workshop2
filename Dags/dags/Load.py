import pandas as pd
import json
from datetime import datetime
import sys
from sqlalchemy.orm import sessionmaker
sys.path.append("/home/maria-fernanda/Desktop/workshop2/src")
sys.path.append("src") 

import db_connection


def load_to_postgres(**kwargs) -> None:
    """
    Carga los datos fusionados a la base de datos Postgres.
    """
    try:
        print(f"[{datetime.now()}] - Iniciando carga de datos a Postgres")
        ti = kwargs['ti']
        
        # Obtener los datos fusionados desde XCom
        merged_json = ti.xcom_pull(task_ids='merge_dataset')
        if not merged_json:
            raise ValueError("No se encontraron datos fusionados en XCom")
        
        # Convertir JSON a DataFrame
        df_merge = pd.read_json(merged_json, orient="records")
        print(f"[{datetime.now()}] - Datos fusionados obtenidos correctamente. Número de registros: {len(df_merge)}")
        
        # Cargar el DataFrame a Postgres
        engine = db_connection.connection()
        Session = sessionmaker(bind=engine)
        session = Session()
        df_merge.to_sql("merge", con=engine, if_exists="replace", index=False)

        print(f"[{datetime.now()}] - Datos cargados exitosamente en la tabla 'merge'")
        
    except Exception as err:
        print(f"[{datetime.now()}] - Error en load_to_postgres: {err}")
        raise
