.. _cli_reference:

===============
 CLI reference
===============

This page lists the ``--help`` for every ``duckdb-utils`` CLI sub-command.

.. contents:: :local:
   :class: this-will-duplicate-information-and-it-is-still-useful-here

.. [[[cog
    from duckdb_utils import cli
    import sys
    sys._called_from_test = True
    from click.testing import CliRunner
    import textwrap
    commands = list(cli.cli.commands.keys())
    go_first = [
        "query", "memory", "insert", "upsert", "bulk", "search", "transform", "extract",
        "schema", "insert-files", "analyze-tables", "convert", "tables", "views", "rows",
        "triggers", "indexes", "create-database", "create-table", "create-index",
        "enable-fts", "populate-fts", "rebuild-fts", "disable-fts"
    ]
    refs = {
        "query": "cli_query",
        "memory": "cli_memory",
        "insert": [
            "cli_inserting_data", "cli_insert_csv_tsv", "cli_insert_unstructured", "cli_insert_convert"
        ],
        "upsert": "cli_upsert",
        "tables": "cli_tables",
        "views": "cli_views",
        "optimize": "cli_optimize",
        "rows": "cli_rows",
        "triggers": "cli_triggers",
        "indexes": "cli_indexes",
        "enable-fts": "cli_fts",
        "analyze": "cli_analyze",
        "vacuum": "cli_vacuum",
        "dump": "cli_dump",
        "add-column": "cli_add_column",
        "rename-table": "cli_renaming_tables",
        "duplicate": "cli_duplicate_table",
        "add-foreign-key": "cli_add_foreign_key",
        "add-foreign-keys": "cli_add_foreign_keys",
        "index-foreign-keys": "cli_index_foreign_keys",
        "create-index": "cli_create_index",
        "enable-wal": "cli_wal",
        "enable-counts": "cli_enable_counts",
        "bulk": "cli_bulk",
        "create-database": "cli_create_database",
        "create-table": "cli_create_table",
        "drop-table": "cli_drop_table",
        "create-view": "cli_create_view",
        "drop-view": "cli_drop_view",
        "search": "cli_search",
        "transform": "cli_transform_table",
        "extract": "cli_extract",
        "schema": "cli_schema",
        "insert-files": "cli_insert_files",
        "analyze-tables": "cli_analyze_tables",
        "convert": "cli_convert",
        "add-geometry-column": "cli_spatialite",
        "create-spatial-index": "cli_spatialite_indexes",
        "install": "cli_install",
        "uninstall": "cli_uninstall",
        "tui": "cli_tui",
    }
    commands.sort(key = lambda command: go_first.index(command) if command in go_first else 999)
    cog.out("\n")
    for command in commands:
        cog.out(".. _cli_ref_" + command.replace("-", "_") + ":\n\n")
        cog.out(command + "\n")
        cog.out(("=" * len(command)) + "\n\n")
        if command in refs:
            command_refs = refs[command]
            if isinstance(command_refs, str):
                command_refs = [command_refs]
            cog.out(
                "See {}.\n\n".format(
                    ", ".join(":ref:`{}`".format(c) for c in command_refs)
                )
            )
        cog.out("::\n\n")
        result = CliRunner().invoke(cli.cli, [command, "--help"])
        output = result.output.replace("Usage: cli ", "Usage: duckdb-utils ")
        cog.out(textwrap.indent(output, '    '))
        cog.out("\n\n")
.. ]]]

.. _cli_ref_query:

query
=====

See :ref:`cli_query`.

::

    Usage: duckdb-utils query [OPTIONS] PATH SQL

      Execute SQL query and return the results as JSON

      Example:

          duckdb-utils data.duckdb \
              "select * from seagulls where age > :age" \
              -p age 1

    Options:
      --attach <TEXT FILE>...     Additional databases to attach - specify alias and
                                  filepath
      --nl                        Output newline-delimited JSON
      --arrays                    Output rows as arrays instead of objects
      --csv                       Output CSV
      --tsv                       Output TSV
      --no-headers                Omit CSV headers
      -t, --table                 Output as a formatted table
      --fmt TEXT                  Table format - one of asciidoc, double_grid,
                                  double_outline, fancy_grid, fancy_outline, github,
                                  grid, heavy_grid, heavy_outline, html, jira,
                                  latex, latex_booktabs, latex_longtable, latex_raw,
                                  mediawiki, mixed_grid, mixed_outline, moinmoin,
                                  orgtbl, outline, pipe, plain, presto, pretty,
                                  psql, rounded_grid, rounded_outline, rst, simple,
                                  simple_grid, simple_outline, textile, tsv,
                                  unsafehtml, youtrack
      --json-cols                 Detect JSON cols and output them as JSON, not
                                  escaped strings
      -r, --raw                   Raw output, first column of first row
      --raw-lines                 Raw output, first column of each row
      -p, --param <TEXT TEXT>...  Named :parameters for SQL query
      --functions TEXT            Python code defining one or more custom SQL
                                  functions
      --load-extension TEXT       Path to DuckDB extension, with optional
                                  :entrypoint
      -h, --help                  Show this message and exit.


