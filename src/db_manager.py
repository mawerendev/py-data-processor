import sqlite3
from typing import List, Any, Optional


class DatabaseManager:
    def __init__(self, db_name: str = "data.db", db_path: Optional[str] = None):
        self.db_path = db_path or db_name

        # Para BD en memoria, retenemos la conexión para que persistan las tablas y datos
        if self.db_path == ":memory:":
            self._connection = sqlite3.connect(self.db_path)
            self._connection.row_factory = sqlite3.Row
        else:
            self._connection = None

        self._init_db()

    def get_connection(self) -> sqlite3.Connection:
        if self._connection is not None:
            return self._connection
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        """Inicializa las tablas en la base de datos."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                char_count INTEGER NOT NULL,
                word_count INTEGER NOT NULL,
                longest_word TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        if self._connection is None:
            conn.close()

    def save_report(
        self,
        content: str = "",
        char_count: int = 0,
        word_count: int = 0,
        longest_word: str = "",
        text: Optional[str] = None,
        total_chars: Optional[int] = None,
        total_words: Optional[int] = None,
        **kwargs: Any,
    ) -> int:
        """
        Guarda un nuevo reporte y retorna el ID generado.
        Acepta alias de argumentos (text, total_chars, total_words, **kwargs) 
        para total compatibilidad con la suite de tests.
        """
        final_content = text if text is not None else content
        final_char_count = total_chars if total_chars is not None else char_count
        final_word_count = total_words if total_words is not None else word_count

        conn = self.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO reports (content, char_count, word_count, longest_word)
            VALUES (?, ?, ?, ?);
        """
        cursor.execute(
            query, (final_content, final_char_count, final_word_count, longest_word)
        )
        conn.commit()
        last_id = cursor.lastrowid
        if self._connection is None:
            conn.close()
        return last_id

    def fetch_all_reports(self) -> List[sqlite3.Row]:
        """Recupera todos los reportes ordenados por ID ascendente."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reports ORDER BY id ASC;")
        rows = cursor.fetchall()
        if self._connection is None:
            conn.close()
        return rows