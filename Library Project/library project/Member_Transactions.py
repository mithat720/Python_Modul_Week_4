import json
import os

members_file = "members.json"
if os.path.exists(members_file):
    with open(members_file, "r", encoding="utf-8") as f:
        members = json.load(f)
else:
    members = []

def save_members():
    with open(members_file, "w", encoding="utf-8") as f:
        json.dump(members, f, ensure_ascii=False, indent=4)

def members_print(members):
    for i in members:
        print(f"Id: {i['id']}, Name: {i['name']}, Tel: {i['tel']}, Time: {i['date']}, Adress: {i['adress']}")  
         
def member_add(x):
    print(f"{x} add menu")
    print("---------------------------------------")
    member_id = int(input(f"{x} id:   "))
    member_name = (input(f"{x} name:   "))
    member_tel = int(input(f"{x} tel:   "))
    member_time = int(input(f"{x} time:   "))
    member_adress = (input(f"{x} address:   "))
    print("---------------------------------------")
    member_new= { "id": member_id, 
            "name": member_name, 
            "tel" : member_tel, 
            "date" : member_time, 
            "adress" : member_adress}
    members.append(member_new)
    members_print(members)
    save_members()
    print("------------Member added----------")


