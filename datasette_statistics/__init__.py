import statistics
import sys

from datasette import hookimpl


def build_aggregate(fn):
    class Aggregate:
        def __init__(self):
            self.values = []

        def step(self, value):
            self.values.append(float(value))

        def finalize(self):
            return float(fn(self.values))

    return Aggregate


@hookimpl
def prepare_connection(conn):
    conn.create_aggregate("statistics_mean", 1, build_aggregate(statistics.mean))
    conn.create_aggregate("statistics_median", 1, build_aggregate(statistics.median))
    conn.create_aggregate(
        "statistics_median_low", 1, build_aggregate(statistics.median_low)
    )
    conn.create_aggregate(
        "statistics_median_high", 1, build_aggregate(statistics.median_high)
    )
    conn.create_aggregate("statistics_mode", 1, build_aggregate(statistics.mode))
    if sys.version_info[:2] >= (3, 8):
        conn.create_aggregate(
            "statistics_geometric_mean", 1, build_aggregate(statistics.geometric_mean)
        )
    conn.create_aggregate("statistics_stdev", 1, build_aggregate(statistics.stdev))
    conn.create_aggregate("statistics_pstdev", 1, build_aggregate(statistics.pstdev))
    conn.create_aggregate(
        "statistics_variance", 1, build_aggregate(statistics.variance)
    )
    conn.create_aggregate(
        "statistics_pvariance", 1, build_aggregate(statistics.pvariance)
    )
