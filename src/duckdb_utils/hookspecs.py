from pluggy import HookimplMarker
from pluggy import HookspecMarker

hookspec = HookspecMarker("duckdb_utils")
hookimpl = HookimplMarker("duckdb_utils")


@hookspec
def register_commands(cli):
    """Register additional CLI commands, e.g. 'duckdb-utils mycommand ...'"""


@hookspec
def prepare_connection(conn):
    """Modify DuckDB connection in some way e.g. register custom SQL functions"""
