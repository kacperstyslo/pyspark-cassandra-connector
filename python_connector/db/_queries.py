from . import _cassandra

"""
Write cassandra query here.
"""


@_cassandra.db_operator
def __create_keyspace() -> str:
    """
    Only create example keyspace to make sure if user can connect and do operations on Cassandra.
    """
    return """CREATE KEYSPACE IF NOT EXISTS 
              example_keyspace WITH 
              REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 2};"""


@_cassandra.db_operator
def __create_table(table_name) -> str:
    """
    Only create example table to make sure if user can use created keyspace.
    """
    return f"""
        CREATE
        TABLE
        IF
        NOT
        EXISTS
        example_keyspace.{table_name}
        (
        id         int,
        name       text,
        technology text,
        salary     double,
        PRIMARY KEY (id));"""
