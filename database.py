import sqlite3

#function to build a connection

def build_connection():
    conn = sqlite3.connect('expenses.db') 
    return conn

#function to create table

def create_table():
    conn = build_connection()
    cur = conn.cursor()

    expense_table = """
            CREATE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            amount INTEGER NOT NULL,
            description TEXT
            );
        """
    cur.execute(create_table)
    conn.commit()
    conn.close()
