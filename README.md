# Electrical-Results-ETL
A very simple ETL pipeline with the purpose of routinely ingesting .txt files containing raw test data.

The code within this repo is intended as a proof of concept and as an educational project within which to become familiar with ETL tools and processes.

![ETL](https://user-images.githubusercontent.com/45105631/155734326-30f680a9-0cca-48e4-9069-41f6d8d165c8.PNG)

Test results are periodically written to txt files within a known directory - these results contain timestamped resistances, generated by Keithley instruments.
This ETL process is designed to check for completed test files, extract their contents, calculate metrics of interest and store these in a data warehouse. Further analysis of the generated data can be done *via* the dashboard.
 
 ## Set-up
 
 This project is configured for quite a unique usecase; however, should anyone wish to test its features, these are the steps to do so.
 
 ### Prerequisites
 
 - [Docker](https://docs.docker.com/get-docker/)
 - [Docker Compose](https://docs.docker.com/compose/)
 
 ### Airflow
 
 Clone the repository to your desired location.
 
 Should you wish to alter the location of any mounted directories, such as the target directory (where new results files land), you can change the mount location in the Compose file ([docker-compose.yaml](https://github.com/BenChapman93/Electrical-Results-ETL/blob/master/docker-compose.yaml)).
 
 In the repository directory, run the following command:
 ```
 echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
 ```
 This will create the .env file containing the Airflow UID and GID needed by docker-compose.
 
 When using for the first time, run the following command to create an Airflow user and initialise an Airflow instance.
 ```
 docker-compose up airflow-init
 ```
 
 To start all Docker containers corresponding to each service within the Compose file, run the following command:
 
 ```
 docker-compose up
 ```
 
 ### Metabase
 
 Metabase can be ran *via* its official Docker image - run the following command to start a container running Metabase:
 
 ```
 docker run -d -p 3000:3000 \
-v ~/metabase-data:/metabase-data \
-e "MB_DB_FILE=/metabase-data/metabase.db" \
-v [HOST-DB-LOCATION]:/metabase-data/electricaldb
--name metabase metabase/metabase
```
 Ensure that `[HOST-DB-LOCATION]` is set to the location (local) of the sqlite database used by the Airflow dag.
 
 ## Airflow Web UI
 
 Below is an example of the DAG (directed acyclic graph) being triggered manually (scheduled to run every 15 minutes).
 
![Airflow gif](https://user-images.githubusercontent.com/45105631/155702416-788043aa-1224-422b-9220-be4b6de20a41.gif)

From the Graph View we can see the DAG running through each task, according to their dependancies.

## Pipeline Tasks

1. **Start:** DAG begins.
2. **get_files:** A series of checks are performed to determine if a file contains a complete set of test results. Returns any results files that are eligible for processing.
3. **any_files_branch:** A list of eligible files are pulled in *via* Airflow's XCom feature. Path to take is determined by the number of eligible files.
4. **process_files:** Eligible files are ingested - raw data is cleaned and useful metrics are calculated. Results are stored in the database and the raw txt file is relocated.
5. **no_files:** Only runs if there are no eligible files for process.

## Metabase Dashboard

Metabase is an open source data visualisation tool primarily used by analysts for business intelligence. 

![Metabase gif p1](https://user-images.githubusercontent.com/45105631/155730627-f06bb96f-e367-42da-9f13-5a18373b46d9.gif)

This project uses its interactive dashboarding to link dashboards, compare datasets and export results of interest.

![Metabase gif p2](https://user-images.githubusercontent.com/45105631/155732670-88661d12-5c72-4a01-99da-eb8540df8eb8.gif)
