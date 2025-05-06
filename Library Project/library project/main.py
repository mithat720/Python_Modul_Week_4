from functions import main_menu
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


print("---------------------------------------")
print("--------Welkom to Library--------------")
select = main_menu()
print("-------------Main Menu----------------")

while True:
    if select ==1:
        print("-----------Membership Menu----------")
        select_member = menu("Member")

        while True:
            if select_member ==1:
                member_add("Member")
                print("------------Member added----------")
                break

            elif select_member ==2:
                menu_delete("Member")
                if menu_delete("Member") == 1:
                    print("Delete with id")
                    member_id = int(input("Member id:   "))
                    for i in members:
                        if i["id"] == member_id:
                            members.remove(i)
                            print(f"Member with id {member_id} deleted.")
                            members_print(members)

                elif menu_delete("Member") == 2:
                    print("Delete with name")
                    member_name = input("Member name:   ")
                    for i in members:
                        if i["name"] == member_name:
                            members.remove(i)
                            print(f"Member with name {member_name} deleted.")
                            members_print(members)

                elif menu_delete("Member") == 3:
                    print("Delete all members")
                    members.clear()
                    print("All members deleted.")
                    members_print(members)

                elif menu_delete("Member") == 4:
                    print("Exit")                    
                    break

                else:
                    print("Invalid choice.")
                    break

            elif select_member == 3:
                print("Update member")
                menu_update("Member")
                members_print(members)
                break

            elif select_member == 4:
                menu_list("Member")
                members_print(members)
                break

            elif select_member == 5:
                print("Exit")
                break
            break

    elif select ==2:
        print("--------------Bookshelf menu-------")
        select_book = menu("Book")
       
        while True:
            if select_book ==1:
                book_add()
                print("------------Book added----------")
                break
            elif select_book ==2:
                #book_delete("Book")
                if menu_delete("Book") == 1:
                    book_delete_id()
                    break
                elif menu_delete("Book") == 2:
                    book_delete_name()
                    break
                    
            elif select_book == 3:
                menu_update("Book")
                books_print(books)
                break

            elif select_book == 4:
                menu_list("Book")
                books_print(books)
                break
                
            elif select_book == 5:
                print("Exit") 
                books_print(books)
                break


    elif select ==3:
        print("Exit")
        break
