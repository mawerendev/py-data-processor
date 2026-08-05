import sqlite3
from typing import List, Dict, Any


class DatabaseManager:
    """
    Manages SQLite database connections, schema creation, 
    and CRUD operations for text processing metrics.
    """

    def __init__(self, db_name: str = "database.db"):
        self.db_name = db_name
        self._shared_conn = None

        # Hold a continuous connection in memory if test mode is enabled
        if self.db_name == ":memory:":
            self._shared_conn = sqlite3.connect(":memory:")

        self._create_table()

    def _get_connection(self) -> sqlite3.Connection:
        """Establishes and returns a connection to the SQLite database."""
        if self.db_name == ":memory:":
            return self._shared_conn
        return sqlite3.connect(self.db_name)

    def _create_table(self) -> None:
        """Creates the 'reports' table if it does not already exist."""
        query = """
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT NOT NULL,
            total_characters INTEGER NOT NULL,
            total_words INTEGER NOT NULL,
            longest_word TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        if self.db_name != ":memory:":
            conn.close()

    def save_report(self, text: str, total_chars: int, total_words: int, longest_word: str) -> int:
        """
        Inserts a new metric record into the database table.
        Returns the inserted record ID.
        """
        query = """
        INSERT INTO reports (input_text, total_characters, total_words, longest_word)
        VALUES (?, ?, ?, ?);
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (text, total_chars, total_words, longest_word))
        conn.commit()
        last_id = cursor.lastrowid
        if self.db_name != ":memory:":
            conn.close()
        return last_id

    def fetch_all_reports(self) -> List[Dict[str, Any]]:
        """Retrieves all stored records from the database."""
        query = "SELECT id, input_text, total_characters, total_words, longest_word, created_at FROM reports ORDER BY created_at DESC;"
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        if self.db_name != ":memory:":
            conn.close()
            
        reports = []
        for row in rows:
            reports.append({
                "id": row[0],
                "input_text": row[1],
                "total_characters": row[2],
                "total_words": row[3],
                "longest_word": row[4],
                "created_at": row[5]
            })
        return reports