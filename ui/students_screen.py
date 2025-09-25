import tkinter as tk
from tkinter import messagebox
import database

def refresh_students(listbox):
    listbox.delete(0, tk.END)
    students = database.get_all_students()
    for s in students:
        listbox.insert(tk.END, f"ID:{s[0]} | {s[1]} | {s[2]} | {s[3]}")

def students_window():
    win = tk.Toplevel()
    win.title("Students Management")
    win.geometry("500x400")

    tk.Label(win, text="Name:").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Email:").pack()
    email_entry = tk.Entry(win)
    email_entry.pack()

    tk.Label(win, text="Contact:").pack()
    contact_entry = tk.Entry(win)
    contact_entry.pack()

    student_listbox = tk.Listbox(win, width=60)
    student_listbox.pack(pady=10)

    def add_student():
        name = name_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        if name:
            database.add_student(name, email, contact)
            messagebox.showinfo("Success", "Student added!")
            refresh_students(student_listbox)
        else:
            messagebox.showerror("Error", "Name required")

    tk.Button(win, text="Add Student", command=add_student).pack(pady=5)

    refresh_students(student_listbox)
