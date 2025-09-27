# Enterprise Airflow Docker Setup for Data Engineering & MLOps

This repository provides a robust, production-grade Apache Airflow environment using Docker Compose, designed for building and running complex data engineering pipelines, CI and MLOps workflows. 


#### The repository is complete with templates and examples for:

🐳 Dockerized Apache Airflow with LocalExecutor

- Enterprise orchestration

- MLOps workflow

- Data Engineering ETL

✅ CI/CD with GitHub Actions for validation and testing :

- DAG syntax validation

- Unit tests with pytest

- Function argument passing (op_kwargs)

- DAG templates for: BashOperator & PythonOperator

🔁 Retry logic and task dependencies

-  Visual monitoring through Airflow Web UI
  
- Plug-and-play template structure for fast development

- DAG status visualization via the Airflow UI

🧰 Production-ready and extensible

---


* The examples and templates provided are designed to be production-scalable, developer-friendly, and ready to integrate into large-scale data platforms and ML environments.


## Project Structure 📁


```ruby

enterprise-airflow-docker-setup/
├── config/                         # Custom configs (e.g., airflow.cfg)
├── dags/                           # DAG definition files
│   ├── new_dag_v5.py                      # BashOperator example
│   ├── dags_with_python_operator_v3.py    # PythonOperator example
│   ├── mlops_training_pipeline.py         # MLOps pipeline DAG
│   └── data_engineering_etl_pipeline.py   # Data Engineering ETL DAG
├── logs/                           # Runtime logs (auto-generated)
├── plugins/                        # Optional custom plugins
├── snapshots/                      # Screenshots of DAGs (optional)
├── tests/                          # Unit tests for DAGs/functions
│   └── test_dag_import.py
├── .env                            # Environment variables
├── .gitignore
├── LICENSE
├── docker-compose.yaml             # Docker setup for Airflow
└── README.md                       # You are right here!

```
---


## Getting Started

* Set up the Docker environment and Airflow automatically by using the repository here:  https://github.com/manuelbomi/Enterprise-Airflow-with-Docker

### 1. Clone the Repository

```ruby

git clone https://github.com/manuelbomi/Enterprise-Airflow-Docker-Setup-for-Data-Engineering-and-MLOps.git

cd enterprise-airflow-docker-setup

```

### 2 Set Environment Variables

* Create a .env file at the root with:

```ruby
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__CORE__FERNET_KEY=your_fernet_key

```

### 3. Start the Airflow Environment


```ruby
docker compose up airflow-init

docker-compose up -d

```

### 4. Access the Airflow UI

* Do <ins> docker ps </ins> to see the containers running in your Docker. 

* Open Airflow at:  http://localhost:8080

* <ins> Default Username </ins>: airflow 

* <ins> Default Password </ins>: airflow

---

### Included DAG Templates (all are ready to run out of the box for your enterprise projects)

🔧 1. new_dag_v5.py — BashOperator

Simple task flow using shell commands and Airflow's retry features.

🐍 2. dags_with_python_operator_v3.py — PythonOperator

Pass parameters to Python functions with Airflow logging.

🤖 3. mlops_training_pipeline.py — MLOps Workflow

Typical ML lifecycle: load data → train model → evaluate results.

🏗️ 4. data_engineering_etl_pipeline.py — ETL Flow

Data engineering pipeline: extract → transform → load.

---

### CI/CD Integration (GitHub Actions)  🧪 

 <ins> 1. DAG Syntax Validation </ins>

* .github/workflows/airflow-dag-validation.yml

* Parses all DAGs

* Fails CI if any DAG has import errors

* See file: .github/workflows/airflow-dag-validation.yml
  

<ins>2. Unit Testing with Pytest</ins>

* .github/workflows/python-tests.yml

* Runs pytest on DAGs and callable logic

* Test example: test_dag_import.py

Run tests locally with:


```ruby
pytest tests/

```

---

## How to Use in Your Own Projects 🛠️ 

* Clone this repo

* Replace existing DAGs with your logic *or* extend the existing DAGs

* Add custom operators, sensors, or hooks in the plugins/ folder

* Connect to production databases or clouds using .env and Airflow's Connections UI (see Airflow UI snapshots in the snapshot folder in this repo)

* Customize the docker-compose.yaml to run on your infra (e.g., add CeleryExecutor)

---

## Enterprise Use Cases  💼 

✅ Data Engineering

- Automate daily, hourly, or real-time ETL

- Ingest CSV/JSON files into warehouses

- Use Python or SQL transforms

✅ MLOps Pipelines

- Chain training, evaluation, and deployment

- Trigger ML pipelines on new data arrival

- Use Airflow with MLflow, SageMaker, etc.

✅ Enterprise Orchestration

- Schedule legacy system jobs

- Chain REST APIs or shell commands

- Alert on failures, retries, and SLA misses

































Thank you for reading
  

### **AUTHOR'S BACKGROUND**
### Author's Name:  Emmanuel Oyekanlu
```
Skillset:   I have experience spanning several years in data science, developing scalable enterprise data pipelines,
enterprise solution architecture, architecting enterprise systems data and AI applications,
software and AI solution design and deployments, data engineering, high performance computing (GPU, CUDA), IoT applications,
machine learning, MLOps, NLP, Agentic-AI and LLM applications as well as deploying scalable solutions (apps) on-prem and in the cloud.

I can be reached through: manuelbomi@yahoo.com

Websites (professional):  http://emmanueloyekanlu.com/
Websites (application):  https://app.emmanueloyekanluprojects.com/
Publications:  https://scholar.google.com/citations?user=S-jTMfkAAAAJ&hl=en
LinkedIn:  https://www.linkedin.com/in/emmanuel-oyekanlu-6ba98616
Github:  https://github.com/manuelbomi

```
[![Icons](https://skillicons.dev/icons?i=aws,azure,gcp,scala,mongodb,redis,cassandra,kafka,anaconda,matlab,nodejs,django,py,c,anaconda,git,github,mysql,docker,kubernetes&theme=dark)](https://skillicons.dev)




  
  







