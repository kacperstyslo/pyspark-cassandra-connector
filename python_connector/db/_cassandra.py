from functools import wraps
from typing import List, Union

from cassandra import cluster as org_cluster
from cassandra.cluster import Cluster, Session

# Cassandra custom exception
from .exceptions import CassandraNotReadyYet


def wait_for_cassandra() -> List[Union[Cluster, Session]]:
    """
    Try to connect until cassandra is not ready.
    """
    while True:
        try:
            cluster = Cluster(["127.0.0.1"])
            session = cluster.connect()
            return [cluster, session]
        except org_cluster.NoHostAvailable:
            CassandraNotReadyYet()


def db_operator(db_query):
    @wraps(db_query)
    def run_db_query(*args, **kwargs):
        """
        Here query's on cassandra will be executed. Cluster & spark session is already connected
        with Cassandra between containers, fell free to use them here.
        """
        cluster, session = wait_for_cassandra()[0], wait_for_cassandra()[1]
        try:
            session.execute(db_query(*args, **kwargs))
        finally:
            session.shutdown()
            cluster.shutdown()

    return run_db_query
