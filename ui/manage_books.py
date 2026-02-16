# ui/manage_books.py
# -------------------------------------------------
# Manage Books (Admin)
# -------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
from utils.db_connection import get_connection

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_manage_books():
    win = tk.Toplevel()
    win.title("Manage Books")
    win.configure(bg=BG_COLOR)
    win.state("zoomed")

    # ================= TABLE =================
    columns = ("Book ID", "Title", "Author", "Category", "Total", "Available")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=160)

    tree.pack(expand=True, fill="both", padx=30, pady=20)

    # ================= LOAD BOOKS =================
    def load_books():
        tree.delete(*tree.get_children())
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM etr_books")
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    load_books()

    # ================= FORM =================
    form = tk.Frame(win, bg=BG_COLOR)
    form.pack(pady=20)

    labels = ["Book ID", "Title", "Author", "Category", "Total Copies", "Available Copies"]
    entries = {}

    for i, lbl in enumerate(labels):
        tk.Label(form, text=lbl, bg=BG_COLOR).grid(row=i, column=0, pady=5)
        ent = tk.Entry(form, width=30)
        ent.grid(row=i, column=1, pady=5)
        entries[lbl] = ent

    # ================= SELECT BOOK =================
    def select_book(event):
        selected = tree.focus()
        if not selected:
            return
        values = tree.item(selected)["values"]
        for i, key in enumerate(labels):
            entries[key].delete(0, tk.END)
            entries[key].insert(0, values[i])

    tree.bind("<ButtonRelease-1>", select_book)

    # ================= ADD BOOK =================
    def add_book():
        data = [entries[l].get().strip() for l in labels]
        if "" in data:
            messagebox.showerror("Error", "All fields required")
            return

        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO etr_books VALUES (?,?,?,?,?,?)", data)
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully")
            load_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        conn.close()

    # ================= UPDATE BOOK =================
    def update_book():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE etr_books
            SET title=?, author=?, category=?, total_copies=?, available_copies=?
            WHERE book_id=?
        """, (
            entries["Title"].get(),
            entries["Author"].get(),
            entries["Category"].get(),
            entries["Total Copies"].get(),
            entries["Available Copies"].get(),
            entries["Book ID"].get()
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book updated successfully")
        load_books()

    # ================= BUTTONS =================
    btns = tk.Frame(win, bg=BG_COLOR)
    btns.pack(pady=20)

    tk.Button(btns, text="Add Book", bg=BTN_COLOR, fg=TEXT_COLOR, command=add_book).grid(row=0, column=0, padx=10)
    tk.Button(btns, text="Update Book", bg=BTN_COLOR, fg=TEXT_COLOR, command=update_book).grid(row=0, column=1, padx=10)
    tk.Button(btns, text="Exit", bg="brown", fg="white", command=win.destroy).grid(row=0, column=2, padx=10)
