import tkinter as tk
from tkinter import messagebox
import database

def refresh_books(listbox):
    listbox.delete(0, tk.END)
    books = database.get_all_books()
    for b in books:
        listbox.insert(tk.END, f"ID:{b[0]} | {b[1]} by {b[2]} | Qty:{b[3]}")

def books_window():
    win = tk.Toplevel()
    win.title("Books Management")
    win.geometry("500x400")

    # Add book
    tk.Label(win, text="Title:").pack()
    title_entry = tk.Entry(win)
    title_entry.pack()

    tk.Label(win, text="Author:").pack()
    author_entry = tk.Entry(win)
    author_entry.pack()

    tk.Label(win, text="Quantity:").pack()
    qty_entry = tk.Entry(win)
    qty_entry.pack()

    book_listbox = tk.Listbox(win, width=60)
    book_listbox.pack(pady=10)

    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        qty = qty_entry.get()
        if title and qty.isdigit():
            database.add_book(title, author, int(qty))
            messagebox.showinfo("Success", "Book added!")
            refresh_books(book_listbox)
        else:
            messagebox.showerror("Error", "Invalid details")

    tk.Button(win, text="Add Book", command=add_book).pack(pady=5)

    refresh_books(book_listbox)
