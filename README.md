# ETL Workshop - Spotify and Grammy Awards Data Integration

Este proyecto tiene como objetivo procesar y analizar datasets de Spotify y los premios Grammy mediante técnicas de ETL (Extract, Transform, Load). El flujo completo incluye la extracción de datos, transformaciones, carga en bases de datos, visualización de datos y la creación de un tablero en Power BI.

## Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Guía de Inicio](#guía-de-inicio)
  - [Requisitos Previos](#requisitos-previos)
  - [Configuración de la Máquina Virtual](#configuración-de-la-máquina-virtual)
  - [Configuración de PostgreSQL](#configuración-de-postgresql)
- [Instalación](#instalación)
  - [Configuración de la API de Google Drive](#configuración-de-la-api-de-google-drive)
  - [Instalación de Airflow](#instalación-de-airflow)
- [Tablero de Visualización](#tablero-de-visualización)
- [Contacto](#contacto)

## Descripción del Proyecto

Este proyecto tiene dos objetivos principales:
1. Integrar y procesar datos de los datasets de Spotify y los premios Grammy.
2. Proporcionar una visualización útil de las tendencias y características clave de ambos conjuntos de datos a través de un tablero interactivo.

### Fuentes de Datos
1. **Dataset de los Premios Grammy**  
   - Descripción: Información sobre ganadores, nominados y categorías de los premios Grammy a lo largo de los años.

2. **Dataset de Spotify**  
   - Descripción: Más de 114,000 canciones con características como popularidad, energía y duración.

### Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **etl_scripts/**: Contiene los scripts principales de ETL que realizan las operaciones de extracción, transformación y carga.
  - **spotify_etl.py**: Realiza las transformaciones y carga del dataset de Spotify.
  - **grammy_etl.py**: Procesa los datos del dataset de los premios Grammy.
  
- **data/**: Almacena los archivos de datos en formato CSV.
  - **spotify_data.csv**: Dataset de Spotify.
  - **grammy_data.csv**: Dataset de los premios Grammy.

- **notebooks/**: Contiene los análisis exploratorios realizados en Jupyter Notebooks.
  - **eda_spotify.ipynb**: Análisis del dataset de Spotify.
  - **eda_grammy.ipynb**: Análisis del dataset de los premios Grammy.

- **db/**: Scripts SQL para la creación y gestión de la base de datos PostgreSQL.
  - **create_tables.sql**: Define las tablas de la base de datos.
  
- **visualizations/**: Contiene gráficos y visualizaciones generados a partir de los análisis de datos.
  - **spotify_popularity_analysis.png**: Análisis de la popularidad de las canciones en Spotify.
  - **grammy_winners_trends.png**: Tendencias de los ganadores de los premios Grammy.

### Tecnologías Utilizadas
- **Python** (Pandas, SQLAlchemy)
- **PostgreSQL**
- **Apache Airflow**
- **Google Drive API**
- **Power BI**
- **Jupyter Notebook**

## Guía de Inicio

### Requisitos Previos
Antes de comenzar, asegúrate de tener instalados los siguientes programas:

1. **Python 3.x**  
   Descárgalo desde [python.org](https://www.python.org/downloads/).

2. **PostgreSQL**  
   Instálalo desde [postgresql.org](https://www.postgresql.org/download/).

3. **Docker**  
   Para ejecutar el entorno en contenedores, descárgalo desde [docker.com](https://www.docker.com/).

### Configuración de la Máquina Virtual

Para correr el proyecto en una máquina virtual, sigue estos pasos:

1. Crea una nueva máquina virtual usando VirtualBox.
2. Instala Ubuntu LTS en la máquina virtual.
3. Configura el acceso a internet en la VM para poder conectarla a tu máquina local y a internet.

### Configuración de PostgreSQL

Para la configuración de PostgreSQL, realiza lo siguiente:

1. Modifica el archivo `postgresql.conf` para habilitar el acceso desde cualquier IP:
   ```plaintext
   listen_addresses = '*'



## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/MafeTello/workshop2.git
cd workshop2
```

### Configuración del Entorno Python
```bash
  pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

  ```

### Configuración de la API de Google Drive

**Crear Proyecto en Google Cloud**
Accede al Google Cloud Console y crea un nuevo proyecto.

**Habilitar la API de Google Drive**
Navega a "Biblioteca" en Google Cloud y busca la **API de Google Drive**. Habilítala para el proyecto creado.

**Crear Cuenta de Servicio**
1. En el menú de "Credenciales", selecciona "Crear credencial" y elige "Cuenta de servicio".
2. Asigna un nombre a la cuenta de servicio y otórgale los permisos necesarios.
3. Genera una clave de autenticación en formato JSON y descárgala.
4. Renombra el archivo descargado a driveapi.json y colócalo en el directorio raíz del proyecto.

**Compartir Carpeta en Google Drive**
1. Crea una carpeta en Google Drive.
2. Comparte el acceso con la cuenta de servicio utilizando el correo electrónico proporcionado en el archivo JSON.


### Instalación de airflow
1. **Configurar Directorio de Airflow**
Crea un directorio para Airflow y establece la variable de entorno AIRFLOW_HOME:

```bash
export AIRFLOW_HOME=~/airflow
```

2. **Inicializar Base de Datos de Airflow**
```bash
airflow db init
```

3. **Iniciar Airflow**
```bash
airflow standalone
```

4. **Acceso a la Interfaz Web de Airflow**
Abre un navegador y accede a http://localhost:8080. Inicia sesión con las credenciales predeterminadas generadas en la consola.


## Tablero de visulaización

El proyecto incluye un tablero interactivo creado en Power BI, que permite visualizar las principales métricas y tendencias de los datasets de Spotify y los premios Grammy. Algunas preguntas clave que responde el tablero incluyen:

* ¿Cuál es la distribución de la popularidad de las canciones en Spotify?
* ¿Cómo ha cambiado el número de ganadores de los Grammy a lo largo de los años?
* ¿Cuáles son los géneros musicales más representados en Spotify y los premios Grammy?

### Cómo acceder al tablero:
1. Conectar Power BI a PostgreSQL
* En Power BI, selecciona PostgreSQL como la fuente de datos e ingresa las credenciales de tu base de datos.

2. Crear Visualizaciones
* Importa las tablas procesadas en PostgreSQL y utiliza Power BI para generar gráficos y reportes interactivos.

## Contacto
María Fernanda Tello Vergara

Email: _maria_fernanda.tello@uao.edu.co_

GitHub: MafeTello