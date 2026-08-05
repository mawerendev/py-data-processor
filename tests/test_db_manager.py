import pytest
from src.db_manager import DatabaseManager


@pytest.fixture
def in_memory_db():
    """
    Pytest fixture that creates an isolated in-memory SQLite database
    for each test case to avoid side effects on the production database.
    """
    # Using ':memory:' creates an ephemeral database in RAM
    db = DatabaseManager(db_name=":memory:")
    return db


def test_schema_initialization(in_memory_db):
    """
    Verify that the 'reports' table is correctly created upon initialization.
    """
    reports = in_memory_db.fetch_all_reports()
    # The database should start empty
    assert len(reports) == 0


def test_save_report_insertion(in_memory_db):
    """
    Ensure that a new report can be inserted and returns a valid incremental ID.
    """
    sample_text = "Testing database insertion with SQLite"
    total_chars = len(sample_text)
    total_words = 5
    longest_word = "insertion"

    # Execute insert operation
    record_id = in_memory_db.save_report(
        text=sample_text,
        total_chars=total_chars,
        total_words=total_words,
        longest_word=longest_word
    )

    # Assert that a valid auto-incrementing ID was generated
    assert record_id == 1


def test_fetch_all_reports_retrieval(in_memory_db):
    """
    Verify that inserted records are properly retrieved and mapped to dictionaries.
    """
    # Insert multiple test records
    in_memory_db.save_report("First query", 11, 2, "First")
    in_memory_db.save_report("Second query text", 17, 3, "Second")

    # Fetch records
    records = in_memory_db.fetch_all_reports()

    # Assert records count and order (ORDER BY created_at DESC)
    assert len(records) == 2
    assert records[0]["input_text"] == "Second query text"
    assert records[1]["input_text"] == "First query"
    assert records[0]["longest_word"] == "Second"