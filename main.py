# main.py
# ----------------------------------------------------
# Home Screen for "The Everyday Reads"
# Allows user to enter as Student or Admin
# ----------------------------------------------------

import tkinter as tk
from tkinter import messagebox
from ui.student_ui import open_student_ui
from ui.admin_login import open_admin_login

# -------------------- COLORS --------------------
BG_COLOR = "#F9E7B2"      
BTN_COLOR = "#562F00"     
TEXT_COLOR = "white"

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("The Everyday Reads")
root.configure(bg=BG_COLOR)

# Full screen window
root.state("zoomed")

# -------------------- FUNCTIONS --------------------

def enter_student():
    open_student_ui()

def enter_admin():
    open_admin_login()

# -------------------- MAIN FRAME --------------------
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(expand=True)

# -------------------- TITLE --------------------
title_label = tk.Label(
    main_frame,
    text="The Everyday Reads",
    font=("Times New Roman", 36, "bold"),
    bg=BG_COLOR,
    fg=BTN_COLOR
)
title_label.pack(pady=40)

subtitle_label = tk.Label(
    main_frame,
    text="Library Management System",
    font=("Times New Roman", 18),
    bg=BG_COLOR,
    fg=BTN_COLOR
)
subtitle_label.pack(pady=10)

# -------------------- BUTTONS FRAME --------------------
button_frame = tk.Frame(main_frame, bg=BG_COLOR)
button_frame.pack(pady=60)

# Student Button
student_btn = tk.Button(
    button_frame,
    text="Enter as Student",
    font=("Arial", 16, "bold"),
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    width=20,
    height=2,
    command=enter_student
)
student_btn.grid(row=0, column=0, padx=30)

# Admin Button
admin_btn = tk.Button(
    button_frame,
    text="Enter as Admin",
    font=("Arial", 16, "bold"),
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    width=20,
    height=2,
    command=enter_admin
)
admin_btn.grid(row=0, column=1, padx=30)

# -------------------- FOOTER --------------------
footer_label = tk.Label(
    root,
    text="Developed by Pl Shwetha Uma",
    bg=BG_COLOR,
    fg=BTN_COLOR,
    font=("Arial", 10)
)
footer_label.pack(side="bottom", pady=10)

# -------------------- RUN APP --------------------
root.mainloop()
