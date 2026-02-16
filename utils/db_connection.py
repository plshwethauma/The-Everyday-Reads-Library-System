# utils/db_connection.py
# ----------------------------------------------------
# Centralized database connection (SAFE PATH)
# ----------------------------------------------------

import sqlite3
import os

def get_connection():
    # Get absolute path of project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Point explicitly to db/everyday_reads.db
    db_path = os.path.join(base_dir, "db", "everyday_reads.db")


    conn = sqlite3.connect(db_path)
    return conn
