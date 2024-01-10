from duckdb_utils import Database
from duckdb_utils.utils import duckdb
import pytest


def test_recursive_triggers():
    db = Database(memory=True)
    assert db.execute("PRAGMA recursive_triggers").fetchone()[0]


def test_recursive_triggers_off():
    db = Database(memory=True, recursive_triggers=False)
    assert not db.execute("PRAGMA recursive_triggers").fetchone()[0]


def test_memory_name():
    db1 = Database(memory_name="shared")
    db2 = Database(memory_name="shared")
    db1["cats"].insert({"name": "Emme"})
    assert list(db2["cats"].rows) == [{"name": "Emme"}]


def test_duckdb_version():
    db = Database(memory=True)
    version = db.duckdb_version
    assert isinstance(version, tuple)
    as_string = ".".join(map(str, version))
    actual = next(db.query("select duckdb_version() as v"))["v"]
    assert actual == as_string


@pytest.mark.parametrize("memory", [True, False])
def test_database_close(tmpdir, memory):
    if memory:
        db = Database(memory=True)
    else:
        db = Database(str(tmpdir / "test.duckdb"))
    assert db.execute("select 1 + 1").fetchone()[0] == 2
    db.close()
    with pytest.raises(duckdb.ProgrammingError):
        db.execute("select 1 + 1")
