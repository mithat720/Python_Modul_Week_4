import json
import os


from functions import menu_add
from functions import menu_delete
from functions import main_menu

# Kitapları JSON'dan yükle
books_file = "books.json"
if os.path.exists(books_file):
    with open(books_file, "r", encoding="utf-8") as f:
        books = json.load(f)
else:
    books = []

def save_books():
    with open(books_file, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def book_add():
    print("Add a new book")
    book_barekod = int(input("Book barekod:   "))
    book_language = input("Book language:   ")
    book_price = float(input("Book price:   "))
    book_name = input("Book name:   ")
    book_house = input("Book house:   ")
    book_author = input("Book author:   ")
    book_new = { "Barkod": book_barekod, "Dil": book_language, "Fiyat" : book_price, "Kitap_Adi" : book_name, "Yayinevi" : book_house, "Yazar" : book_author}
    books.append(book_new)  
    print("------------Book added----------")
    books_print(books)
    save_books()

def books_print(books):
    print("Books in the library:")
    print("Barkod, Dil, Fiyat, Kitap_Adi, Yayinevi, Yazar")
    for i in books:
        print(f"Barkod: {i['Barkod']}, Dil: {i['Dil']}, Fiyat: {i['Fiyat']}, Kitap_Adi: {i['Kitap_Adi']}, Yayinevi: {i['Yayinevi']}, Yazar: {i['Yazar']}")  

def book_update():
    print("Update a book")
    book_id = int(input("Book id:   "))
    for i in books:
        if i["Barkod"] == book_id:
            book_barekod = int(input("Book barekod:   "))
            book_language = input("Book language:   ")
            book_price = float(input("Book price:   "))
            book_name = input("Book name:   ")
            book_house = input("Book house:   ")
            book_author = input("Book author:   ")
            i["Barkod"] = book_barekod
            i["Dil"] = book_language
            i["Fiyat"] = book_price
            i["Kitap_Adi"] = book_name
            i["Yayinevi"] = book_house
            i["Yazar"] = book_author
            print(f"Book with id {book_id} updated.")
        books_print(books)
        save_books()


def book_delete_id():
    print("Delete with barekod")
    book_id = int(input("Book barekod:   "))
    for i in books:
        if i["Barkod"] == book_id:
            books.remove(i)
            print(f"Book with barkod {book_id} deleted.")
            save_books()
            books_print(books)
            break
    else:
        print(f"No book found with barekod: {book_id}")

def book_delete_name():
    print("Delete with name")
    book_name = input("Book name:   ")
    for i in books:
        if i["Kitap_Adi"] == book_name:  # ✅ Doğru anahtar adı
            books.remove(i)
            print(f"Book with name {book_name} deleted.")
            save_books()  # ✅ Değişikliği dosyaya kaydet
            books_print(books)
            break
    else:
        print(f"No book found with name: {book_name}")


