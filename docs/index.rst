=======================
 duckdb-utils |version|
=======================

|PyPI| |Changelog| |CI| |License| |discord|

.. |PyPI| image:: https://img.shields.io/pypi/v/duckdb-utils.svg
   :target: https://pypi.org/project/duckdb-utils/
.. |Changelog| image:: https://img.shields.io/github/v/release/databooth/duckdb-utils?include_prereleases&label=changelog
   :target: https://duckdb-utils.databooth.com.au/en/stable/changelog.html
.. |CI| image:: https://github.com/databooth/duckdb-utils/workflows/Test/badge.svg
   :target: https://github.com/databooth/duckdb-utils/actions
.. |License| image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg
   :target: https://github.com/databooth/duckdb-utils/blob/main/LICENSE
.. |discord| image:: https://img.shields.io/discord/823971286308356157?label=discord
   :target: https://discord.gg/Ass7bCAMDw

*CLI tool and Python library for manipulating DuckDB databases*

This library and command-line utility helps create DuckDB databases from an existing collection of data.

Most of the functionality is available as either a Python API or through the ``duckdb-utils`` command-line tool.

duckdb-utils is not intended to be a full ORM: the focus is utility helpers to make creating the initial database and populating it with data as productive as possible.

It is designed as a useful complement to `Datasette <https://databooth.com.au/>`_.

`Cleaning data with duckdb-utils and Datasette <https://databooth.com.au/tutorials/clean-data>`_ provides a tutorial introduction (and accompanying ten minute video) about using this tool.

Contents
--------

.. toctree::
   :maxdepth: 3

   installation
   cli
   python-api
   plugins
   reference
   cli-reference
   contributing
   changelog
