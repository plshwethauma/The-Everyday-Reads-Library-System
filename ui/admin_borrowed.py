# ui/admin_borrowed.py
# ----------------------------------------------------
# Admin View – All Borrowed Books
# ----------------------------------------------------

import tkinter as tk
from tkinter import ttk
from utils.db_connection import get_connection
from datetime import datetime

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"


def open_admin_borrowed():
    win = tk.Toplevel()
    win.title("Admin – Borrowed Books")
    win.configure(bg=BG_COLOR)
    win.state("zoomed")

    # ================= TITLE =================
    tk.Label(
        win,
        text="Issued Books",
        font=("Times New Roman", 28, "bold"),
        bg=BG_COLOR,
        fg=BTN_COLOR
    ).pack(pady=20)

    # ================= TABLE =================
    columns = (
        "Issue ID",
        "Student ID",
        "Student Name",
        "Book ID",
        "Book Title",
        "Issue Date",
        "Return Date",
        "Days Left"
    )

    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=160)

    tree.pack(expand=True, fill="both", padx=30, pady=20)

    # ================= LOAD DATA =================
    def load_all_borrowed():
        tree.delete(*tree.get_children())

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                i.issue_id,
                s.student_id,
                s.student_name,
                b.book_id,
                b.title,
                i.issue_date,
                i.return_date
            FROM etr_issues i
            JOIN etr_students s ON i.student_id = s.student_id
            JOIN etr_books b ON i.book_id = b.book_id
        """)

        rows = cur.fetchall()
        conn.close()

        today = datetime.now()

        for r in rows:
            days_left = (datetime.strptime(r[6], "%Y-%m-%d") - today).days
            tree.insert("", "end", values=(*r, days_left))

    load_all_borrowed()

    # ================= EXIT =================
    tk.Button(
        win,
        text="Back to Admin Home",
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 14, "bold"),
        command=win.destroy
    ).pack(pady=20)
