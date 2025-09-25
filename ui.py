import tkinter as tk
from tkinter import messagebox
import database

def refresh_books(listbox):
    listbox.delete(0, tk.END)
    books = database.get_all_books()
    for book in books:
        status = "Available" if book[3] else "Borrowed"
        listbox.insert(tk.END, f"{book[0]} | {book[1]} by {book[2]} - {status}")

def add_book_ui(title_entry, author_entry, listbox):
    title = title_entry.get()
    author = author_entry.get()
    if title:
        database.add_book(title, author)
        messagebox.showinfo("Success", "Book added!")
        refresh_books(listbox)
    else:
        messagebox.showwarning("Error", "Title cannot be empty!")

def launch_ui():
    root = tk.Tk()
    root.title("Library Management System")

    # Frames
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    tk.Label(frame, text="Title:").grid(row=0, column=0)
    title_entry = tk.Entry(frame)
    title_entry.grid(row=0, column=1)

    tk.Label(frame, text="Author:").grid(row=1, column=0)
    author_entry = tk.Entry(frame)
    author_entry.grid(row=1, column=1)

    book_listbox = tk.Listbox(frame, width=50)
    book_listbox.grid(row=3, column=0, columnspan=2, pady=10)

    tk.Button(frame, text="Add Book", 
              command=lambda: add_book_ui(title_entry, author_entry, book_listbox)).grid(row=2, column=0, columnspan=2)

    refresh_books(book_listbox)
    root.mainloop()
