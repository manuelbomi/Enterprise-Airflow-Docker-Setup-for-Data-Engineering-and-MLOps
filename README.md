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
































```ruby

- Data Engineering ETL pipelines

- MLOps workflows

- Enterprise orchestration

- CI/CD with GitHub Actions for validation and testing

```
---




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




  
  







