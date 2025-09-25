import sqlite3

DB_NAME = "library.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT,
                        available INTEGER DEFAULT 1)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        book_id INTEGER,
                        borrow_date TEXT,
                        return_date TEXT,
                        FOREIGN KEY(student_id) REFERENCES students(id),
                        FOREIGN KEY(book_id) REFERENCES books(id))''')

    conn.commit()
    conn.close()

def add_book(title, author):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

def add_student(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def get_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books
