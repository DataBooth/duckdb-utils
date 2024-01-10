from hypothesis import given
import hypothesis.strategies as st
import duckdb_utils


# DuckDB integers are -(2^63) to 2^63 - 1
@given(st.integers(-9223372036854775808, 9223372036854775807))
def test_roundtrip_integers(integer):
    db = duckdb_utils.Database(memory=True)
    row = {
        "integer": integer,
    }
    db["test"].insert(row)
    assert list(db["test"].rows) == [row]


@given(st.text())
def test_roundtrip_text(text):
    db = duckdb_utils.Database(memory=True)
    row = {
        "text": text,
    }
    db["test"].insert(row)
    assert list(db["test"].rows) == [row]


@given(st.binary(max_size=1024 * 1024))
def test_roundtrip_binary(binary):
    db = duckdb_utils.Database(memory=True)
    row = {
        "binary": binary,
    }
    db["test"].insert(row)
    assert list(db["test"].rows) == [row]


@given(st.floats(allow_nan=False))
def test_roundtrip_floats(floats):
    db = duckdb_utils.Database(memory=True)
    row = {
        "floats": floats,
    }
    db["test"].insert(row)
    assert list(db["test"].rows) == [row]
