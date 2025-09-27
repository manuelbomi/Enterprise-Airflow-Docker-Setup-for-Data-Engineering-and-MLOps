# Enterprise Airflow with Docker

This repository demonstrates how to set up and run **Apache Airflow** in a containerized environment using **Docker** and **Docker Compose**, designed with enterprise-grade applications in mind.  

The setup includes:
- **Airflow Webserver, Scheduler, Worker, and Triggerer**
- **PostgreSQL** as the metadata database
- **Redis** as the message broker
- **Docker Compose orchestration**
- Example **DAGs** for workflow automation

---

## Overview

Apache Airflow is a powerful open-source platform to programmatically author, schedule, and monitor workflows.  
This repository provides a **step-by-step installation guide** with screenshots to help you quickly deploy Airflow locally and adapt it for **enterprise applications** such as:

- Data Engineering Pipelines  
- ETL / ELT Workflows  
- IoT & Sensor Data Processing  
- Machine Learning Model Training & Deployment  
- Enterprise Task Automation  

---

## Repository Structure

   
```ruby
enterprise-airflow-docker-setup/
│── dags/                  # Example DAGs
│── docker-compose.yaml    # Airflow + Postgres + Redis setup
│── logs/                  # Airflow logs
│── plugins/               # Custom plugins (if any)
│── docs/screenshots/      # Installation screenshots
│── README.md              # Project documentation

```

##  Installation

1. Clone the repository
   
   ```bash
   git clone https://github.com/manuelbomi/Enterprise-Airflow-Docker-Setup
   cd enterprise-airflow-docker-setup

2. Start Airflow with Docker Compose
   
   ```ruby
   docker-compose up -d
   ```

3. Access the Airflow Web UI at:
   
 ```ruby
   http://127.0.0.1:8080
 ```
---

## Installation Walkthrough  📷

In a case of the reader preferring to do the Docker installation from ground up, this repository also includes step-by-step installation screenshots that shows installation details and commands used for all the keypoints,listed below:

* Docker Compose configuration (docker-compose.yaml)

* Starting containers (docker ps)

* Accessing the Airflow UI at localhost:8080

* Example DAGs after logging into Airflow

See screenshots and steps by step details below:


#### 1. Create a folder on VSCode

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/f3d6dc11-8e65-4680-b13a-fdd2d114781b" />

---

#### 2.  Ensure that Docker is running on your system, then navigate to the Airflow homepage and if on Linux system, curl the docker compose yaml files

 ```ruby
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.0/docker-compose.yaml'
 ```
If on Windows (Powershell), use the following command:

 ```ruby
  Invoke-WebRequest -Uri "https://airflow.apache.org/docs/apache-airflow/3.1.0/docker-compose.yaml" -OutFile "docker-compose.yaml"

```

(Note: In PowerShell, the curl command is actually an alias for Invoke-WebRequest, and it doesn't understand flags like -LfO)



<img width="1332" height="502" alt="Image" src="https://github.com/user-attachments/assets/60bf3e26-3442-4812-aceb-4c8d78022f0a" />

---

#### 3. After the command, the Airflow docker-compose.yaml file will be created. Go into the yaml file and change **CeleryExecutor** to **LocalExecutor** since we won't need **CeleryExecutor**
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/40236d98-59ff-469c-bfd6-a4c8ac98654e" />

---

#### 4. Create Directory for Dags, Plugins and logs

On Linux, use the command: **mkdir -p ./dags ./logs ./plugins ./config**

On Windows(Powershell), use the command: **New-Item -ItemType Directory -Force -Path .\dags, .\logs, .\plugins, .\config**

<img width="1280" height="480" alt="Image" src="https://github.com/user-attachments/assets/d40fae27-21ab-4e94-b16e-f819d27c74da" />



<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/bec480c4-bb85-49ba-a771-8972b7b19fbc" />

---

#### 5. Now do **docker-compose up airflow-init**

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/516eea35-f218-4094-91af-788199ebba37" />



<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/dac04879-a9f2-41ad-be6c-ef30c4d5b037" />

---

#### 6. **docker compose up -d**    to run the containers in the background. You can also do **docker ps** to see all the containers runing in  your Docker

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/d709f77e-e9be-4051-b1f2-2a76c924c010" />



<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/e267a17c-4d05-4fad-a29d-dbbf76409e34" />

---

#### 7. According to **docker ps** , Airflow is running at 0.0.0.0:8080    on Localhost

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/89c351e4-285f-492a-965f-f451ff93623c" />

---

#### 8. Navigate to 0.0.0.0:8080 and log in with username = 'airflow' , and password = 'airflow'. (Check the docker yaml file to see that the default username and password are 'airflow')

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/06b51b76-8e88-4362-a90e-8230be84b8ab" />

---

#### 9. Some processes running after login


<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/09d3c5bb-ed55-4c92-83ea-2b65ef053c90" />

---



## Next Steps

* Integrate enterprise-grade DAGs (IoT, ML pipelines, ETL flows)

* Deploy on Kubernetes (Airflow on K8s) for scalability

* Add monitoring (Prometheus + Grafana)

* Connect to cloud storage (AWS S3, Azure Blob, or GCS)

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




  
  