.. _cli_ref_memory:

memory
======

See :ref:`cli_memory`.

::

    Usage: duckdb-utils memory [OPTIONS] [PATHS]... SQL

      Execute SQL query against an in-memory database, optionally populated by
      imported data

      To import data from CSV, TSV or JSON files pass them on the command-line:

          duckdb-utils memory one.csv two.json \
              "select * from one join two on one.two_id = two.id"

      For data piped into the tool from standard input, use "-" or "stdin":

          cat animals.csv | duckdb-utils memory - \
              "select * from stdin where species = 'dog'"

      The format of the data will be automatically detected. You can specify the
      format explicitly using :json, :csv, :tsv or :nl (for newline-delimited JSON)
      - for example:

          cat animals.csv | duckdb-utils memory stdin:csv places.dat:nl \
              "select * from stdin where place_id in (select id from places)"

      Use --schema to view the SQL schema of any imported files:

          duckdb-utils memory animals.csv --schema

    Options:
      --functions TEXT            Python code defining one or more custom SQL
                                  functions
      --attach <TEXT FILE>...     Additional databases to attach - specify alias and
                                  filepath
      --flatten                   Flatten nested JSON objects, so {"foo": {"bar":
                                  1}} becomes {"foo_bar": 1}
      --nl                        Output newline-delimited JSON
      --arrays                    Output rows as arrays instead of objects
      --csv                       Output CSV
      --tsv                       Output TSV
      --no-headers                Omit CSV headers
      -t, --table                 Output as a formatted table
      --fmt TEXT                  Table format - one of asciidoc, double_grid,
                                  double_outline, fancy_grid, fancy_outline, github,
                                  grid, heavy_grid, heavy_outline, html, jira,
                                  latex, latex_booktabs, latex_longtable, latex_raw,
                                  mediawiki, mixed_grid, mixed_outline, moinmoin,
                                  orgtbl, outline, pipe, plain, presto, pretty,
                                  psql, rounded_grid, rounded_outline, rst, simple,
                                  simple_grid, simple_outline, textile, tsv,
                                  unsafehtml, youtrack
      --json-cols                 Detect JSON cols and output them as JSON, not
                                  escaped strings
      -r, --raw                   Raw output, first column of first row
      --raw-lines                 Raw output, first column of each row
      -p, --param <TEXT TEXT>...  Named :parameters for SQL query
      --encoding TEXT             Character encoding for CSV input, defaults to
                                  utf-8
      -n, --no-detect-types       Treat all CSV/TSV columns as TEXT
      --schema                    Show SQL schema for in-memory database
      --dump                      Dump SQL for in-memory database
      --save FILE                 Save in-memory database to this file
      --analyze                   Analyze resulting tables and output results
      --load-extension TEXT       Path to DuckDB extension, with optional
                                  :entrypoint
      -h, --help                  Show this message and exit.


.. _cli_ref_insert:

insert
======

See :ref:`cli_inserting_data`, :ref:`cli_insert_csv_tsv`, :ref:`cli_insert_unstructured`, :ref:`cli_insert_convert`.

::

    Usage: duckdb-utils insert [OPTIONS] PATH TABLE FILE

      Insert records from FILE into a table, creating the table if it does not
      already exist.

      Example:

          echo '{"name": "Lila"}' | duckdb-utils insert data.duckdb seagulls -

      By default the input is expected to be a JSON object or array of objects.

      - Use --nl for newline-delimited JSON objects
      - Use --csv or --tsv for comma-separated or tab-separated input
      - Use --lines to write each incoming line to a column called "line"
      - Use --text to write the entire input to a column called "text"

      You can also use --convert to pass a fragment of Python code that will be used
      to convert each input.

      Your Python code will be passed a "row" variable representing the imported
      row, and can return a modified row.

      This example uses just the name, latitude and longitude columns from a CSV
      file, converting name to upper case and latitude and longitude to floating
      point numbers:

          duckdb-utils insert plants.duckdb plants plants.csv --csv --convert '
            return {
              "name": row["name"].upper(),
              "latitude": float(row["latitude"]),
              "longitude": float(row["longitude"]),
            }'

      If you are using --lines your code will be passed a "line" variable, and for
      --text a "text" variable.

      When using --text your function can return an iterator of rows to insert. This
      example inserts one record per word in the input:

          echo 'A bunch of words' | duckdb-utils insert words.duckdb words - \
            --text --convert '({"word": w} for w in text.split())'

    Options:
      --pk TEXT                 Columns to use as the primary key, e.g. id
      --flatten                 Flatten nested JSON objects, so {"a": {"b": 1}}
                                becomes {"a_b": 1}
      --nl                      Expect newline-delimited JSON
      -c, --csv                 Expect CSV input
      --tsv                     Expect TSV input
      --empty-null              Treat empty strings as NULL
      --lines                   Treat each line as a single value called 'line'
      --text                    Treat input as a single value called 'text'
      --convert TEXT            Python code to convert each item
      --import TEXT             Python modules to import
      --delimiter TEXT          Delimiter to use for CSV files
      --quotechar TEXT          Quote character to use for CSV/TSV
      --sniff                   Detect delimiter and quote character
      --no-headers              CSV file has no header row
      --encoding TEXT           Character encoding for input, defaults to utf-8
      --batch-size INTEGER      Commit every X records
      --stop-after INTEGER      Stop after X records
      --alter                   Alter existing table to add any missing columns
      --not-null TEXT           Columns that should be created as NOT NULL
      --default <TEXT TEXT>...  Default value that should be set for a column
      -d, --detect-types        Detect types for columns in CSV/TSV data
      --analyze                 Run ANALYZE at the end of this operation
      --load-extension TEXT     Path to DuckDB extension, with optional :entrypoint
      --silent                  Do not show progress bar
      --strict                  Apply STRICT mode to created table
      --ignore                  Ignore records if pk already exists
      --replace                 Replace records if pk already exists
      --truncate                Truncate table before inserting records, if table
                                already exists
      -h, --help                Show this message and exit.


