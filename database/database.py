import sqlite3
from auth import add_user


def send_query(query):
    conn = get_connection()
    if conn is None:
        return False
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    return c


def get_connection():
    try:
        conn = sqlite3.connect('identifier.sqlite')
        if conn is not None:
            return conn
        else:
            return None
    except sqlite3.Error as error:
        print(error)


def create_database():
    try:
        conn = sqlite3.connect('identifier.sqlite')
        c = conn.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password_hash TEXT NOT NULL,
                        role TEXT NOT NULL,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        registration_date TEXT NOT NULL
                    )
                ''')
        # Create members table
        c.execute('''
                    CREATE TABLE IF NOT EXISTS members (
                        id SERIAL PRIMARY KEY,
                        membership_id TEXT NOT NULL UNIQUE,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        weight TEXT NOT NULL,
                        address TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        registration_date TEXT NOT NULL
                    )
                ''')
        # Create logs table
        c.execute('''
                    CREATE TABLE IF NOT EXISTS logs (
                        id SERIAL PRIMARY KEY,
                        date TEXT NOT NULL,
                        time TEXT NOT NULL,
                        username TEXT NOT NULL,
                        description TEXT NOT NULL,
                        suspicious TEXT NOT NULL
                    )
                ''')
        conn.commit()
    except sqlite3.Error as error:
        print(error)


def seed_database():
    add_user("super_admin", "Admin123?", "super_admin", "Jonna", "Jimmy")


def prepare_database():
    create_database()
    seed_database()
