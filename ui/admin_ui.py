# ui/admin_ui.py
# -------------------------------------------------
# Admin Dashboard
# -------------------------------------------------

import tkinter as tk
from ui.manage_books import open_manage_books
from ui.admin_borrowed import open_admin_borrowed   

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_admin_dashboard():
    win = tk.Toplevel()
    win.title("Admin Dashboard - The Everyday Reads")
    win.configure(bg=BG_COLOR)
    win.state("zoomed")

    tk.Label(
        win,
        text="Admin Dashboard",
        font=("Times New Roman", 28, "bold"),
        bg=BG_COLOR,
        fg=BTN_COLOR
    ).pack(pady=40)

    # ---------------- MANAGE BOOKS ----------------
    tk.Button(
        win, text="Manage Books",
        font=("Arial", 18, "bold"),
        bg=BTN_COLOR, fg=TEXT_COLOR,
        width=25,
        command=open_manage_books
    ).pack(pady=20)


    tk.Button(
        win, text="View Issued Books",
        font=("Arial", 18, "bold"),
        bg=BTN_COLOR, fg=TEXT_COLOR,
        width=25,
        command=open_admin_borrowed
    ).pack(pady=20)

    # ---------------- EXIT ----------------
    tk.Button(
        win, text="Exit",
        font=("Arial", 16, "bold"),
        bg="brown", fg="white",
        width=15,
        command=win.destroy
    ).pack(pady=40)
