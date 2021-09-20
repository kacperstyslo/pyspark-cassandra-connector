from inspect import cleandoc

from _jobs_operators import SPARK_SESSION


def __read_spark_config() -> str:
    """
    Created to check main Spark setup.
    """
    return cleandoc(
            f"""
          --------- Spark Config ---------
          Name: {SPARK_SESSION.conf.get('spark.app.name')}
          Driver TCP port: {SPARK_SESSION.conf.get('spark.driver.port')}
          Number of partitions: {SPARK_SESSION.conf.get('spark.sql.shuffle.partitions')}
          --------------------------------
    """
        )


print(__read_spark_config())
