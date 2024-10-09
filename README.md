# ETL Workshop - Spotify and Grammy Awards Data Integration

This project aims to process and analyze datasets from Spotify and the Grammy Awards using ETL (Extract, Transform, Load) techniques. The complete flow includes data extraction, transformations, loading into databases, data visualization, and the creation of a dashboard in Power BI.

## Contenidos
- [Project Description](#Project-Description)
  - [Project Structure](#Project-Structure)
  - [Technologies Used](#Technologies-Used)
- [Getting Started Guide](#guía-de-inicio)
  - [Prerequisites](#Prerequisites)
  - [Virtual Machine Configuration](#Virtual-Machine-Configuration)
  - [PostgreSQL Configuration](#PostgreSQL-Configuration)
- [Installation](#Installation)
  - [Google Drive API Configuration](#Google-Drive-API-Configuration)
  - [Airflow Installation](#Airflow-Installation)
- [Dashboard](#Dashboard)
- [contact](#contact)

## Project Description
This project has two main goals:
1. Integrate and process data from the Spotify and Grammy Awards datasets.
2. Provide a useful visualization of key trends and features from both datasets through an interactive dashboard.


### Data Sources
1. **Grammy Awards Dataset**
- Description: Information on Grammy Award winners, nominees, and categories over the years.

2. **Spotify Dataset**
- Description: Over 114,000 songs with characteristics such as popularity, energy, and duration.

### Project Structure

The project is organized into the following folders:

- **etl_scripts/**: Contains the main ETL scripts that perform the extract, transform, and load operations.
  - **spotify_etl.py**:Performs transformations and loading of the Spotify dataset.
  - **grammy_etl.py**:Processes data from the Grammy Awards dataset.
  
- **data/**: Stores data files in CSV format.
  - **spotify_data.csv**: Spotify dataset.
  - **grammy_data.csv**: Grammy Awards dataset.

- **notebooks/**:Contains exploratory analysis performed in Jupyter Notebooks.
  - **eda_spotify.ipynb**: Analysis of the Spotify dataset.
  - **eda_grammy.ipynb**: Analysis of the Grammy Awards dataset.

- **db/**: SQL scripts for creating and managing the PostgreSQL database.
  - **create_tables.sql**: Defines the database tables.
  
- **visualizations/**: Contains graphs and visualizations generated from data analysis.
  - **spotify_popularity_analysis.png**: Analysis of song popularity on Spotify.
  - **grammy_winners_trends.png**: Grammy Award Winners Trends.

### Technologies Used
- **Python** (Pandas, SQLAlchemy)
- **PostgreSQL**
- **Apache Airflow**
- **Google Drive API**
- **Power BI**
- **Jupyter Notebook**

## Getting Started Guide

### Prerequisites
Before you begin, make sure you have the following programs installed:

1. **Python 3.x** Download it from [python.org](https://www.python.org/downloads/).

2. **PostgreSQL** Install it from [postgresql.org](https://www.postgresql.org/download/).

3. **Docker** To run the containerized environment, download it from [docker.com](https://www.docker.com/).

### Virtual Machine Setup

To run the project on a virtual machine, follow these steps:

1. Create a new virtual machine using VirtualBox.
2. Install Ubuntu LTS on the virtual machine.
3. Configure internet access on the VM so that it can connect to your local machine and the internet.

### PostgreSQL Setup

To configure PostgreSQL, do the following:

1. Modify the `postgresql.conf` file to enable access from any IP:
   ```plaintext
   listen_addresses = '*'


## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MafeTello/workshop2.git
cd workshop2
```

### Setting up the Python Environment
```bash
pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

  ```

### Google Drive API Setup

**Create Project in Google Cloud**
Go to the Google Cloud Console and create a new project.

**Enable Google Drive API**
Navigate to "Library" in Google Cloud and find the **Google Drive API**. Enable it for the created project.

**Create Service Account**
1. From the "Credentials" menu, select "Create Credential" and choose "Service Account".
2. Give the service account a name and grant it the necessary permissions.
3. Generate an authentication key in JSON format and download it.
4. Rename the downloaded file to driveapi.json and place it in the root directory of the project.

**Share Folder on Google Drive**
1. Create a folder on Google Drive.
2. Share access with the service account using the email provided in the JSON file.

### Installing airflow
1. **Setting Up Airflow Directory**
Create a directory for Airflow and set the AIRFLOW_HOME environment variable:

```bash
export AIRFLOW_HOME=~/airflow
```

2. **Initialize Airflow Database**
```bash
airflow db init
```

3. **Start Airflow**
```bash
airflow standalone
```
4. **Accessing the Airflow Web Interface**
Open a browser and go to http://localhost:8080. Log in with the default credentials generated in the console.

## Visualization Dashboard

The project includes an interactive dashboard created in Power BI, which allows you to visualize the main metrics and trends of the Spotify and Grammy Awards datasets. Some key questions that the dashboard answers include:

* What is the distribution of song popularity on Spotify?
* How has the number of Grammy winners changed over the years?
* What are the most represented music genres on Spotify and the Grammy Awards?

### How to access the dashboard:
1. Connect Power BI to PostgreSQL
* In Power BI, select PostgreSQL as the data source and enter your database credentials.

2. Create Visualizations
* Import the processed tables into PostgreSQL and use Power BI to generate interactive graphs and reports.

## Contact
María Fernanda Tello Vergara

Email: _maria_fernanda.tello@uao.edu.co_

GitHub: MafeTello