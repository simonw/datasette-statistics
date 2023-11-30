import sys

from datasette.app import Datasette
import pytest
import pytest_asyncio
import sqlite_utils


@pytest_asyncio.fixture
async def db():
    datasette = Datasette([], memory=True)
    db = datasette.add_memory_database("test")

    def setup(conn):
        sqlite_utils.Database(conn)["numbers"].insert_all(
            {"integers": i, "floats": float(i), "strings": str(i)}
            for i in [10, 10, 11, 12, 13, 14, 15, 15, 15]
        )

    await db.execute_write_fn(setup, block=True)
    return db


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "function,expected",
    (
        ("statistics_mean", pytest.approx(12.777777777777779)),
        ("statistics_median", pytest.approx(13.0)),
        ("statistics_median_low", pytest.approx(13.0)),
        ("statistics_median_high", pytest.approx(13.0)),
        ("statistics_mode", 15),
        ("statistics_pstdev", pytest.approx(1.987615979999813)),
        ("statistics_pvariance", pytest.approx(3.950617283950617)),
        ("statistics_stdev", pytest.approx(2.0015643334421376)),
        ("statistics_variance", pytest.approx(4.0)),
    ),
)
async def test_statistic_functions(db, function, expected):
    if function == "statistics_geometric_mean" and sys.version_info[:2] < (3, 8):
        return

    for column in ("integers", "floats", "strings"):
        result = await db.execute("select {}({}) from numbers".format(function, column))
        assert result.single_value() == expected
