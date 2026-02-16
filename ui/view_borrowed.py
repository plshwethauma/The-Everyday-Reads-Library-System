# ui/view_borrowed.py
# ----------------------------------------------------
# View Borrowed Books + Return Book
# ----------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
from utils.db_connection import get_connection
from datetime import datetime

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_view_borrowed():
    win = tk.Toplevel()
    win.title("View Borrowed Books")
    win.configure(bg=BG_COLOR)
    win.state("zoomed")

    # ================= TOP =================
    top = tk.Frame(win, bg=BG_COLOR)
    top.pack(pady=20)

    tk.Label(top, text="Student ID:", bg=BG_COLOR, font=("Arial", 14)).pack(side="left")
    sid_entry = tk.Entry(top, font=("Arial", 14), width=20)
    sid_entry.pack(side="left", padx=10)

    # ================= TABLE =================
    columns = ("Issue ID", "Book ID", "Title", "Issue Date", "Return Date", "Days Left")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=180)

    tree.pack(expand=True, fill="both", padx=30, pady=20)

    # ================= LOAD =================
    def load_books():
        tree.delete(*tree.get_children())
        sid = sid_entry.get().strip()

        if not sid:
            messagebox.showerror("Error", "Enter Student ID")
            return

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT i.issue_id, b.book_id, b.title, i.issue_date, i.return_date
            FROM etr_issues i
            JOIN etr_books b ON i.book_id = b.book_id
            WHERE i.student_id = ?
        """, (sid,))

        rows = cur.fetchall()
        conn.close()

        today = datetime.now()

        for r in rows:
            days_left = (datetime.strptime(r[4], "%Y-%m-%d") - today).days
            tree.insert("", "end", values=(*r, days_left))

    # ================= RETURN BOOK =================
    def return_book():
        selected = tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a book")
            return

        issue_id, book_id = tree.item(selected)["values"][:2]

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM etr_issues WHERE issue_id=?", (issue_id,))
        cur.execute("""
            UPDATE etr_books
            SET available_copies = available_copies + 1
            WHERE book_id = ?
        """, (book_id,))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Book returned successfully!")
        load_books()

    # ================= BUTTONS =================
    tk.Button(
        top, text="View",
        bg=BTN_COLOR, fg=TEXT_COLOR,
        font=("Arial", 14, "bold"),
        command=load_books
    ).pack(side="left", padx=10)

    tk.Button(
        win, text="Return Selected Book",
        bg=BTN_COLOR, fg=TEXT_COLOR,
        font=("Arial", 14, "bold"),
        command=return_book
    ).pack(pady=10)
