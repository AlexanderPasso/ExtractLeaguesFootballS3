# ⚽ Football Leagues ETL with Airflow

Pipeline de **Data Engineering** desarrollado en Python y Apache Airflow para extraer, transformar y almacenar información de tablas de posiciones de diferentes ligas de fútbol.

## 📌 Descripción

El proyecto automatiza un proceso ETL que:

1. Extrae las tablas de posiciones de seis ligas de fútbol.
2. Transforma y estandariza la información utilizando Pandas.
3. Consolida los resultados en un único dataset.
4. Almacena el resultado en **Amazon S3**.
5. Ejecuta el proceso de forma programada mediante **Apache Airflow**.

## 🛠️ Tecnologías

- Python
- Pandas
- Apache Airflow
- Astronomer
- Docker
- Amazon S3
- AWS IAM

## 🏗️ Arquitectura

```text
Fuentes web
     ↓
Apache Airflow
     ↓
Python + Pandas
     ↓
Transformación y consolidación
     ↓
Amazon S3
```

## 📂 Estructura
```text
├── dags/
│   └── demo_leagues/
│       └── demo_leagues.py
├── data/
│   └── df_ligas.csv
├── notebooks/
|   └── football_leagues.ipynb
├── utils.py
├── Dockerfile
├── requirements.txt
└── .gitignore
```