.. _cli_ref_upsert:

upsert
======

See :ref:`cli_upsert`.

::

    Usage: duckdb-utils upsert [OPTIONS] PATH TABLE FILE

      Upsert records based on their primary key. Works like 'insert' but if an
      incoming record has a primary key that matches an existing record the existing
      record will be updated.

      Example:

          echo '[
              {"id": 1, "name": "Lila"},
              {"id": 2, "name": "Suna"}
          ]' | duckdb-utils upsert data.duckdb seagulls - --pk id

    Options:
      --pk TEXT                 Columns to use as the primary key, e.g. id
                                [required]
      --flatten                 Flatten nested JSON objects, so {"a": {"b": 1}}
                                becomes {"a_b": 1}
      --nl                      Expect newline-delimited JSON
      -c, --csv                 Expect CSV input
      --tsv                     Expect TSV input
      --empty-null              Treat empty strings as NULL
      --lines                   Treat each line as a single value called 'line'
      --text                    Treat input as a single value called 'text'
      --convert TEXT            Python code to convert each item
      --import TEXT             Python modules to import
      --delimiter TEXT          Delimiter to use for CSV files
      --quotechar TEXT          Quote character to use for CSV/TSV
      --sniff                   Detect delimiter and quote character
      --no-headers              CSV file has no header row
      --encoding TEXT           Character encoding for input, defaults to utf-8
      --batch-size INTEGER      Commit every X records
      --stop-after INTEGER      Stop after X records
      --alter                   Alter existing table to add any missing columns
      --not-null TEXT           Columns that should be created as NOT NULL
      --default <TEXT TEXT>...  Default value that should be set for a column
      -d, --detect-types        Detect types for columns in CSV/TSV data
      --analyze                 Run ANALYZE at the end of this operation
      --load-extension TEXT     Path to DuckDB extension, with optional :entrypoint
      --silent                  Do not show progress bar
      --strict                  Apply STRICT mode to created table
      -h, --help                Show this message and exit.


.. _cli_ref_bulk:

bulk
====

See :ref:`cli_bulk`.

::

    Usage: duckdb-utils bulk [OPTIONS] PATH SQL FILE

      Execute parameterized SQL against the provided list of documents.

      Example:

          echo '[
              {"id": 1, "name": "Lila2"},
              {"id": 2, "name": "Suna2"}
          ]' | duckdb-utils bulk data.duckdb '
              update seagulls set name = :name where id = :id
          ' -

    Options:
      --batch-size INTEGER   Commit every X records
      --functions TEXT       Python code defining one or more custom SQL functions
      --flatten              Flatten nested JSON objects, so {"a": {"b": 1}} becomes
                             {"a_b": 1}
      --nl                   Expect newline-delimited JSON
      -c, --csv              Expect CSV input
      --tsv                  Expect TSV input
      --empty-null           Treat empty strings as NULL
      --lines                Treat each line as a single value called 'line'
      --text                 Treat input as a single value called 'text'
      --convert TEXT         Python code to convert each item
      --import TEXT          Python modules to import
      --delimiter TEXT       Delimiter to use for CSV files
      --quotechar TEXT       Quote character to use for CSV/TSV
      --sniff                Detect delimiter and quote character
      --no-headers           CSV file has no header row
      --encoding TEXT        Character encoding for input, defaults to utf-8
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_search:

search
======

See :ref:`cli_search`.

