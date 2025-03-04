import types


def test_query(fresh_db):
    fresh_db["cats"].insert_all([{"name": "Emme"}, {"name": "Pancakes"}])
    results = fresh_db.query("select * from cats order by name desc")
    assert isinstance(results, types.GeneratorType)
    assert list(results) == [{"name": "Pancakes"}, {"name": "Emme"}]


def test_execute_returning_dicts(fresh_db):
    # Like db.query() but returns a list, included for backwards compatibility
    # see https://github.com/databooth/duckdb-utils/issues/290
    fresh_db["test"].insert({"id": 1, "bar": 2}, pk="id")
    assert fresh_db.execute_returning_dicts("select * from test") == [
        {"id": 1, "bar": 2}
    ]
