import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

from config import DATABASE_PATH, DB_RETENTION_DAYS


def get_connection():
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_connection()

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            camera TEXT,
            event_type TEXT NOT NULL,
            confidence REAL,
            image_path TEXT
        )
        """
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_code TEXT UNIQUE,
            product_name TEXT,
            quantity INTEGER DEFAULT 0,
            location TEXT
        )
        """
    )

    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_events_timestamp ON events(timestamp)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_events_event_type ON events(event_type)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_inventory_product_code ON inventory(product_code)"
    )

    conn.commit()
    conn.close()


def prune_old_events():
    conn = get_connection()
    cutoff = (datetime.now() - timedelta(days=DB_RETENTION_DAYS)).strftime("%Y-%m-%dT%H:%M:%S")
    conn.execute("DELETE FROM events WHERE timestamp < ?", (cutoff,))
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
        (timestamp, camera, event_type, confidence, image_path),
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
        (limit,),
    )

    rows = cursor.fetchall()
    conn.close()
    return [tuple(row) for row in rows]


def get_event_counts():
    conn = get_connection()
    cursor = conn.execute(
        """
        SELECT event_type, COUNT(*) as total
        FROM events
        GROUP BY event_type
        ORDER BY total DESC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return {row["event_type"]: row["total"] for row in rows}


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
    return [tuple(row) for row in rows]