::

    Usage: duckdb-utils search [OPTIONS] PATH DBTABLE Q

      Execute a full-text search against this table

      Example:

          duckdb-utils search data.duckdb seagulls lila

    Options:
      -o, --order TEXT       Order by ('column' or 'column desc')
      -c, --column TEXT      Columns to return
      --limit INTEGER        Number of rows to return - defaults to everything
      --sql                  Show SQL query that would be run
      --quote                Apply FTS quoting rules to search term
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit CSV headers
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, double_grid,
                             double_outline, fancy_grid, fancy_outline, github,
                             grid, heavy_grid, heavy_outline, html, jira, latex,
                             latex_booktabs, latex_longtable, latex_raw, mediawiki,
                             mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                             pipe, plain, presto, pretty, psql, rounded_grid,
                             rounded_outline, rst, simple, simple_grid,
                             simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_transform:

transform
=========

See :ref:`cli_transform_table`.

::

    Usage: duckdb-utils transform [OPTIONS] PATH TABLE

      Transform a table beyond the capabilities of ALTER TABLE

      Example:

          duckdb-utils transform mydb.duckdb mytable \
              --drop column1 \
              --rename column2 column_renamed

    Options:
      --type <TEXT CHOICE>...         Change column type to INTEGER, TEXT, FLOAT or
                                      BLOB
      --drop TEXT                     Drop this column
      --rename <TEXT TEXT>...         Rename this column to X
      -o, --column-order TEXT         Reorder columns
      --not-null TEXT                 Set this column to NOT NULL
      --not-null-false TEXT           Remove NOT NULL from this column
      --pk TEXT                       Make this column the primary key
      --pk-none                       Remove primary key (convert to rowid table)
      --default <TEXT TEXT>...        Set default value for this column
      --default-none TEXT             Remove default from this column
      --add-foreign-key <TEXT TEXT TEXT>...
                                      Add a foreign key constraint from a column to
                                      another table with another column
      --drop-foreign-key TEXT         Drop foreign key constraint for this column
      --sql                           Output SQL without executing it
      --load-extension TEXT           Path to DuckDB extension, with optional
                                      :entrypoint
      -h, --help                      Show this message and exit.


.. _cli_ref_extract:

extract
=======

See :ref:`cli_extract`.

::

    Usage: duckdb-utils extract [OPTIONS] PATH TABLE COLUMNS...

      Extract one or more columns into a separate table

      Example:

          duckdb-utils extract trees.duckdb Street_Trees species

    Options:
      --table TEXT             Name of the other table to extract columns to
      --fk-column TEXT         Name of the foreign key column to add to the table
      --rename <TEXT TEXT>...  Rename this column in extracted table
      --load-extension TEXT    Path to DuckDB extension, with optional :entrypoint
      -h, --help               Show this message and exit.


.. _cli_ref_schema:

schema
======

See :ref:`cli_schema`.

::

    Usage: duckdb-utils schema [OPTIONS] PATH [TABLES]...

      Show full schema for this database or for specified tables

      Example:

          duckdb-utils schema trees.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_insert_files:

insert-files
============

See :ref:`cli_insert_files`.

::

    Usage: duckdb-utils insert-files [OPTIONS] PATH TABLE FILE_OR_DIR...

      Insert one or more files using BLOB columns in the specified table

      Example:

          duckdb-utils insert-files pics.duckdb images *.gif \
              -c name:name \
              -c content:content \
              -c content_hash:sha256 \
              -c created:ctime_iso \
              -c modified:mtime_iso \
              -c size:size \
              --pk name

    Options:
      -c, --column TEXT      Column definitions for the table
      --pk TEXT              Column to use as primary key
      --alter                Alter table to add missing columns
      --replace              Replace files with matching primary key
      --upsert               Upsert files with matching primary key
      --name TEXT            File name to use
      --text                 Store file content as TEXT, not BLOB
      --encoding TEXT        Character encoding for input, defaults to utf-8
      -s, --silent           Don't show a progress bar
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_analyze_tables:

analyze-tables
==============

See :ref:`cli_analyze_tables`.

::

    Usage: duckdb-utils analyze-tables [OPTIONS] PATH [TABLES]...

      Analyze the columns in one or more tables

      Example:

          duckdb-utils analyze-tables data.duckdb trees

    Options:
      -c, --column TEXT       Specific columns to analyze
      --save                  Save results to _analyze_tables table
      --common-limit INTEGER  How many common values
      --no-most               Skip most common values
      --no-least              Skip least common values
      --load-extension TEXT   Path to DuckDB extension, with optional :entrypoint
      -h, --help              Show this message and exit.


.. _cli_ref_convert:

convert
=======

See :ref:`cli_convert`.

