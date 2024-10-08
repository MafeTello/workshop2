# Workshop 2 - ETL with Airflow and Data Visualization

This project demonstrates an ETL (Extract, Transform, Load) pipeline using datasets from Spotify and the Grammy Awards. The data is processed using Python, Airflow, PostgreSQL, and Google Drive API, and visualized with Power BI.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.12.3
- Docker
- PostgreSQL
- Apache Airflow 2.10.1
- Power BI (for visualization)
- Google Drive API enabled for your Google Cloud project

## Project Structure

- **dags/**: Contains the Airflow DAGs (Directed Acyclic Graphs) for managing the workflow.
- **scripts/**: Python scripts for data extraction, transformation, and loading.
- **visualizations/**: Power BI visualizations of the processed data.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MafeTello/workshop2.git
cd workshop2


