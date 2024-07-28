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
            CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL DEFAULT (datetime('now','localtime')),
            type TEXT NOT NULL,
            amount INTEGER NOT NULL,
            description TEXT
            );
        """
    cur.execute(expense_table)
    conn.commit()
    conn.close()

create_table()