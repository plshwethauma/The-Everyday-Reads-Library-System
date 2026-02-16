#  The Everyday Reads  
### Library Management System (Python + Tkinter + SQLite)

**The Everyday Reads** is a desktop-based Library Management System built using **Python**, **Tkinter**, and **SQLite**.  
It supports both **Student** and **Admin** roles and handles book management, borrowing, returning, and issue tracking in a clean and user-friendly interface.

---

##  Features

###  Student Side
- View available books with live filtering (title / author / category)
- Borrow books (with availability check)
- View borrowed books using Student ID
- See issue date, return date, and days left
- Return borrowed books (auto-updates availability)

---

###  Admin Side
- Secure Admin Login
- Manage Books:
  - View all books
  - Add new books
  - Edit existing book details
- View Borrowed Books:
  - View all currently issued books
  - See student name, book title, issue date, return date
  - Automatically calculate **days left for return**
- Centralized Admin Dashboard

---

## Project Structure

The_Everyday_Reads/
│
├── main.py
│
├── ui/
│ ├── student_ui.py
│ ├── admin_ui.py
│ ├── admin_login.py
│ ├── admin_borrowed.py
│ ├── borrow_book.py
│ ├── view_borrowed.py
│ ├── admin_borrowed.py
│ ├── manage_books.py
│
├── utils/
│ └── db_connection.py
│
├── db/
│ ├── everyday_reads.db
│ └── db_setup.py
│
└── README.md


---

##  Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **SQLite3** (Database)
- **Datetime module** (date calculations)

---

##  Database Tables

- `etr_books` – Book details and availability
- `etr_students` – Student information
- `etr_issues` – Borrowed books record
- `etr_admins` – Admin login credentials

---

## Admin Login Credentials (Sample)

| Username    | Password  |
|------------|-----------|
| admin      | admin123  |
| librarian | read@123  |




Logic Highlights

Book availability automatically decreases on borrowing
Availability increases when a book is returned
Borrowing is blocked if no copies are available
Days left for return are calculated dynamically
Admin always sees real-time issue data



Future Enhancements 

Overdue fine calculation
Search & sort in admin borrowed view
Password encryption for admins
Export reports (CSV / PDF)


Developed By
Shwetha
Engineering Student
Python | Tkinter | SQLite