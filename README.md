# datasette-statistics

[![PyPI](https://img.shields.io/pypi/v/datasette-statistics.svg)](https://pypi.org/project/datasette-statistics/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-statistics?include_prereleases&label=changelog)](https://github.com/simonw/datasette-statistics/releases)
[![Tests](https://github.com/simonw/datasette-statistics/workflows/Test/badge.svg)](https://github.com/simonw/datasette-statistics/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-statistics/blob/main/LICENSE)

SQL statistics functions for Datasette

## Installation

Install this plugin in the same environment as Datasette.

    $ datasette install datasette-statistics

## Usage

This plugin adds three new SQL aggregate functions for use within Datasette:

- `statistics_mean()` for calculating the mean
- `statistics_median()` for calculating the median
- `statistics_mode()` for calculating the mode

All three use the implementations from the [Python statistics library](https://docs.python.org/3/library/statistics.html).

Use them like this:

    select statistics_mean(numeric_column) from mytable

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-statistics
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
