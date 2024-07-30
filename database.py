import sqlite3


def createdatabase():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        telegram_id INTEGER UNIQUE,
        name TEXT,
        category1 TEXT,
        category2 TEXT,
        category3 TEXT,
        expenses1 REAL,
        expenses2 REAL,
        expenses3 REAL
        )
    ''')

    conn.commit()
    