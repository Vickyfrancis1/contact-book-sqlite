import sqlite3
from contacts_lib import find_contact, add_contact, delete_contact

conn = sqlite3.connect("contacts.db")

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all")
    print("4. Delete contact")
    print("5. Quit")
    choice = input("Choose: ").strip()
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        if add_contact(conn, name, phone):
            print("Saved")
        else:
            print("That contact already exists.")
    elif choice == "2":
        row = find_contact(conn, input("Search for: "))
        if row is None:
            print("Not found.")
        else:
            print(f"{row[0]}: {row[1]}")
    elif choice == "3":
        rows = conn.execute("SELECT name, phone FROM contacts ORDER BY name").fetchall()
        if not rows:
            print("No contacts yet.")
        for name, phone in rows:
            print(f"{name}: {phone}")
    elif choice == "4":
        if delete_contact(conn, input("Delete who? ")):
            print("Deleted.")
        else:
            print("Not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose 1 to 5.")
            
conn.close()