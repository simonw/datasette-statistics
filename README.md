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

Usage instructions go here.

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
