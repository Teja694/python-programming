import os
import pickle
from datetime import datetime

# Define global variables
books = []
filename = "books.dat"

# Define classes
class Book:
    def __init__(self, id, category, name, author, quantity, price, rackno):
        self.id = id
        self.category = category
        self.name = name
        self.author = author
        self.quantity = quantity
        self.price = price
        self.rackno = rackno

    def __str__(self):
        return f"{self.category:<10} {self.id:<5} {self.name:<20} {self.author:<15} {self.quantity:<5} {self.price:<8.2f} {self.rackno:<5}"

# Functions
def load_books():
    global books
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            books = pickle.load(f)

def save_books():
    with open(filename, "wb") as f:
        pickle.dump(books, f)

def view_books():
    os.system("cls" if os.name == "nt" else "clear")
    print("*********************************Book List*****************************")
    print(" CATEGORY     ID    BOOK NAME           AUTHOR         QTY    PRICE   RackNo")
    for book in books:
        print(book)
    print(f"Total Books = {sum(book.quantity for book in books)}")

def edit_book():
    load_books()
    book_id = int(input("Enter Book ID to be edited: "))
    for book in books:
        if book.id == book_id:
            print(f"The book is available")
            print(f"The Book ID: {book.id}")
            book.name = input("Enter new name: ")
            book.author = input("Enter new Author: ")
            book.quantity = int(input("Enter new quantity: "))
            book.price = float(input("Enter new price: "))
            book.rackno = int(input("Enter new rackno: "))
            print("The record is modified")
            save_books()
            return
    print("No record found")

def delete_book():
    load_books()
    book_id = int(input("Enter Book ID to be removed: "))
    global books
    books = [book for book in books if book.id != book_id]
    save_books()
    print("The book is removed from the list")

def issue_book():
    book_id = int(input("Enter Book ID to issue: "))
    for book in books:
        if book.id == book_id:
            print(f"The Book has been issued: {book.name}")
            # Here you would handle issuing logic, e.g., setting due dates, etc.
            return
    print("No record found")

def main_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Library Management System")
        print("1. View Books")
        print("2. Edit Book")
        print("3. Delete Book")
        print("4. Issue Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_books()
        elif choice == '2':
            edit_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Load initial data
load_books()
# Start the main menu
main_menu()

