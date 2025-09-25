class Book:
    def __init__(self, title, author, quantity=1):
        self.title = title
        self.author = author
        self.quantity = quantity

class Student:
    def __init__(self, name, email, contact):
        self.name = name
        self.email = email
        self.contact = contact

class Transaction:
    def __init__(self, student_id, book_id, borrow_date, return_date=None, fine=0):
        self.student_id = student_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.fine = fine
