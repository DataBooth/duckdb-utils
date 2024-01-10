import pytest
from duckdb_utils.duckdb import NotFoundError


def test_get_rowid(fresh_db):
    cats = fresh_db["cats"]
    emme = {"name": "Emme", "age": 4}
    row_id = cats.insert(emme).last_rowid
    assert emme == cats.get(row_id)


def test_get_primary_key(fresh_db):
    cats = fresh_db["cats"]
    emme = {"name": "Emme", "age": 4, "id": 5}
    last_pk = cats.insert(emme, pk="id").last_pk
    assert 5 == last_pk
    assert emme == cats.get(5)


@pytest.mark.parametrize(
    "argument,expected_msg",
    [(100, None), (None, None), ((1, 2), "Need 1 primary key value"), ("2", None)],
)
def test_get_not_found(argument, expected_msg, fresh_db):
    fresh_db["cats"].insert(
        {"id": 1, "name": "Emme", "age": 4, "is_good": True}, pk="id"
    )
    with pytest.raises(NotFoundError) as excinfo:
        fresh_db["cats"].get(argument)
    if expected_msg is not None:
        assert expected_msg == excinfo.value.args[0]
