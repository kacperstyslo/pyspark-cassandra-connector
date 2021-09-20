from ._cassandra import wait_for_cassandra

from ._queries import __create_table, __create_keyspace


def prepare_cassandra() -> None:
    """
    Cassandra is implemented in this project to abel user to store data.
    """
    __create_keyspace()
    __create_table("example_table_name")
