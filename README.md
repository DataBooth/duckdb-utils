# duckdb-utils

[![PyPI](https://img.shields.io/pypi/v/duckdb-utils.svg)](https://pypi.org/project/duckdb-utils/)
[![Changelog](https://img.shields.io/github/v/release/databooth/duckdb-utils?include_prereleases&label=changelog)](https://duckdb-utils.databooth.com.au/en/stable/changelog.html)
[![Python 3.x](https://img.shields.io/pypi/pyversions/duckdb-utils.svg?logo=python&logoColor=white)](https://pypi.org/project/duckdb-utils/)
[![Tests](https://github.com/databooth/duckdb-utils/workflows/Test/badge.svg)](https://github.com/databooth/duckdb-utils/actions?query=workflow%3ATest)
[![Documentation Status](https://readthedocs.org/projects/duckdb-utils/badge/?version=stable)](http://duckdb-utils.databooth.com.au/en/stable/?badge=stable)
[![codecov](https://codecov.io/gh/databooth/duckdb-utils/branch/main/graph/badge.svg)](https://codecov.io/gh/databooth/duckdb-utils)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/databooth/duckdb-utils/blob/main/LICENSE)
[![discord](https://img.shields.io/discord/823971286308356157?label=discord)](https://discord.gg/Ass7bCAMDw)

Python CLI utility and library for manipulating DuckDB databases.

## Some feature highlights

- [Pipe JSON](https://duckdb-utils.databooth.com.au/en/stable/cli.html#inserting-json-data) (or [CSV or TSV](https://duckdb-utils.databooth.com.au/en/stable/cli.html#inserting-csv-or-tsv-data)) directly into a new DuckDB database file, automatically creating a table with the appropriate schema
- [Run in-memory SQL queries](https://duckdb-utils.databooth.com.au/en/stable/cli.html#querying-data-directly-using-an-in-memory-database), including joins, directly against data in CSV, TSV or JSON files and view the results
- [Configure DuckDB full-text search](https://duckdb-utils.databooth.com.au/en/stable/cli.html#configuring-full-text-search) against your database tables and run search queries against them, ordered by relevance
- Run [transformations against your tables](https://duckdb-utils.databooth.com.au/en/stable/cli.html#transforming-tables) to make schema changes that DuckDB `ALTER TABLE` does not directly support, such as changing the type of a column
- [Extract columns](https://duckdb-utils.databooth.com.au/en/stable/cli.html#extracting-columns-into-a-separate-table) into separate tables to better normalize your existing data
- [Install plugins](https://duckdb-utils.databooth.com.au/en/stable/plugins.html) to add custom SQL functions and additional features

Read more on my blog, in this series of posts on [New features in duckdb-utils](https://databooth.com.au/series/duckdb-utils-features/) and other [entries tagged duckdb-utils](https://databooth.com.au/tags/duckdb-utils/).

## Installation

    pip install duckdb-utils

Or if you use [Homebrew](https://brew.sh/) for macOS:

    brew install duckdb-utils

## Using as a CLI tool

Now you can do things with the CLI utility like this:

    $ duckdb-utils memory cats.csv "select * from t"
    [{"id": 1, "age": 4, "name": "Emme"},
     {"id": 2, "age": 2, "name": "Pancakes"}]

    $ duckdb-utils insert cats.duckdb cats cats.csv --csv
    [####################################]  100%

    $ duckdb-utils tables cats.duckdb --counts
    [{"table": "cats", "count": 2}]

    $ duckdb-utils cats.duckdb "select id, name from cats"
    [{"id": 1, "name": "Emme"},
     {"id": 2, "name": "Pancakes"}]

    $ duckdb-utils cats.duckdb "select * from cats" --csv
    id,age,name
    1,4,Emme
    2,2,Pancakes

    $ duckdb-utils cats.duckdb "select * from cats" --table
      id    age  name
    ----  -----  --------
       1      4  Emme
       2      2  Pancakes

You can import JSON data into a new database table like this:

    $ curl https://api.github.com/repos/databooth/duckdb-utils/releases \
        | duckdb-utils insert releases.duckdb releases - --pk id

Or for data in a CSV file:

    $ duckdb-utils insert cats.duckdb cats cats.csv --csv

`duckdb-utils memory` lets you import CSV or JSON data into an in-memory database and run SQL queries against it in a single command:

    $ cat cats.csv | duckdb-utils memory - "select name, age from stdin"

See the [full CLI documentation](https://duckdb-utils.databooth.com.au/en/stable/cli.html) for comprehensive coverage of many more commands.

## Using as a library

You can also `import duckdb_utils` and use it as a Python library like this:

```python
import duckdb_utils
db = duckdb_utils.Database("demo_database.duckdb")
# This line creates a "cats" table if one does not already exist:
db["cats"].insert_all([
    {"id": 1, "age": 4, "name": "Emme"},
    {"id": 2, "age": 2, "name": "Pancakes"}
], pk="id")
```

Check out the [full library documentation](https://duckdb-utils.databooth.com.au/en/stable/python-api.html) for everything else you can do with the Python library.

## Related projects

* [sqlite-utils](https://databooth.com.au/): A tool for SQLite database TODO