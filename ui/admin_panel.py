import tkinter as tk
from ui import books_screen, students_screen, borrow_screen

def admin_panel_window():
    root = tk.Tk()
    root.title("Admin Panel")
    root.geometry("400x250")

    tk.Label(root, text="Library Management System", font=("Arial", 16, "bold")).pack(pady=20)

    tk.Button(root, text="📚 Manage Books", width=20, command=books_screen.books_window).pack(pady=5)
    tk.Button(root, text="👩‍🎓 Manage Students", width=20, command=students_screen.students_window).pack(pady=5)
    tk.Button(root, text="📖 Borrow / Return", width=20, command=borrow_screen.borrow_window).pack(pady=5)

    tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)

    root.mainloop()
