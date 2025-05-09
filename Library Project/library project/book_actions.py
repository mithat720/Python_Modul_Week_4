# def book_actions_menu():
#     print("1. Borrow Book")
#     print("2. Return Book")
#     print("3. Reserve Book")
#     print("4. Cancel Reservation")
#     print("5. List Borrowed Books")
#     print("6. List Reserved Books")
#     print("7. Exit")
#     return int(input("Select an action: "))


import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def borrow_book():
    books = load_books()
    barcode = input("Enter book barcode to borrow: ")
    member_name = input("Enter member name: ")

    for book in books:
        if str(book["Barkod"]) == barcode:
            if book.get("status") == "borrowed":
                print("Book is already borrowed.")
                return
            book["status"] = "borrowed"
            book["borrowed_by"] = member_name
            print(f"Book '{book['Kitap_Adi']}' borrowed by {member_name}.")
            save_books(books)
            return

    print("Book not found.")

def return_book():
    books = load_books()
    barcode = input("Enter book barcode to return: ")

    for book in books:
        if str(book["Barkod"]) == barcode and book.get("status") == "borrowed":
            book["status"] = "available"
            book.pop("borrowed_by", None)
            print(f"Book '{book['Kitap_Adi']}' has been returned.")
            save_books(books)
            return

    print("Book not found or not borrowed.")

def reserve_book():
    books = load_books()
    barcode = input("Enter book barcode to reserve: ")
    member_name = input("Enter member name: ")

    for book in books:
        if str(book["Barkod"]) == barcode:
            if book.get("status") == "available":
                book["status"] = "reserved"
                book["reserved_by"] = member_name
                print(f"Book '{book['Kitap_Adi']}' reserved by {member_name}.")
                save_books(books)
                return
            else:
                print(f"Book is not available. Current status: {book.get('status')}")
                return

    print("Book not found.")

def cancel_reservation():
    books = load_books()
    barcode = input("Enter book barcode to cancel reservation: ")
    member_name = input("Enter member name: ")

    for book in books:
        if (str(book["Barkod"]) == barcode and
            book.get("status") == "reserved" and
            book.get("reserved_by") == member_name):
            book["status"] = "available"
            book.pop("reserved_by", None)
            print(f"Reservation for '{book['Kitap_Adi']}' canceled.")
            save_books(books)
            return

    print("Reservation not found.")

def list_borrowed_books():
    books = load_books()
    borrowed = [book for book in books if book.get("status") == "borrowed"]
    if borrowed:
        print("Borrowed Books:")
        for b in borrowed:
            print(f"{b['Kitap_Adi']} - Borrowed by: {b['borrowed_by']}")
    else:
        print("No books are currently borrowed.")

def list_reserved_books():
    books = load_books()
    reserved = [book for book in books if book.get("status") == "reserved"]
    if reserved:
        print("Reserved Books:")
        for b in reserved:
            print(f"{b['Kitap_Adi']} - Reserved by: {b['reserved_by']}")
    else:
        print("No books are currently reserved.")

def show_all_books():
    books = load_books()
    print("All Book Records:")
    for book in books:
        print(book)

def book_actions_menu():
    print("\nBook Actions Menu:")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Reserve Book")
    print("4. Cancel Reservation")
    print("5. List Borrowed Books")
    print("6. List Reserved Books")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    print("7. List All Books")
    print("8. Exit")
    return int(input("Select an action: "))
=======
=======
>>>>>>> Stashed changes
    print("7. Show All Book Records")
    print("0. Exit")
    try:
        return int(input("Choose an option: "))
    except:
        print("Invalid input.")
<<<<<<< Updated upstream
        return 0
>>>>>>> Stashed changes
=======
        return 0
>>>>>>> Stashed changes
