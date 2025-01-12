import sqlite3

class Book:
    def __init__(self, title, author, description, price, condition, seller_name):
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.condition = condition
        self.seller_name = seller_name

    def add_to_db(self):
        # Connects to the books_app database
        conn = sqlite3.connect('all_books.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, description TEXT, price FLOAT, condition TEXT, seller_name TEXT)''')

        # Inserts the details of the book into the database
        cursor.execute('''
            INSERT INTO books (title, author, description, price, condition, seller_name)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.title, self.author, self.description, self.price, self.condition, self.seller_name))

        conn.commit()
        conn.close()

    
        
        