# ui/manage_issues.py
# -------------------------------------------------
# Manage Issues (Admin)
# -------------------------------------------------

import tkinter as tk
from tkinter import ttk
from utils.db_connection import get_connection
from datetime import datetime

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_manage_issues():
    win = tk.Toplevel()
    win.title("Manage Issues")
    win.configure(bg=BG_COLOR)
    win.state("zoomed")

    # ================= SORT =================
    top = tk.Frame(win, bg=BG_COLOR)
    top.pack(pady=10)

    tk.Label(top, text="Sort By:", bg=BG_COLOR).pack(side="left")

    sort_var = tk.StringVar(value="All")
    ttk.Combobox(
        top,
        textvariable=sort_var,
        values=["All", "Student"],
        state="readonly",
        width=15
    ).pack(side="left", padx=10)

    # ================= TABLE =================
    columns = ("Student", "Book", "Issue Date", "Return Date", "Days Left")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=200)

    tree.pack(expand=True, fill="both", padx=30, pady=20)

    # ================= LOAD ISSUES =================
    def load_issues():
        tree.delete(*tree.get_children())
        conn = get_connection()
        cur = conn.cursor()

        query = """
            SELECT s.student_name, b.title, i.issue_date, i.return_date
            FROM etr_issues i
            JOIN etr_students s ON i.student_id = s.student_id
            JOIN etr_books b ON i.book_id = b.book_id
        """

        if sort_var.get() == "Student":
            query += " ORDER BY s.student_name"

        cur.execute(query)
        rows = cur.fetchall()
        conn.close()

        today = datetime.now()

        for r in rows:
            days_left = (datetime.strptime(r[3], "%Y-%m-%d") - today).days
            tree.insert("", "end", values=(*r, days_left))

    sort_var.trace_add("write", lambda *a: load_issues())
    load_issues()

    # ================= EXIT =================
    tk.Button(
        win, text="Exit",
        bg="brown", fg="white",
        font=("Arial", 14, "bold"),
        command=win.destroy
    ).pack(pady=20)
