from inventory import add_book, view_inventory

while True:
    print("\n1. Add Book\n2. View Inventory\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        add_book(title, author, price, stock)
        print("Book added.")
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        break

    elif choice == "4":
        keyword = input("Enter title keyword to search: ")
        results = search_books(keyword)
        if results:
            for book in results:
                print(f"{book['title']} by {book['author']}")
        else:
            print("No books found.")

print("\n1. Add Book\n2. View Inventory\n3. Exit\n4. Search")
