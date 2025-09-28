import sqlite3

DB_NAME = "library.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Admin
    cur.execute("""CREATE TABLE IF NOT EXISTS admin (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT)""")

    # Insert default admin if not exists
    cur.execute("SELECT * FROM admin WHERE username=?", ("admin",))
    if not cur.fetchone():
        cur.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ("admin", "admin123"))

    # Books
    cur.execute("""CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT,
                    quantity INTEGER DEFAULT 1)""")

    # Students
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    contact TEXT)""")

    # Transactions
    cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    book_id INTEGER,
                    borrow_date TEXT,
                    return_date TEXT,
                    fine INTEGER DEFAULT 0,
                    FOREIGN KEY(student_id) REFERENCES students(id),
                    FOREIGN KEY(book_id) REFERENCES books(id))""")

    conn.commit()
    conn.close()

# --- Admin ---
def check_admin(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
    row = cur.fetchone()
    conn.close()
    return row

# --- Books ---
def add_book(title, author, qty):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", (title, author, qty))
    conn.commit()
    conn.close()

def update_book_qty(book_id, qty_change):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE books SET quantity = quantity + ? WHERE id=?", (qty_change, book_id))
    conn.commit()
    conn.close()

def get_all_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

# --- Students ---
def add_student(name, email, contact):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, email, contact) VALUES (?, ?, ?)", (name, email, contact))
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    # Check if book is currently borrowed
    cur.execute("SELECT * FROM transactions WHERE book_id=? AND return_date IS NULL", (book_id,))
    if cur.fetchone():
        conn.close()
        return False  # Cannot delete
    cur.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    return True

def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    # Check if student has active borrow
    cur.execute("SELECT * FROM transactions WHERE student_id=? AND return_date IS NULL", (student_id,))
    if cur.fetchone():
        conn.close()
        return False
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    return True


# --- Borrow/Return ---
def borrow_book(student_id, book_id, borrow_date):
    conn = get_connection()
    cur = conn.cursor()
    # decrease book qty
    cur.execute("UPDATE books SET quantity = quantity - 1 WHERE id=? AND quantity > 0", (book_id,))
    if cur.rowcount == 0:
        conn.close()
        return False
    cur.execute("INSERT INTO transactions (student_id, book_id, borrow_date) VALUES (?, ?, ?)", 
                (student_id, book_id, borrow_date))
    conn.commit()
    conn.close()
    return True

def return_book(trans_id, return_date, fine):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE transactions SET return_date=?, fine=? WHERE id=?", (return_date, fine, trans_id))

    # restore book qty
    cur.execute("SELECT book_id FROM transactions WHERE id=?", (trans_id,))
    book_id = cur.fetchone()[0]
    cur.execute("UPDATE books SET quantity = quantity + 1 WHERE id=?", (book_id,))

    conn.commit()
    conn.close()

def get_active_borrows():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT t.id, s.name, b.title, t.borrow_date
                   FROM transactions t
                   JOIN students s ON t.student_id=s.id
                   JOIN books b ON t.book_id=b.id
                   WHERE t.return_date IS NULL""")
    rows = cur.fetchall()
    conn.close()
    return rows
