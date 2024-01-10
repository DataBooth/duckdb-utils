.. _installation:

==============
 Installation
==============

``duckdb-utils`` is tested on Linux, macOS and Windows.

.. _installation_homebrew:

Using Homebrew
==============

The :ref:`duckdb-utils command-line tool <cli>` can be installed on macOS using Homebrew::

    brew install duckdb-utils

If you have it installed and want to upgrade to the most recent release, you can run::

    brew upgrade duckdb-utils

Then run ``duckdb-utils --version`` to confirm the installed version.

.. _installation_pip:

Using pip
=========

The `duckdb-utils package <https://pypi.org/project/duckdb-utils/>`__ on PyPI includes both the :ref:`duckdb_utils Python library <python_api>` and the ``duckdb-utils`` command-line tool. You can install them using ``pip`` like so::

    pip install duckdb-utils

.. _installation_pipx:

Using pipx
==========

`pipx <https://pypi.org/project/pipx/>`__ is a tool for installing Python command-line applications in their own isolated environments. You can use ``pipx`` to install the ``duckdb-utils`` command-line tool like this::

    pipx install duckdb-utils

.. _installation_duckdb_alternatives:

Alternatives to duckdb
=======================

By default, ``duckdb-utils`` uses the ``duckdb`` package bundled with the Python standard library.

Depending on your operating system, this may come with some limitations.

On some platforms the ability to load additional extensions (via ``conn.load_extension(...)`` or ``--load-extension=/path/to/extension``) may be disabled.

You may also see the error ``duckdb.OperationalError: table duckdb_master may not be modified`` when trying to alter an existing table.

You can work around these limitations by installing either the `pyduckdb <https://pypi.org/project/pyduckdb/>`__ package or the `sqlean.py <https://pypi.org/project/sqlean.py/>`__ package, both of which provide drop-in replacements for the standard library ``duckdb`` module but with a recent version of DuckDB and full support for loading extensions.

To install ``sqlean.py`` (which has compiled binary wheels available for all major platforms) run the following:

.. code-block:: bash

    duckdb-utils install sqlean.py

``pyduckdb`` and ``sqlean.py`` do not provide implementations of the ``.iterdump()`` method. To use that method (see :ref:`python_api_itedump`) or the ``duckdb-utils dump`` command you should also install the ``sqlite-dump`` package:

.. code-block:: bash

    duckdb-utils install sqlite-dump

.. _installation_completion:

Setting up shell completion
===========================

You can configure shell tab completion for the ``duckdb-utils`` command using these commands.

For ``bash``:

.. code-block:: bash

    eval "$(_duckdb_UTILS_COMPLETE=bash_source duckdb-utils)"

For ``zsh``:

.. code-block:: zsh

    eval "$(_duckdb_UTILS_COMPLETE=zsh_source duckdb-utils)"

Add this code to ``~/.zshrc`` or ``~/.bashrc`` to automatically run it when you start a new shell.

See `the Click documentation <https://click.palletsprojects.com/en/8.1.x/shell-completion/>`__ for more details.