# db/db_setup.py
# -------------------------------------------------
# This script creates all database tables
# and inserts sample data for testing
# -------------------------------------------------

import sqlite3

# Connect to database 
conn = sqlite3.connect("db/everyday_reads.db")
cursor = conn.cursor()

# -------------------- CREATE TABLES --------------------

# BOOKS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS etr_books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    total_copies INTEGER NOT NULL,
    available_copies INTEGER NOT NULL
)
""")

# STUDENTS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS etr_students (
    student_id TEXT PRIMARY KEY,
    student_name TEXT NOT NULL
)
""")

# ISSUES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS etr_issues (
    issue_id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL,
    book_id TEXT NOT NULL,
    issue_date TEXT NOT NULL,
    return_date TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES etr_students(student_id),
    FOREIGN KEY(book_id) REFERENCES etr_books(book_id)
)
""")

# ADMINS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS etr_admins (
    admin_id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# -------------------- INSERT SAMPLE DATA --------------------

# BOOKS
cursor.executemany("""
INSERT OR IGNORE INTO etr_books VALUES (?,?,?,?,?,?)
""", [
    ('B001','Atomic Habits','James Clear','Self Help',5,5),
    ('B002','1984','George Orwell','Fiction',4,4),
    ('B003','Sapiens','Yuval Noah Harari','History',6,6),
    ('B004','Clean Code','Robert C Martin','Programming',3,3),
    ('B005','The Alchemist','Paulo Coelho','Fiction',7,7),
    ('B006','Ikigai','Hector Garcia','Self Help',5,5),
    ('B007','Python Crash Course','Eric Matthes','Programming',4,4),
    ('B008','Rich Dad Poor Dad','Robert Kiyosaki','Finance',6,6),
    ('B009','Deep Work','Cal Newport','Productivity',5,5),
    ('B010','Think Like a Monk','Jay Shetty','Self Help',4,4)
])

# STUDENTS
cursor.executemany("""
INSERT OR IGNORE INTO etr_students VALUES (?,?)
""", [
    ('S001','Aarav Mehta'),
    ('S002','Diya Sharma'),
    ('S003','Rohan Iyer'),
    ('S004','Ananya Rao'),
    ('S005','Karthik N'),
    ('S006','Meera Pillai'),
    ('S007','Aditya Singh'),
    ('S008','Nisha Verma'),
    ('S009','Rahul Das'),
    ('S010','Sneha Kapoor')
])

# ISSUES
cursor.executemany("""
INSERT OR IGNORE INTO etr_issues VALUES (?,?,?,?,?)
""", [
    ('I001','S001','B002','2026-02-01','2026-02-15'),
    ('I002','S002','B005','2026-02-03','2026-02-17'),
    ('I003','S003','B001','2026-02-05','2026-02-19'),
    ('I004','S004','B004','2026-02-06','2026-02-20'),
    ('I005','S005','B003','2026-02-07','2026-02-21'),
    ('I006','S006','B006','2026-02-08','2026-02-22'),
    ('I007','S007','B007','2026-02-09','2026-02-23'),
    ('I008','S008','B008','2026-02-10','2026-02-24'),
    ('I009','S009','B009','2026-02-11','2026-02-25'),
    ('I010','S010','B010','2026-02-12','2026-02-26')
])

# ADMINS
cursor.executemany("""
INSERT OR IGNORE INTO etr_admins VALUES (?,?,?)
""", [
    ('A001','admin','admin123'),
    ('A002','librarian','read@123')
])


# Commit and close
conn.commit()
conn.close()

print(" Database setup completed successfully!")
