import time
from os import path
from pathlib import Path
from typing import Tuple

from pyspark import SparkContext
from pyspark.sql import SparkSession, dataframe


def __create_spark_operators() -> Tuple[SparkSession, SparkContext]:
    """
    Just create and return Spark Session & Spark Context.
    """
    spark_session = (
        SparkSession.builder.appName("connector_app")
        .master("local[*]")
        .config(
            "spark.sql.catalog.cassandra",
            "com.datastax.spark.connector.datasource.CassandraCatalog",
        )
        .config("spark.cassandra.connection.host", "localhost")
        .getOrCreate()
    )

    spark_context = spark_session.sparkContext
    spark_context.setLogLevel("WARN")

    return spark_session, spark_context


def __create_df_operators(file_name: str, spark_session: SparkSession) -> dataframe.DataFrame:
    """
    Load already saved csv data from Cassandra tables and returning data frames obj.
    """
    local_data = path.join(Path(__file__).resolve().parent.parent, "db", "data", f"{file_name}.csv")
    while not path.exists(local_data):
        time.sleep(1)

    data_frame = spark_session.read.csv(local_data, header=True)
    return data_frame


# Spark operators
spark_operators: Tuple[SparkSession, SparkContext] = __create_spark_operators()
SPARK_SESSION: SparkSession = spark_operators[0]
SPARK_CONTEXT: SparkContext = spark_operators[1]

