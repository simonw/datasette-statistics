from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-statistics",
    description="SQL statistics functions for Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-statistics",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-statistics/issues",
        "CI": "https://github.com/simonw/datasette-statistics/actions",
        "Changelog": "https://github.com/simonw/datasette-statistics/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_statistics"],
    entry_points={"datasette": ["statistics = datasette_statistics"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "sqlite-utils"]},
    tests_require=["datasette-statistics[test]"],
    python_requires=">=3.6",
)
