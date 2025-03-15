import sqlite3

def initialize_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  description TEXT NOT NULL,
                  completed INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()