::

    Usage: duckdb-utils convert [OPTIONS] DB_PATH TABLE COLUMNS... CODE

      Convert columns using Python code you supply. For example:

          duckdb-utils convert my.duckdb mytable mycolumn \
              '"\n".join(textwrap.wrap(value, 10))' \
              --import=textwrap

      "value" is a variable with the column value to be converted.

      Use "-" for CODE to read Python code from standard input.

      The following common operations are available as recipe functions:

      r.jsonsplit(value, delimiter=',', type=<class 'str'>)

          Convert a string like a,b,c into a JSON array ["a", "b", "c"]

      r.parsedate(value, dayfirst=False, yearfirst=False, errors=None)

          Parse a date and convert it to ISO date format: yyyy-mm-dd
          
          - dayfirst=True: treat xx as the day in xx/yy/zz
          - yearfirst=True: treat xx as the year in xx/yy/zz
          - errors=r.IGNORE to ignore values that cannot be parsed
          - errors=r.SET_NULL to set values that cannot be parsed to null

      r.parsedatetime(value, dayfirst=False, yearfirst=False, errors=None)

          Parse a datetime and convert it to ISO datetime format: yyyy-mm-ddTHH:MM:SS
          
          - dayfirst=True: treat xx as the day in xx/yy/zz
          - yearfirst=True: treat xx as the year in xx/yy/zz
          - errors=r.IGNORE to ignore values that cannot be parsed
          - errors=r.SET_NULL to set values that cannot be parsed to null

      You can use these recipes like so:

          duckdb-utils convert my.duckdb mytable mycolumn \
              'r.jsonsplit(value, delimiter=":")'

    Options:
      --import TEXT                   Python modules to import
      --dry-run                       Show results of running this against first 10
                                      rows
      --multi                         Populate columns for keys in returned
                                      dictionary
      --where TEXT                    Optional where clause
      -p, --param <TEXT TEXT>...      Named :parameters for where clause
      --output TEXT                   Optional separate column to populate with the
                                      output
      --output-type [integer|float|blob|text]
                                      Column type to use for the output column
      --drop                          Drop original column afterwards
      --no-skip-false                 Don't skip falsey values
      -s, --silent                    Don't show a progress bar
      --pdb                           Open pdb debugger on first error
      -h, --help                      Show this message and exit.


.. _cli_ref_tables:

tables
======

See :ref:`cli_tables`.

::

    Usage: duckdb-utils tables [OPTIONS] PATH

      List the tables in the database

      Example:

          duckdb-utils tables trees.duckdb

    Options:
      --fts4                 Just show FTS4 enabled tables
      --fts5                 Just show FTS5 enabled tables
      --counts               Include row counts per table
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit CSV headers
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, double_grid,
                             double_outline, fancy_grid, fancy_outline, github,
                             grid, heavy_grid, heavy_outline, html, jira, latex,
                             latex_booktabs, latex_longtable, latex_raw, mediawiki,
                             mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                             pipe, plain, presto, pretty, psql, rounded_grid,
                             rounded_outline, rst, simple, simple_grid,
                             simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --columns              Include list of columns for each table
      --schema               Include schema for each table
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_views:

views
=====

See :ref:`cli_views`.

::

    Usage: duckdb-utils views [OPTIONS] PATH

      List the views in the database

      Example:

          duckdb-utils views trees.duckdb

    Options:
      --counts               Include row counts per view
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit CSV headers
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, double_grid,
                             double_outline, fancy_grid, fancy_outline, github,
                             grid, heavy_grid, heavy_outline, html, jira, latex,
                             latex_booktabs, latex_longtable, latex_raw, mediawiki,
                             mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                             pipe, plain, presto, pretty, psql, rounded_grid,
                             rounded_outline, rst, simple, simple_grid,
                             simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --columns              Include list of columns for each view
      --schema               Include schema for each view
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_rows:

rows
====

See :ref:`cli_rows`.

::

    Usage: duckdb-utils rows [OPTIONS] PATH DBTABLE

      Output all rows in the specified table

      Example:

          duckdb-utils rows trees.duckdb Trees

    Options:
      -c, --column TEXT           Columns to return
      --where TEXT                Optional where clause
      -o, --order TEXT            Order by ('column' or 'column desc')
      -p, --param <TEXT TEXT>...  Named :parameters for where clause
      --limit INTEGER             Number of rows to return - defaults to everything
      --offset INTEGER            SQL offset to use
      --nl                        Output newline-delimited JSON
      --arrays                    Output rows as arrays instead of objects
      --csv                       Output CSV
      --tsv                       Output TSV
      --no-headers                Omit CSV headers
      -t, --table                 Output as a formatted table
      --fmt TEXT                  Table format - one of asciidoc, double_grid,
                                  double_outline, fancy_grid, fancy_outline, github,
                                  grid, heavy_grid, heavy_outline, html, jira,
                                  latex, latex_booktabs, latex_longtable, latex_raw,
                                  mediawiki, mixed_grid, mixed_outline, moinmoin,
                                  orgtbl, outline, pipe, plain, presto, pretty,
                                  psql, rounded_grid, rounded_outline, rst, simple,
                                  simple_grid, simple_outline, textile, tsv,
                                  unsafehtml, youtrack
      --json-cols                 Detect JSON cols and output them as JSON, not
                                  escaped strings
      --load-extension TEXT       Path to DuckDB extension, with optional
                                  :entrypoint
      -h, --help                  Show this message and exit.


