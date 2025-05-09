import json
import os
from functions import *
from functions import menu_add
from functions import menu_update
from functions import menu_delete
from functions import menu_list
from functions import menu
from Kitap_transactions import book_add
#from Kitap_transactions import book_delete
from Member_Transactions import member_add
from Member_Transactions import members
from Kitap_transactions import books
from Member_Transactions import members_print
from Kitap_transactions import books_print
from Kitap_transactions import book_delete_id
from Kitap_transactions import book_delete_name
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from book_actions import book_actions_menu
from Kitap_transactions import book_list
=======
=======
>>>>>>> Stashed changes
#from book_actions import book_actions_menu
from book_actions import (
    book_actions_menu,
    borrow_book,
    return_book,
    reserve_book,
    cancel_reservation,
    list_borrowed_books,
    list_reserved_books,
    show_all_books
)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

# bu degisikligi simdi yaptim !!!!!!!!!!!!!!!!!!.....,,,,,
books_file = "books.json"
if os.path.exists(books_file):
    with open(books_file, "r", encoding="utf-8") as f:
        books = json.load(f)
else:
    books = []
# Kitapları JSON dosyasına kaydetme fonksiyonu
def save_books():
    with open(books_file, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


print("---------------------------------------")
print("--------Welkom to Library--------------")
select = main_menu()
print("-------------Main Menu----------------")

while True:
    if select ==1:
        
        print("-----------Membership Menu----------")

        while True:
            select_member = menu("Member")

            if select_member ==1:
                member_add("Member")
                print("------------Member added----------")
                
            elif select_member ==2:

                print("Delete member")
                print("Delete with id or name")
                menu_delete_selecet = menu_delete("Member")
                if menu_delete_selecet == 1:
                    print("Delete with id")
                    member_id = int(input("Member id:   "))
                    for i in members:
                        if i["id"] == member_id:
                            members.remove(i)
                            print(f"Member with id {member_id} deleted.")
                            members_print(members)

                elif menu_delete_selecet == 2:
                    print("Delete with name")
                    member_name = input("Member name:   ")
                    for i in members:
                        if i["name"] == member_name:
                            members.remove(i)
                            print(f"Member with name {member_name} deleted.")
                            members_print(members)
                elif menu_delete_selecet == 3:
                    print("Delete all members")
                    members.clear()
                    print("All members deleted.")
                    members_print(members)
                else:
                    print("Exit")                    
                    break               

            elif select_member == 3:
                print("Update member")
                menu_update("Member")
                members_print(members)
                
            elif select_member == 4:
                menu_list("Member")
                members_print(members)
                
            else:
                print("Exit")
                break
            
    elif select ==2:
        print("--------------Bookshelf menu-------")
        select_book = menu("Book")
       
        while True:
            if select_book ==1:
                book_add()
                print("------------Book added----------")
                
            elif select_book ==2:
                menu_delete_selecet = menu_delete("Book")
                if menu_delete_selecet == 1:
                    book_delete_id()
                    
                elif menu_delete_selecet == 2:
                    book_delete_name()
                    
                    
            elif select_book == 3:
                menu_update("Book")
                books_print(books)
                

            elif select_book == 4:
                menu_list("Book")
                books_print(books)
                break
                
            elif select_book == 5:
                print("Exit") 
                books_print(books)
                break


    elif select ==3:
        print("-----------Book actions menu--------")
        while True:
            select_book_actions = book_actions_menu()

            if select_book_actions == 1:
                borrow_book()
                # Add your borrow book logic here
                
            elif select_book_actions == 2:
                return_book()

            elif select_book_actions == 3:
                reserve_book()

            elif select_book_actions == 4:
                cancel_reservation()

            elif select_book_actions == 5:
                list_borrowed_books()

            elif select_book_actions == 6:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
                print("List Reserved Books")
                # Add your list reserved books logic here
            elif select_book_actions == 7:
                print(books)
                #book_list()
                print("List Reserved Books")
                # Add your list reserved books logic here
                
=======
=======
>>>>>>> Stashed changes
                list_reserved_books()

            elif select_book_actions == 7:
                show_all_books()

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            else:
                print("Exit")
                break
