#contacts project
import json
import os

# Define the name of the file to store contacts
CONTACTS_FILE = 'contacts.json' # The path to store contacts

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts,file)
    print("Contacts saved successfully!")
    print("Goodbye!")

def display_menu():
    print("\n--- Contacts Book Menu ---")
    print("1. View all contacts")
    print("2. Add a new contact")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Save and Exit")
    print("7. Exit without saving")
    print("-"*15) #decoration line

def view_all_contacts(contacts):
    if not contacts:
        print("No contacts found")
        return
    print("\n--- All Contacts ---")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-"*15) #decoration line

def add_contact(contacts):
    print("\n--- Add a New Contact")
    name = input("Enter Name:")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter Phone Number:")
    email = input("Enter Email Address:")
    contacts[name] = {"phone": phone, "email":email}
    print("Contact added successfully.")

def search_contact(contacts):
    print("\n--- Search for a Contact")
    name_to_find = input("Enter the name of the contact to search for: ")

    if name_to_find.lower() in contacts:
        details = contacts[name_to_find]
        print("\n--- Contact Found ---")
        print(f"Name: {name_to_find}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"No contact found with the name '{name_to_find}")

def update_contact(contacts):
    print("\n--- Update Contact")
    name_to_update = input("Enter the name of the contact to update: ")

    if name_to_update in contacts:
        print("Enter new details. Press Enter to keep the current details")

        current_details = contacts[name_to_update]
        print(f"Current phone: {current_details['phone']}")
        new_phone = input("New phone: ").strip() #strip() removes any whitespaces from the string

        print(f"Current email: {current_details['email']}")
        new_email = input("New email: ").strip()

        # Only update if the user provides a new value
        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email

        print(f"Contact '{name_to_update}' updated successfully")

    else:
        print(f"No contact found with the name '{name_to_update}'")

    
def delete_contact(contacts):
    print("\n--- Delete Contact")
    name_to_delete = input("Enter the name of the contact to delete: ")

    if name_to_delete in contacts:
        # The 'del' keyword removes the key-value pair from the contacts
        del contacts[name_to_delete]
        print(f"Contact '{name_to_delete}' has been deleted.")
    else:
        print(f"No contact found with name '{name_to_delete}'")
    

# -- The main program loop --

def main():
    '''The main function that run the contacts management program'''
    contacts = load_contacts()
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            view_all_contacts(contacts)
        elif choice == 2:
            add_contact(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            update_contact(contacts)
        elif choice == 5:
            delete_contact(contacts)
        elif choice == 6:
            save_contacts(contacts)
            break
        else:
            print("Invalid choice. Please try again.")

main()