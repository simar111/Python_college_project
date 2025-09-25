import tkinter as tk
from tkinter import messagebox
import database, utils
from datetime import datetime

def refresh_borrows(listbox):
    listbox.delete(0, tk.END)
    borrows = database.get_active_borrows()
    for b in borrows:
        listbox.insert(tk.END, f"TransID:{b[0]} | {b[1]} borrowed {b[2]} on {b[3]}")

def borrow_window():
    win = tk.Toplevel()
    win.title("Borrow/Return")
    win.geometry("600x450")

    # Borrow Section
    tk.Label(win, text="Student ID:").pack()
    student_entry = tk.Entry(win)
    student_entry.pack()

    tk.Label(win, text="Book ID:").pack()
    book_entry = tk.Entry(win)
    book_entry.pack()

    def borrow_book():
        sid = student_entry.get()
        bid = book_entry.get()
        if sid.isdigit() and bid.isdigit():
            success = database.borrow_book(int(sid), int(bid), datetime.now().strftime("%Y-%m-%d"))
            if success:
                messagebox.showinfo("Success", "Book borrowed!")
                refresh_borrows(borrow_listbox)
            else:
                messagebox.showerror("Error", "Book not available")
        else:
            messagebox.showerror("Error", "Invalid IDs")

    tk.Button(win, text="Borrow", command=borrow_book).pack(pady=5)

    # Return Section
    tk.Label(win, text="Transaction ID (to return):").pack()
    trans_entry = tk.Entry(win)
    trans_entry.pack()

    def return_book():
        tid = trans_entry.get()
        if tid.isdigit():
            today = datetime.now().strftime("%Y-%m-%d")
            # fetch borrow_date
            borrows = database.get_active_borrows()
            for b in borrows:
                if b[0] == int(tid):
                    fine = utils.calculate_fine(b[3], today)
                    database.return_book(int(tid), today, fine)
                    messagebox.showinfo("Returned", f"Book returned! Fine: ₹{fine}")
                    refresh_borrows(borrow_listbox)
                    return
            messagebox.showerror("Error", "Invalid transaction ID")
        else:
            messagebox.showerror("Error", "Invalid input")

    tk.Button(win, text="Return Book", command=return_book).pack(pady=5)

    borrow_listbox = tk.Listbox(win, width=80)
    borrow_listbox.pack(pady=10)

    refresh_borrows(borrow_listbox)
