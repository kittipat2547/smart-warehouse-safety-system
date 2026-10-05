import sqlite3
from pathlib import Path

from config import DATABASE_PATH


def get_connection():
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def init_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            camera TEXT,
            event_type TEXT NOT NULL,
            confidence REAL,
            image_path TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_code TEXT UNIQUE,
            product_name TEXT,
            quantity INTEGER DEFAULT 0,
            location TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_event(timestamp, event_type, confidence, image_path, camera):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO events
        (timestamp, camera, event_type, confidence, image_path)
        VALUES (?, ?, ?, ?, ?)
        """,
        (timestamp, camera, event_type, confidence, image_path)
    )

    conn.commit()
    conn.close()


def get_events(limit=100):
    conn = get_connection()

    cursor = conn.execute(
        """
        SELECT id, timestamp, camera, event_type,
               confidence, image_path
        FROM events
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_inventory():
    conn = get_connection()

    cursor = conn.execute(
        """
        SELECT id, product_code, product_name,
               quantity, location
        FROM inventory
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()
    return rows
