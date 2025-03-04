import pytest
from duckdb_utils import Database


@pytest.fixture
def db_path_tmpdir(tmpdir):
    path = tmpdir / "test.duckdb"
    db = Database(str(path))
    return db, path, tmpdir


def test_enable_disable_wal(db_path_tmpdir):
    db, path, tmpdir = db_path_tmpdir
    assert len(tmpdir.listdir()) == 1
    assert "delete" == db.journal_mode
    assert "test.duckdb-wal" not in [f.basename for f in tmpdir.listdir()]
    db.enable_wal()
    assert "wal" == db.journal_mode
    db["test"].insert({"foo": "bar"})
    assert "test.duckdb-wal" in [f.basename for f in tmpdir.listdir()]
    db.disable_wal()
    assert "delete" == db.journal_mode
    assert "test.duckdb-wal" not in [f.basename for f in tmpdir.listdir()]
