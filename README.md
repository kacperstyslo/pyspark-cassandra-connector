## Pyspark Cassandra Connector
[![Build Status](https://api.travis-ci.com/kacperstyslo/pyspark-cassandra-connector.svg?branch=master)](https://app.travis-ci.com/github/kacperstyslo/pyspark-cassandra-connector)

# Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
<details>
    <summary>Click here to see general information about application!</summary>
        <br>
       By this app, you can submit pyspark jobs directly into docker containers. 
</details>

## Technologies

<details>
    <summary>Click here to see the technologies used!</summary>
        <ul>
            <li>Python 3.8.5</li>
            <li>Cassandra 3.0</li>
            <li>Hadoop 2.7</li>
            <li>Spark 2.4.5</li>
            <li>PySpark 2.4.5</li>
            <li>Docker 20.10.7</li>
            <li>Docker-compose 1.29.2</li>
        </ul>
</details>

## Setup
<details>
    <summary>Click here to see how to run pyspark jobs in containers!</summary>

```
To setup envoriment:
docker-compose up --build -d cassandra-db; python run.py; docker-compose build

To run existing pyspark jobs (make sure you are running below command in linux shell):
export JOB_NAME="read_spark_config.py"; docker-compose run py-spark

If you add new pyspark job just run:
docker-compose build; export JOB_NAME="example_job.py"; docker-compose run py-spark
```
</details>

