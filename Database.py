import sqlite3

DB_NAME = "capstone.db"

def init_db():
    """Initialize SQLite database and create the exam_logs table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exam_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            total_marks INTEGER NOT NULL,
            generated_paper TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_exam_to_db(topic: str, total_marks: int, generated_paper: str):
    """Insert a new generated exam paper into the database."""
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO exam_logs (topic, total_marks, generated_paper)
        VALUES (?, ?, ?)
    ''', (topic, total_marks, generated_paper))
    conn.commit()
    conn.close()

# Auto-initialize database on import
init_db()