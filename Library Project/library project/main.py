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
        print("Exit")
        break
