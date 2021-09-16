from datasette import hookimpl
import statistics


def build_aggregate(fn):
    class Aggregate:
        def __init__(self):
            self.values = []

        def step(self, value):
            self.values.append(value)

        def finalize(self):
            return fn(self.values)

    return Aggregate


@hookimpl
def prepare_connection(conn):
    conn.create_aggregate("statistics_mean", 1, build_aggregate(statistics.mean))
    conn.create_aggregate("statistics_median", 1, build_aggregate(statistics.median))
    conn.create_aggregate("statistics_mode", 1, build_aggregate(statistics.mode))