.. _cli_ref_triggers:

triggers
========

See :ref:`cli_triggers`.

::

    Usage: duckdb-utils triggers [OPTIONS] PATH [TABLES]...

      Show triggers configured in this database

      Example:

          duckdb-utils triggers trees.duckdb

    Options:
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit CSV headers
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, double_grid,
                             double_outline, fancy_grid, fancy_outline, github,
                             grid, heavy_grid, heavy_outline, html, jira, latex,
                             latex_booktabs, latex_longtable, latex_raw, mediawiki,
                             mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                             pipe, plain, presto, pretty, psql, rounded_grid,
                             rounded_outline, rst, simple, simple_grid,
                             simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_indexes:

indexes
=======

See :ref:`cli_indexes`.

::

    Usage: duckdb-utils indexes [OPTIONS] PATH [TABLES]...

      Show indexes for the whole database or specific tables

      Example:

          duckdb-utils indexes trees.duckdb Trees

    Options:
      --aux                  Include auxiliary columns
      --nl                   Output newline-delimited JSON
      --arrays               Output rows as arrays instead of objects
      --csv                  Output CSV
      --tsv                  Output TSV
      --no-headers           Omit CSV headers
      -t, --table            Output as a formatted table
      --fmt TEXT             Table format - one of asciidoc, double_grid,
                             double_outline, fancy_grid, fancy_outline, github,
                             grid, heavy_grid, heavy_outline, html, jira, latex,
                             latex_booktabs, latex_longtable, latex_raw, mediawiki,
                             mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                             pipe, plain, presto, pretty, psql, rounded_grid,
                             rounded_outline, rst, simple, simple_grid,
                             simple_outline, textile, tsv, unsafehtml, youtrack
      --json-cols            Detect JSON cols and output them as JSON, not escaped
                             strings
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_create_database:

create-database
===============

See :ref:`cli_create_database`.

::

    Usage: duckdb-utils create-database [OPTIONS] PATH

      Create a new empty database file

      Example:

          duckdb-utils create-database trees.duckdb

    Options:
      --enable-wal           Enable WAL mode on the created database
      --init-spatialite      Enable SpatiaLite on the created database
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_create_table:

create-table
============

See :ref:`cli_create_table`.

::

    Usage: duckdb-utils create-table [OPTIONS] PATH TABLE COLUMNS...

      Add a table with the specified columns. Columns should be specified using
      name, type pairs, for example:

          duckdb-utils create-table my.duckdb people \
              id integer \
              name text \
              height float \
              photo blob --pk id

      Valid column types are text, integer, float and blob.

    Options:
      --pk TEXT                 Column to use as primary key
      --not-null TEXT           Columns that should be created as NOT NULL
      --default <TEXT TEXT>...  Default value that should be set for a column
      --fk <TEXT TEXT TEXT>...  Column, other table, other column to set as a
                                foreign key
      --ignore                  If table already exists, do nothing
      --replace                 If table already exists, replace it
      --transform               If table already exists, try to transform the schema
      --load-extension TEXT     Path to DuckDB extension, with optional :entrypoint
      --strict                  Apply STRICT mode to created table
      -h, --help                Show this message and exit.


.. _cli_ref_create_index:

create-index
============

See :ref:`cli_create_index`.

::

    Usage: duckdb-utils create-index [OPTIONS] PATH TABLE COLUMN...

      Add an index to the specified table for the specified columns

      Example:

          duckdb-utils create-index seagulls.duckdb seagulls name

      To create an index in descending order:

          duckdb-utils create-index seagulls.duckdb seagulls -- -name

    Options:
      --name TEXT                Explicit name for the new index
      --unique                   Make this a unique index
      --if-not-exists, --ignore  Ignore if index already exists
      --analyze                  Run ANALYZE after creating the index
      --load-extension TEXT      Path to DuckDB extension, with optional :entrypoint
      -h, --help                 Show this message and exit.


.. _cli_ref_enable_fts:

enable-fts
==========

See :ref:`cli_fts`.

::

    Usage: duckdb-utils enable-fts [OPTIONS] PATH TABLE COLUMN...

      Enable full-text search for specific table and columns"

      Example:

          duckdb-utils enable-fts seagulls.duckdb seagulls name

    Options:
      --fts4                 Use FTS4
      --fts5                 Use FTS5
      --tokenize TEXT        Tokenizer to use, e.g. porter
      --create-triggers      Create triggers to update the FTS tables when the
                             parent table changes.
      --replace              Replace existing FTS configuration if it exists
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_populate_fts:

