# ----------------------------------------------------
# Admin Login Page
# ----------------------------------------------------

import tkinter as tk
from tkinter import messagebox
from utils.db_connection import get_connection
from ui.admin_ui import open_admin_dashboard

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_admin_login():
    win = tk.Toplevel()
    win.title("Admin Login")
    win.configure(bg=BG_COLOR)
    win.geometry("500x400")
    win.resizable(False, False)

    # ---------------- TITLE ----------------
    tk.Label(
        win,
        text="Admin Login",
        font=("Times New Roman", 26, "bold"),
        bg=BG_COLOR,
        fg=BTN_COLOR
    ).pack(pady=30)

    # ---------------- FORM ----------------
    frame = tk.Frame(win, bg=BG_COLOR)
    frame.pack(pady=20)

    tk.Label(frame, text="Username", bg=BG_COLOR, font=("Arial", 12)).grid(row=0, column=0, pady=10, sticky="w")
    username_entry = tk.Entry(frame, width=25, font=("Arial", 12))
    username_entry.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Password", bg=BG_COLOR, font=("Arial", 12)).grid(row=1, column=0, pady=10, sticky="w")
    password_entry = tk.Entry(frame, width=25, show="*", font=("Arial", 12))
    password_entry.grid(row=1, column=1, pady=10)

    # ---------------- LOGIN LOGIC ----------------
    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM etr_admins
            WHERE username = ? AND password = ?
        """, (username, password))

        admin = cursor.fetchone()
        conn.close()

        if admin:
            messagebox.showinfo("Success", "Login successful!")
            win.destroy()
            open_admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # ---------------- BUTTONS ----------------
    tk.Button(
        win,
        text="Login",
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 14, "bold"),
        width=15,
        command=login
    ).pack(pady=20)

    tk.Button(
        win,
        text="Cancel",
        font=("Arial", 12),
        command=win.destroy
    ).pack()
