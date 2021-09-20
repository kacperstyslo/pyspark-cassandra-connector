class CassandraNotReadyYet(Exception):
    """
    Custom cassandra exception. It was created to give the user a clear error message.
    """

    def __str__(self) -> str:
        return "Cassandra cluster probably is not ready yet. Try to connect in a moment."
