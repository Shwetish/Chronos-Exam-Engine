import sqlite3

# Connects to capstone.db (creates the file automatically if it doesn't exist)
conn = sqlite3.connect('capstone.db')
cursor = conn.cursor()

# Create table for storing generated exam papers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS generated_exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        total_marks INTEGER NOT NULL,
        questions_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

print("Database 'capstone.db' initialized successfully with 'generated_exams' table.")

