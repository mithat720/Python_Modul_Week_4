# For example, adding a book, deleting a book,
#  adding a member, giving a book to a member, 
# and member control will be done here
#  and the main function will be in the main.py file
# Libraary Project
# 1. Book class,
# 2. Member class,
# 3. Library class,
# 4. Book class will have a title, author, and ISBN number
# 5. Member class will have a name, member ID, and a list of borrowed books
# 6. Library class will have a list of books and a list of members
# 7. Library class will have methods to add a book, delete a book, add a member, give a book to a member, and return a book
# 8. Library class will have a method to display all books and members

def main_menu():
    print("--------------Main Menu -------------")
    print("| 1. Membership                     |")
    print("| 2. Bookshelf                      |")
    print("| 3. Book Actions                   |")
    print("| 4. Web application                |")
    print("| 5. Kioks                          |")
    print("| 6. Exit                           |")
    print("| --------------------------------- |")
    return int(input(" Chooice a menu: "))

def web_ablications():
    print("--------------Web Application Menu -------------")
    print("| 1. Web application                 |")
    print("| 2. Web application                 |")
    print("| 3. Web application                 |")
    print("| 4. Web application                 |")
    print("| 5. Web application                 |")
    print("| 6. Exit                            |")
    print("| --------------------------------- |")
    return int(input(" Chooice a menu: "))

def kioks():
    print("--------------Kioks Menu -------------")
    print("| 1. Kioks                           |")
    print("| 2. Kioks                           |")
    print("| 3. Kioks                           |")
    print("| 4. Kioks                           |")
    print("| 5. Kioks                           |")
    print("| 6. Exit                            |")
    print("| --------------------------------- |")
    return int(input(" Chooice a menu: "))
    
def menu(x):
    print("-------------------------------------")
    print(f"| 1. {x} Add                     |")
    print(f"| 2. {x} Delete                  |")
    print(f"| 3. {x} Update                  |")
    print(f"| 4. {x} List                    |")
    print(f"| 5.     Exit                    |")   
    print("--------------------------------------")
    return int(input("Choice: "))
   
def menu_add(x):
    print(f"{x} add menu")
    print("---------------------------------------")
    id = int(input(f"{x} id:   "))
    name = (input(f"{x} name:   "))
    tel = int(input(f"{x} tel:   "))
    time = int(input(f"{x} time:   "))
    print("---------------------------------------")
    return id, name, tel, time
    
def menu_delete(x):
    print(f"{x} delete menu")
    print("---------------------------------------")
    print(f"| 1. Delete with {x} id:             |")
    print(f"| 2. Delete with {x} name:           |")
    print(f"| 3. Delete all {x} details:         |")
    print(f"| 4. Exit                            |")
    print("---------------------------------------")
    return int(input("| Choise:    |"))
   
def menu_delete_id(x):
    print(f"{x} delete menu with id")
    print("---------------------------------------")
    return int(input(f" {x} Id, want to delete |"))

def menu_delete_name(x):
    print(f"{x} delete menu with name")
    print("---------------------------------------")
    return input(f" {x} Name, want to delete |")

def menu_update(x):
    print(f"{x} update menu")
    print("---------------------------------------")
    print(f"| 1. Update with {x} id:             |")
    print(f"| 2. Update with {x} name:           |")
    print(f"| 3. Delete all {x} details:         |")
    print(f"| 4. Exit:                           |")
    print("---------------------------------------")
    return int(input("| Choise:             --"))

def print_librarytech_logo():
    print("""
   _      _ _                      _______        _     
  | |    (_) |                    |__   __|      | |    
  | |     _| |__   ___  _ __ ___     | | ___  ___| |__  
  | |    | | '_ \ / _ \| '_ ` _ \    | |/ _ \/ __| '_ \ 
  | |____| | | | | (_) | | | | | |   | |  __/\__ \ | | |
  |______|_|_| |_|\___/|_| |_| |_|   |_|\___||___/_| |_|

                L I B R A R Y T E C H
    """)

print_librarytech_logo()



def menu_list(x):
    print(f"{x} list menu")
    print("---------------------------------------")
    print(f"| 1. List with {x} id:               |")
    print(f"| 2. List with {x} name:             |")
    print(f"| 3. List all {x} details:           |")
    print(f"| 4. Exit:                           |")
    select_menu_list = int(input("| Choise:             --"))

    if select_menu_list == 1:
        select_id = int(input(f"{x} id:       --"))
        if {x} == "Book":
            from Kitap_transactions import book
            for i in book():
                print("liste:", book)
        elif {x} == "Member":
            from Member_Transactions import member
            for i in member():
                print("liste:", member)
                break

    elif select_menu_list == 2:
        select_name = input(f"{x} name:       --")
        if {x} == "Book":
            from Kitap_transactions import book
            for i in book():
                print(select_name[i])
        elif {x} == "Member":
            from Member_Transactions import member
            for i in member():
                print(select_name[i])
                break

    elif select_menu_list == 3:
        if {x} == "Book":
            from Kitap_transactions import book
            for i in book():
                print("liste:", book)
        elif {x} == "Member":
            from Member_Transactions import member
            for i in member():
                print(i)
                break

        


    
