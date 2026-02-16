# ui/student_ui.py
# ----------------------------------------------------
# Student Home Page
# ----------------------------------------------------

import tkinter as tk
from ui.borrow_book import open_borrow_book
from ui.view_borrowed import open_view_borrowed

BG_COLOR = "#F9E7B2"
BTN_COLOR = "#562F00"
TEXT_COLOR = "white"

def open_student_ui():
    student_win = tk.Toplevel()
    student_win.title("Student - The Everyday Reads")
    student_win.configure(bg=BG_COLOR)
    student_win.state("zoomed")

    frame = tk.Frame(student_win, bg=BG_COLOR)
    frame.pack(expand=True)

    tk.Label(
        frame,
        text="Student Portal",
        font=("Times New Roman", 30, "bold"),
        bg=BG_COLOR,
        fg=BTN_COLOR
    ).pack(pady=40)

    tk.Button(
        frame,
        text="Borrow a Book",
        font=("Arial", 16, "bold"),
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        width=25,
        height=2,
        command=open_borrow_book
    ).pack(pady=20)

    tk.Button(
        frame,
        text="View Borrowed Books",
        font=("Arial", 16, "bold"),
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        width=25,
        height=2,
        command=open_view_borrowed
    ).pack(pady=20)

    tk.Button(
        frame,
        text="Exit",
        font=("Arial", 14),
        bg="gray",
        fg="white",
        width=15,
        command=student_win.destroy
    ).pack(pady=40)