populate-fts
============

::

    Usage: duckdb-utils populate-fts [OPTIONS] PATH TABLE COLUMN...

      Re-populate full-text search for specific table and columns

      Example:

          duckdb-utils populate-fts seagulls.duckdb seagulls name

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_rebuild_fts:

rebuild-fts
===========

::

    Usage: duckdb-utils rebuild-fts [OPTIONS] PATH [TABLES]...

      Rebuild all or specific full-text search tables

      Example:

          duckdb-utils rebuild-fts seagulls.duckdb seagulls

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_disable_fts:

disable-fts
===========

::

    Usage: duckdb-utils disable-fts [OPTIONS] PATH TABLE

      Disable full-text search for specific table

      Example:

          duckdb-utils disable-fts seagulls.duckdb seagulls

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_tui:

tui
===

See :ref:`cli_tui`.

::

    Usage: duckdb-utils tui [OPTIONS]

      Open Textual TUI.

    Options:
      -h, --help  Show this message and exit.


.. _cli_ref_optimize:

optimize
========

See :ref:`cli_optimize`.

::

    Usage: duckdb-utils optimize [OPTIONS] PATH [TABLES]...

      Optimize all full-text search tables and then run VACUUM - should shrink the
      database file

      Example:

          duckdb-utils optimize seagulls.duckdb

    Options:
      --no-vacuum            Don't run VACUUM
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_analyze:

analyze
=======

See :ref:`cli_analyze`.

::

    Usage: duckdb-utils analyze [OPTIONS] PATH [NAMES]...

      Run ANALYZE against the whole database, or against specific named indexes and
      tables

      Example:

          duckdb-utils analyze seagulls.duckdb

    Options:
      -h, --help  Show this message and exit.


.. _cli_ref_vacuum:

vacuum
======

See :ref:`cli_vacuum`.

::

    Usage: duckdb-utils vacuum [OPTIONS] PATH

      Run VACUUM against the database

      Example:

          duckdb-utils vacuum seagulls.duckdb

    Options:
      -h, --help  Show this message and exit.


.. _cli_ref_dump:

dump
====

See :ref:`cli_dump`.

::

    Usage: duckdb-utils dump [OPTIONS] PATH

      Output a SQL dump of the schema and full contents of the database

      Example:

          duckdb-utils dump seagulls.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_add_column:

add-column
==========

See :ref:`cli_add_column`.

::

    Usage: duckdb-utils add-column [OPTIONS] PATH TABLE COL_NAME
                          [[integer|int|float|text|str|blob|bytes]]

      Add a column to the specified table

      Example:

          duckdb-utils add-column seagulls.duckdb seagulls weight float

    Options:
      --fk TEXT                Table to reference as a foreign key
      --fk-col TEXT            Referenced column on that foreign key table - if
                               omitted will automatically use the primary key
      --not-null-default TEXT  Add NOT NULL DEFAULT 'TEXT' constraint
      --ignore                 If column already exists, do nothing
      --load-extension TEXT    Path to DuckDB extension, with optional :entrypoint
      -h, --help               Show this message and exit.


.. _cli_ref_add_foreign_key:

add-foreign-key
===============

See :ref:`cli_add_foreign_key`.

::

    Usage: duckdb-utils add-foreign-key [OPTIONS] PATH TABLE COLUMN [OTHER_TABLE]
                               [OTHER_COLUMN]

      Add a new foreign key constraint to an existing table

      Example:

          duckdb-utils add-foreign-key my.duckdb books author_id authors id

    Options:
      --ignore               If foreign key already exists, do nothing
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_add_foreign_keys:

add-foreign-keys
================

See :ref:`cli_add_foreign_keys`.

::

    Usage: duckdb-utils add-foreign-keys [OPTIONS] PATH [FOREIGN_KEY]...

      Add multiple new foreign key constraints to a database

      Example:

          duckdb-utils add-foreign-keys my.duckdb \
              books author_id authors id \
              authors country_id countries id

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_index_foreign_keys:

index-foreign-keys
==================

See :ref:`cli_index_foreign_keys`.

::

    Usage: duckdb-utils index-foreign-keys [OPTIONS] PATH

      Ensure every foreign key column has an index on it

      Example:

          duckdb-utils index-foreign-keys seagulls.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_enable_wal:

enable-wal
==========

See :ref:`cli_wal`.

::

    Usage: duckdb-utils enable-wal [OPTIONS] PATH...

      Enable WAL for database files

      Example:

          duckdb-utils enable-wal seagulls.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_disable_wal:

disable-wal
===========

::

    Usage: duckdb-utils disable-wal [OPTIONS] PATH...

      Disable WAL for database files

      Example:

          duckdb-utils disable-wal seagulls.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_enable_counts:

