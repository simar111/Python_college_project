import tkinter as tk
from tkinter import messagebox
import database
from ui import admin_panel

def login_window():
    root = tk.Tk()
    root.title("Library Login")
    root.geometry("300x180")

    tk.Label(root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        if database.check_admin(username, password):
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()
            admin_panel.admin_panel_window()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=attempt_login).pack(pady=10)

    root.mainloop()
