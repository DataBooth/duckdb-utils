from duckdb_utils.duckdb import PrimaryKeyRequired
import pytest


def test_upsert(fresh_db):
    table = fresh_db["table"]
    table.insert({"id": 1, "name": "Emme"}, pk="id")
    table.upsert({"id": 1, "age": 5}, pk="id", alter=True)
    assert list(table.rows) == [{"id": 1, "name": "Emme", "age": 5}]
    assert table.last_pk == 1


def test_upsert_all(fresh_db):
    table = fresh_db["table"]
    table.upsert_all([{"id": 1, "name": "Emme"}, {"id": 2, "name": "Nixie"}], pk="id")
    table.upsert_all([{"id": 1, "age": 5}, {"id": 2, "age": 5}], pk="id", alter=True)
    assert list(table.rows) == [
        {"id": 1, "name": "Emme", "age": 5},
        {"id": 2, "name": "Nixie", "age": 5},
    ]
    assert table.last_pk is None


def test_upsert_all_single_column(fresh_db):
    table = fresh_db["table"]
    table.upsert_all([{"name": "Emme"}], pk="name")
    assert list(table.rows) == [{"name": "Emme"}]
    assert table.pks == ["name"]


def test_upsert_all_not_null(fresh_db):
    # https://github.com/databooth/duckdb-utils/issues/538
    fresh_db["comments"].upsert_all(
        [{"id": 1, "name": "Emme"}],
        pk="id",
        not_null=["name"],
    )
    assert list(fresh_db["comments"].rows) == [{"id": 1, "name": "Emme"}]


def test_upsert_error_if_no_pk(fresh_db):
    table = fresh_db["table"]
    with pytest.raises(PrimaryKeyRequired):
        table.upsert_all([{"id": 1, "name": "Emme"}])
    with pytest.raises(PrimaryKeyRequired):
        table.upsert({"id": 1, "name": "Emme"})


def test_upsert_with_hash_id(fresh_db):
    table = fresh_db["table"]
    table.upsert({"foo": "bar"}, hash_id="pk")
    assert [{"pk": "a5e744d0164540d33b1d7ea616c28f2fa97e754a", "foo": "bar"}] == list(
        table.rows
    )
    assert "a5e744d0164540d33b1d7ea616c28f2fa97e754a" == table.last_pk


@pytest.mark.parametrize("hash_id", (None, "custom_id"))
def test_upsert_with_hash_id_columns(fresh_db, hash_id):
    table = fresh_db["table"]
    table.upsert({"a": 1, "b": 2, "c": 3}, hash_id=hash_id, hash_id_columns=("a", "b"))
    assert list(table.rows) == [
        {
            hash_id or "id": "4acc71e0547112eb432f0a36fb1924c4a738cb49",
            "a": 1,
            "b": 2,
            "c": 3,
        }
    ]
    assert table.last_pk == "4acc71e0547112eb432f0a36fb1924c4a738cb49"
    table.upsert({"a": 1, "b": 2, "c": 4}, hash_id=hash_id, hash_id_columns=("a", "b"))
    assert list(table.rows) == [
        {
            hash_id or "id": "4acc71e0547112eb432f0a36fb1924c4a738cb49",
            "a": 1,
            "b": 2,
            "c": 4,
        }
    ]


def test_upsert_compound_primary_key(fresh_db):
    table = fresh_db["table"]
    table.upsert_all(
        [
            {"species": "dog", "id": 1, "name": "Emme", "age": 4},
            {"species": "cat", "id": 1, "name": "Catbag"},
        ],
        pk=("species", "id"),
    )
    assert table.last_pk is None
    table.upsert({"species": "dog", "id": 1, "age": 5}, pk=("species", "id"))
    assert ("dog", 1) == table.last_pk
    assert [
        {"species": "dog", "id": 1, "name": "Emme", "age": 5},
        {"species": "cat", "id": 1, "name": "Catbag", "age": None},
    ] == list(table.rows)
    # .upsert_all() with a single item should set .last_pk
    table.upsert_all([{"species": "cat", "id": 1, "age": 5}], pk=("species", "id"))
    assert ("cat", 1) == table.last_pk
