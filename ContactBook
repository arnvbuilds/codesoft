contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added.")

def view_contacts():
    print("\nAll Contacts:")
    for name, details in contacts.items():
        print(f"{name}: {details['phone']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Name: {name}")
        for k, v in contacts[name].items():
            print(f"{k.title()}: {v}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        print("Leave field empty to keep unchanged.")
        phone = input("New phone: ") or contacts[name]['phone']
        email = input("New email: ") or contacts[name]['email']
        address = input("New address: ") or contacts[name]['address']
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    option = input("Choose an option: ")

    if option == '1':
        add_contact()
    elif option == '2':
        view_contacts()
    elif option == '3':
        search_contact()
    elif option == '4':
        update_contact()
    elif option == '5':
        delete_contact()
    elif option == '6':
        break
    else:
        print("Invalid option.")
