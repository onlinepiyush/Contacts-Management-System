# Contacts Management System

import os
import csv

# Define the name of the file to store contacts
CONTACTS_FILE = 'contacts.csv'  # The path to store contacts

def load_contacts():
    """Load contacts from CSV file into a dictionary."""
    contacts = {}
    if not os.path.exists(CONTACTS_FILE):
        return contacts

    with open(CONTACTS_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:  # name, phone, email
                name, phone, email = row
                contacts[name] = {'phone': phone, 'email': email}
    return contacts


def save_contacts(contacts):
    """Save contacts to CSV file."""
    with open(CONTACTS_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for name, details in contacts.items():
            writer.writerow([name, details['phone'], details['email']])
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
    print("-" * 15)


def view_all_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- All Contacts ---")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 15)


def add_contact(contacts):
    print("\n--- Add a New Contact ---")
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")


def search_contact(contacts):
    print("\n--- Search for a Contact ---")
    name_to_find = input("Enter the name of the contact to search for: ").strip()
    if name_to_find in contacts:
        details = contacts[name_to_find]
        print("\n--- Contact Found ---")
        print(f"Name: {name_to_find}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"No contact found with the name '{name_to_find}'.")


def update_contact(contacts):
    print("\n--- Update Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").strip()

    if name_to_update in contacts:
        print("Enter new details. Press Enter to keep the current details.")

        current_details = contacts[name_to_update]
        print(f"Current phone: {current_details['phone']}")
        new_phone = input("New phone: ").strip()
        print(f"Current email: {current_details['email']}")
        new_email = input("New email: ").strip()

        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email

        print(f"Contact '{name_to_update}' updated successfully.")
    else:
        print(f"No contact found with the name '{name_to_update}'.")


def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").strip()

    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"Contact '{name_to_delete}' has been deleted.")
    else:
        print(f"No contact found with the name '{name_to_delete}'.")


# -- The main program loop --

def main():
    """Main function to run the contact manager."""
    contacts = load_contacts()
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

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
        elif choice == 7:
            print("Goodbye (without saving)!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
