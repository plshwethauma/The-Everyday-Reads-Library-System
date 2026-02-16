# ui/borrow_book.py
# ----------------------------------------------------
# Borrow Book Page
# ----------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
from utils.db_connection import get_connection
from datetime import datetime

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_borrow_book():
    win = tk.Toplevel()
    win.title("Borrow Book - The Everyday Reads")
    win.configure(bg=BG_COLOR)
    win.state("zoomed")

    conn = get_connection()
    cursor = conn.cursor()

    # ================== MAIN LAYOUT ==================
    main_frame = tk.Frame(win, bg=BG_COLOR)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    left_frame = tk.Frame(main_frame, bg=BG_COLOR)
    left_frame.pack(side="left", expand=True, fill="both")

    right_frame = tk.Frame(main_frame, bg=BG_COLOR, width=350)
    right_frame.pack(side="right", fill="y", padx=30)

    # ================== FILTER ==================
    filter_frame = tk.Frame(left_frame, bg=BG_COLOR)
    filter_frame.pack(pady=10)

    tk.Label(filter_frame, text="Filter by:", bg=BG_COLOR).grid(row=0, column=0)

    filter_by = tk.StringVar(value="title")
    ttk.Combobox(
        filter_frame,
        textvariable=filter_by,
        values=["title", "author", "category"],
        state="readonly",
        width=12
    ).grid(row=0, column=1, padx=5)

    filter_text = tk.StringVar()
    tk.Entry(filter_frame, textvariable=filter_text, width=30).grid(row=0, column=2)

    # ================== BOOK TABLE ==================
    columns = ("Book ID", "Title", "Author", "Category", "Total", "Available")
    tree = ttk.Treeview(left_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)

    tree.pack(expand=True, fill="both", pady=10)

    def load_books():
        tree.delete(*tree.get_children())
        query = f"""
            SELECT book_id, title, author, category, total_copies, available_copies
            FROM etr_books
            WHERE {filter_by.get()} LIKE ?
        """
        cursor.execute(query, (f"%{filter_text.get()}%",))
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

    filter_text.trace_add("write", lambda *a: load_books())
    load_books()

    # ================== BORROW FORM ==================
    tk.Label(
        right_frame, text="Borrow Book",
        font=("Times New Roman", 22, "bold"),
        bg=BG_COLOR, fg=BTN_COLOR
    ).pack(pady=20)

    fields = {}
    for label in ["Student ID", "Book ID", "Issue Date (YYYY-MM-DD)", "Return Date (YYYY-MM-DD)"]:
        tk.Label(right_frame, text=label, bg=BG_COLOR).pack(anchor="w")
        entry = tk.Entry(right_frame, width=25)
        entry.pack(pady=5)
        fields[label] = entry

    #  Auto-fill Book ID on double click
    def fill_book_id(event):
        selected = tree.focus()
        if selected:
            fields["Book ID"].delete(0, tk.END)
            fields["Book ID"].insert(0, tree.item(selected)["values"][0])

    tree.bind("<Double-1>", fill_book_id)

    # ================== BORROW LOGIC ==================
    def borrow_book():
        sid = fields["Student ID"].get().strip()
        bid = fields["Book ID"].get().strip()
        issue = fields["Issue Date (YYYY-MM-DD)"].get().strip()
        ret = fields["Return Date (YYYY-MM-DD)"].get().strip()

        if not all([sid, bid, issue, ret]):
            messagebox.showerror("Error", "All fields required")
            return

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT available_copies FROM etr_books WHERE book_id=?", (bid,))
        row = cur.fetchone()

        if not row or row[0] <= 0:
            messagebox.showerror("Error", "Book not available")
            conn.close()
            return

        issue_id = "I" + datetime.now().strftime("%Y%m%d%H%M%S")

        cur.execute("""
            INSERT INTO etr_issues VALUES (?,?,?,?,?)
        """, (issue_id, sid, bid, issue, ret))

        cur.execute("""
            UPDATE etr_books
            SET available_copies = available_copies - 1
            WHERE book_id = ?
        """, (bid,))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Book borrowed successfully!")
        win.destroy()

    tk.Button(
        right_frame, text="Borrow Book",
        bg=BTN_COLOR, fg=TEXT_COLOR,
        font=("Arial", 14, "bold"),
        command=borrow_book
    ).pack(pady=30)
