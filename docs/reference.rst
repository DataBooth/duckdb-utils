.. _reference:

===============
 API reference
===============

.. contents:: :local:
   :class: this-will-duplicate-information-and-it-is-still-useful-here

.. _reference_db_database:

duckdb_utils.duckdb.Database
========================

.. autoclass:: duckdb_utils.duckdb.Database
    :members:
    :undoc-members:
    :special-members: __getitem__
    :exclude-members: use_counts_table, execute_returning_dicts, resolve_foreign_keys

.. _reference_db_queryable:

duckdb_utils.duckdb.Queryable
=========================

:ref:`Table <reference_db_table>` and :ref:`View <reference_db_view>` are  both subclasses of ``Queryable``, providing access to the following methods:

.. autoclass:: duckdb_utils.duckdb.Queryable
    :members:
    :undoc-members:
    :exclude-members: execute_count

.. _reference_db_table:

duckdb_utils.duckdb.Table
=====================

.. autoclass:: duckdb_utils.duckdb.Table
    :members:
    :undoc-members:
    :show-inheritance:
    :exclude-members: guess_foreign_column, value_or_default, build_insert_queries_and_params, insert_chunk, add_missing_columns

.. _reference_db_view:

duckdb_utils.duckdb.View
====================

.. autoclass:: duckdb_utils.duckdb.View
    :members:
    :undoc-members:
    :show-inheritance:

.. _reference_db_other:

Other
=====

.. _reference_db_other_column:

duckdb_utils.duckdb.Column
----------------------

.. autoclass:: duckdb_utils.duckdb.Column

.. _reference_db_other_column_details:

duckdb_utils.duckdb.ColumnDetails
-----------------------------

.. autoclass:: duckdb_utils.duckdb.ColumnDetails

duckdb_utils.utils
==================

.. _reference_utils_hash_record:

duckdb_utils.utils.hash_record
------------------------------

.. autofunction:: duckdb_utils.utils.hash_record

.. _reference_utils_rows_from_file:

duckdb_utils.utils.rows_from_file
---------------------------------

.. autofunction:: duckdb_utils.utils.rows_from_file

.. _reference_utils_typetracker:

duckdb_utils.utils.TypeTracker
------------------------------

.. autoclass:: duckdb_utils.utils.TypeTracker
   :members: wrap, types

.. _reference_utils_chunks:

duckdb_utils.utils.chunks
-------------------------

.. autofunction:: duckdb_utils.utils.chunks

.. _reference_utils_flatten:

duckdb_utils.utils.flatten
--------------------------

.. autofunction:: duckdb_utils.utils.flatten
