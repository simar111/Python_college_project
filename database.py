import sqlite3

# Connect to database (creates library.db if not exists)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
""")

# Create Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    available INTEGER DEFAULT 1
);
""")

# Create Borrowed Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS borrowed_books (
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    book_id INTEGER,
    borrow_date TEXT,
    return_date TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);
""")

print("✅ Database and tables created successfully!")

conn.commit()
conn.close()
