import sqlite3
import random


def init_db_user(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """
    )


def init_db_products(cursor, conn):
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        image INTEGER,
        price INTEGER,
        quantity INTEGER,
        user TEXT
    )
    """
    )
    add_products(cursor)
    conn.commit()


def add_products(cursor):
    for i in range(1, 11):
        cursor.execute(
            """
            INSERT INTO products (id, name, description, image, price, quantity, user)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                i,
                f"product number -- {i}",
                "Advanced fitness tracker with heart rate monitoring and GPS functionality.",
                f"{random.randint(1, 10)}.jpg",
                random.randint(100, 1000),
                0,
                "",
            ),
        )


def fetch_user(username: str, password: str):
    print("fetching user")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Solution: Parameterized queries
    # cursor.execute(
    #     "SELECT * FROM users WHERE username=? AND password=?", (username, password)
    # )

    cursor.execute(
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    )
    user = cursor.fetchone()
    print("user", user)
    conn.close()
    return user is not None


def check_db_user():
    # print("checking db")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Check if the users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    if cursor.fetchone() is None:
        # If the users table doesn't exist, initialize the database
        init_db_user(cursor)
    else:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print("[LOG] check_db_user says := ", row)
    conn.close()


def check_db_products():
    print("[LOG] check_db_products says := checking db")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='products'"
    )
    if cursor.fetchone() is None:
        print("creating products table")
        init_db_products(cursor, conn)
    else:
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                # print(row)
                pass
        else:
            print("no products in table")
    conn.close()


def drop_tables():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE users")
    conn.close()
