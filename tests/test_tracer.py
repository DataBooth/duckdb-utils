from duckdb_utils import Database


def test_tracer():
    collected = []
    db = Database(
        memory=True, tracer=lambda sql, params: collected.append((sql, params))
    )
    db["cats"].insert({"name": "Emmepaws"})
    db["cats"].enable_fts(["name"])
    db["cats"].search("Emmepaws")
    assert collected == [
        ("PRAGMA recursive_triggers=on;", None),
        ("select name from duckdb_master where type = 'view'", None),
        ("select name from duckdb_master where type = 'table'", None),
        ("select name from duckdb_master where type = 'view'", None),
        ("select name from duckdb_master where type = 'table'", None),
        ("select name from duckdb_master where type = 'view'", None),
        ("CREATE TABLE [cats] (\n   [name] TEXT\n);\n        ", None),
        ("select name from duckdb_master where type = 'view'", None),
        ("INSERT INTO [cats] ([name]) VALUES (?);", ["Emmepaws"]),
        ("select name from duckdb_master where type = 'view'", None),
        (
            "CREATE VIRTUAL TABLE [cats_fts] USING FTS5 (\n    [name],\n    content=[cats]\n)",
            None,
        ),
        (
            "INSERT INTO [cats_fts] (rowid, [name])\n    SELECT rowid, [name] FROM [cats];",
            None,
        ),
        ("select name from duckdb_master where type = 'view'", None),
    ]


def test_with_tracer():
    collected = []

    def tracer(sql, params):
        return collected.append((sql, params))

    db = Database(memory=True)

    db["cats"].insert({"name": "Emmepaws"})
    db["cats"].enable_fts(["name"])

    assert len(collected) == 0

    with db.tracer(tracer):
        list(db["cats"].search("Emmepaws"))

    assert len(collected) == 5
    assert collected == [
        ("select name from duckdb_master where type = 'view'", None),
        (
            (
                "SELECT name FROM duckdb_master\n"
                "    WHERE rootpage = 0\n"
                "    AND (\n"
                "        sql LIKE :like\n"
                "        OR sql LIKE :like2\n"
                "        OR (\n"
                "            tbl_name = :table\n"
                "            AND sql LIKE '%VIRTUAL TABLE%USING FTS%'\n"
                "        )\n"
                "    )",
                {
                    "like": "%VIRTUAL TABLE%USING FTS%content=[cats]%",
                    "like2": '%VIRTUAL TABLE%USING FTS%content="cats"%',
                    "table": "cats",
                },
            )
        ),
        ("select name from duckdb_master where type = 'view'", None),
        ("select sql from duckdb_master where name = ?", ("cats_fts",)),
        (
            (
                "with original as (\n"
                "    select\n"
                "        rowid,\n"
                "        *\n"
                "    from [cats]\n"
                ")\n"
                "select\n"
                "    [original].*\n"
                "from\n"
                "    [original]\n"
                "    join [cats_fts] on [original].rowid = [cats_fts].rowid\n"
                "where\n"
                "    [cats_fts] match :query\n"
                "order by\n"
                "    [cats_fts].rank"
            ),
            {"query": "Emmepaws"},
        ),
    ]

    # Outside the with block collected should not be appended to
    db["cats"].insert({"name": "Emmepaws"})
    assert len(collected) == 5