enable-counts
=============

See :ref:`cli_enable_counts`.

::

    Usage: duckdb-utils enable-counts [OPTIONS] PATH [TABLES]...

      Configure triggers to update a _counts table with row counts

      Example:

          duckdb-utils enable-counts seagulls.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_reset_counts:

reset-counts
============

::

    Usage: duckdb-utils reset-counts [OPTIONS] PATH

      Reset calculated counts in the _counts table

      Example:

          duckdb-utils reset-counts seagulls.duckdb

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_duplicate:

duplicate
=========

See :ref:`cli_duplicate_table`.

::

    Usage: duckdb-utils duplicate [OPTIONS] PATH TABLE NEW_TABLE

      Create a duplicate of this table, copying across the schema and all row data.

    Options:
      --ignore               If table does not exist, do nothing
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_rename_table:

rename-table
============

See :ref:`cli_renaming_tables`.

::

    Usage: duckdb-utils rename-table [OPTIONS] PATH TABLE NEW_NAME

      Rename this table.

    Options:
      --ignore               If table does not exist, do nothing
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_drop_table:

drop-table
==========

See :ref:`cli_drop_table`.

::

    Usage: duckdb-utils drop-table [OPTIONS] PATH TABLE

      Drop the specified table

      Example:

          duckdb-utils drop-table seagulls.duckdb seagulls

    Options:
      --ignore               If table does not exist, do nothing
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_create_view:

create-view
===========

See :ref:`cli_create_view`.

::

    Usage: duckdb-utils create-view [OPTIONS] PATH VIEW SELECT

      Create a view for the provided SELECT query

      Example:

          duckdb-utils create-view seagulls.duckdb heavy_seagulls \
            'select * from seagulls where weight > 3'

    Options:
      --ignore               If view already exists, do nothing
      --replace              If view already exists, replace it
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_drop_view:

drop-view
=========

See :ref:`cli_drop_view`.

::

    Usage: duckdb-utils drop-view [OPTIONS] PATH VIEW

      Drop the specified view

      Example:

          duckdb-utils drop-view seagulls.duckdb heavy_seagulls

    Options:
      --ignore               If view does not exist, do nothing
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_install:

install
=======

See :ref:`cli_install`.

::

    Usage: duckdb-utils install [OPTIONS] [PACKAGES]...

      Install packages from PyPI into the same environment as duckdb-utils

    Options:
      -U, --upgrade        Upgrade packages to latest version
      -e, --editable TEXT  Install a project in editable mode from this path
      -h, --help           Show this message and exit.


.. _cli_ref_uninstall:

uninstall
=========

See :ref:`cli_uninstall`.

::

    Usage: duckdb-utils uninstall [OPTIONS] PACKAGES...

      Uninstall Python packages from the duckdb-utils environment

    Options:
      -y, --yes   Don't ask for confirmation
      -h, --help  Show this message and exit.


.. _cli_ref_add_geometry_column:

add-geometry-column
===================

See :ref:`cli_spatialite`.

::

    Usage: duckdb-utils add-geometry-column [OPTIONS] DB_PATH TABLE COLUMN_NAME

      Add a SpatiaLite geometry column to an existing table. Requires SpatiaLite
      extension.

      By default, this command will try to load the SpatiaLite extension from usual
      paths. To load it from a specific path, use --load-extension.

    Options:
      -t, --type [POINT|LINESTRING|POLYGON|MULTIPOINT|MULTILINESTRING|MULTIPOLYGON|GEOMETRYCOLLECTION|GEOMETRY]
                                      Specify a geometry type for this column.
                                      [default: GEOMETRY]
      --srid INTEGER                  Spatial Reference ID. See
                                      https://spatialreference.org for details on
                                      specific projections.  [default: 4326]
      --dimensions TEXT               Coordinate dimensions. Use XYZ for three-
                                      dimensional geometries.
      --not-null                      Add a NOT NULL constraint.
      --load-extension TEXT           Path to DuckDB extension, with optional
                                      :entrypoint
      -h, --help                      Show this message and exit.


.. _cli_ref_create_spatial_index:

create-spatial-index
====================

See :ref:`cli_spatialite_indexes`.

::

    Usage: duckdb-utils create-spatial-index [OPTIONS] DB_PATH TABLE COLUMN_NAME

      Create a spatial index on a SpatiaLite geometry column. The table and geometry
      column must already exist before trying to add a spatial index.

      By default, this command will try to load the SpatiaLite extension from usual
      paths. To load it from a specific path, use --load-extension.

    Options:
      --load-extension TEXT  Path to DuckDB extension, with optional :entrypoint
      -h, --help             Show this message and exit.


.. _cli_ref_plugins:

plugins
=======

::

    Usage: duckdb-utils plugins [OPTIONS]

      List installed plugins

    Options:
      -h, --help  Show this message and exit.


.. [[[end]]]
