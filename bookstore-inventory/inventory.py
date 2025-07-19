import json
import os
from math import ceil

DATA_FILE = "books.json"

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(price, 2)
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

def load_inventory():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_inventory(inventory):
    with open(DATA_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

def add_book(title, author, price, stock):
    books = load_inventory()
    new_book = Book(title, author, price, stock)
    books.append(new_book.to_dict())
    save_inventory(books)

def view_inventory():
    books = load_inventory()
    for book in books:
        print(f"{book['title']} by {book['author']} - ${book['price']} (Stock: {book['stock']})")

def search_books(keyword):
    books = load_inventory()
    results = [book for book in books if keyword.lower() in book["title"].lower()]
    return results
