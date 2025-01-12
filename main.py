import sqlite3
from book_info import Book

# adds a new book to the database
def add_new_book():
    print("Please input the details of the book you would like to sell: ")
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    description = input("Enter a small description of the book: ")
    price = float(input("Enter the price of the book: "))
    condition = input("Enter the condition of the book: ")
    seller_name = input("Enter your name: ")

    #Creates an object of the Books class, and adds the user inputs as parameters
    new_book = Book(title, author, description, price, condition, seller_name)

    new_book.add_to_db()
    print(f"Your book, {title} by {author}, is now up for sale!")

# searches through the database of books being sold
def search_books(search_query):
    conn = sqlite3.connect('all_books.db')
    cursor = conn.cursor()

    # Search for books by title or author
    cursor.execute('''
        SELECT id, title, author, description, price, condition, seller_name
        FROM books
        WHERE title LIKE ? OR author LIKE ?
    ''', (f'%{search_query}%', f'%{search_query}%'))
    
    # fetches the results we want
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

# Simulate a chat between user and seller
def chat_with_seller(seller_name):
    print(f"\nStarting chat with {seller_name}. Type 'exit' to end the chat.\n")

    # The user starts a chat with the seller
    ## Not automated currently (The seller's reply is hard coded)
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            print("Chat ended.")
            break
        print(f"{seller_name}: Thank you for your message! I'll get back to you soon.")


print("Welcome to the ShelfSwap!")
while True:
    # users pick an option of what they want to do
    print("\nMenu:")
    print("1. Buy a book")
    print("2. Sell a Book")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # asks user for title or author if they want to buy book
    # then searches it through the databses
    if choice == "1":
        search_query = input("\nEnter the book title or author: ").strip()
        results = search_books(search_query)

        # If results are found, prints book details
        if results:
            print(f"\nFound {len(results)} book(s):\n")
            for book in results:
                book_id, title, author, description, price, condition, seller_name = book
                print(f"ID: {book_id}")
                print(f"Title: {title}")
                print(f"Author: {author}")
                print(f"Description: {description}")
                print(f"Price: ${price}")
                print(f"Condition: {condition}")
                print(f"Seller: {seller_name}\n")

            # Choose a book to chat with the seller
            book_id = input("Enter the ID of the book to contact the seller (or press Enter to go back): ").strip()

            # chats with the seller that the user chooses using their IDs
            if book_id:
                for book in results:
                    if str(book[0]) == book_id:
                        chat_with_seller(book[6])
                        break
                else:
                    print("Invalid book ID.")
        else:
            print("No books found matching your search.")
    # if user wants to sell a book, gets book details from user
    elif choice == "2":
        add_new_book()
    # exits app if user chooses
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

