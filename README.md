# Workshop 2 - ETL with Airflow and Data Visualization

This project demonstrates an ETL (Extract, Transform, Load) pipeline using datasets from Spotify and the Grammy Awards. The data is processed using Python, Airflow, PostgreSQL, and Google Drive API, and visualized with Power BI.

# ETL - Workshop-02 - Spotify and Grammy Awards Data Process by María Fernanda Tello Vergara

## Table of Contents
- [About The Project](#about-the-project)
  - [Data Source](#data-source)
  - [Folders Path](#folders-path)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Virtual Machine Setup](#virtual-machine-setup)
  - [PostgreSQL](#postgresql)
- [Installation](#installation)
  - [Google Drive API](#google-drive-api)
  - [Airflow](#airflow)
- [Dashboard](#dashboard)

## About The Project

### Data Source
1. **Grammy Awards Dataset**  
   - Source: [Kaggle - Grammy Awards Dataset](https://www.kaggle.com/datasets/unanimad/grammy-awards/)  
   - Description: This dataset includes information about Grammy Award winners, nominees, and categories.

2. **Spotify Tracks Dataset**  
   - Source: [Kaggle - Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)  
   - Description: This dataset includes more than 114,000 tracks from Spotify, providing detailed song features like popularity, danceability, energy, etc.

### Folders Path

The project is organized in the following directory structure:

- **Dags/**  
  - **dag/**  
    - **Grammys.py**: ETL process related to Grammy dataset.
    - **Spotify.py**: ETL process related to Spotify dataset.
    - **Load.py**: Handles loading data into databases.
    - **Merge.py**: Combines the data from both sources (Spotify & Grammy) and applies transformations.

- **Dashboard/**  
  - **Dashboard_workshop2.pdf**: Power BI dashboard related to the project.

- **Document/**  
  - **workshop2.pdf**: Detailed project documentation.

- **Notebooks/**  
  - **EDA_grammy.ipynb**: Exploratory Data Analysis (EDA) for the Grammy dataset.
  - **EDA_spotify.ipynb**: EDA for the Spotify dataset.
  - **charge.py**: Script related to handling dataset transformations.

- **docker/**  
  - **docker-compose.ej.yml**: Docker compose file to set up the project's containerized environment.

- **pyDrive/**  
  - **GoogleDrive.py**: Handles Google Drive API interactions.
  - **QuickStart.py**: Quick setup for Google Drive API usage.

- **src/**  
  - **db_connection.py**: Handles database connections and operations.

- **.gitignore**: Specifies files and folders ignored by Git.
- **README.md**: The documentation file you are currently reading.
- **requirements.txt**: List of Python dependencies required for the project.

### Built With
- Python (Pandas, Matplotlib, SQLAlchemy, dotenv)
- PostgreSQL
- Jupyter Notebook
- Docker
- Apache Airflow
- Google Drive API
- Power BI
- Git

## Getting Started

### Prerequisites
Before running the project, ensure you have the following software installed:
1. **Python 3.12.3** 🐍  
   Install from [Python Official Website](https://www.python.org/downloads/).
   
2. **PostgreSQL** 🐘  
   Download from [PostgreSQL Website](https://www.postgresql.org/download/).
   
3. **Docker** 🐳  
   Install Docker by following instructions from [Docker Website](https://www.docker.com/).
   
4. **Google Drive API**  
   Set up Google Drive API by following the steps in the [Google Drive API documentation](#google-drive-api).

### Virtual Machine Setup
1. **Install Ubuntu**  
   Set up a virtual machine using [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and install the latest Ubuntu LTS version.
   
2. **PostgreSQL Setup**  
   Follow instructions in the [PostgreSQL section](#postgresql) to configure your PostgreSQL instance.

### PostgreSQL

To configure PostgreSQL, perform the following steps:
1. Edit the `postgresql.conf` file to listen on all addresses:  
   ```plaintext
   listen_addresses = '*'

### 1. Clone the Repository

```bash
git clone https://github.com/MafeTello/workshop2.git
cd workshop2


