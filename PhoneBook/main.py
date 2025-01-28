import os
import csv

CONTACTS_FILE = "contacts.txt" # the name of the file where contacts will be stored

class Contact:
    """Represents a single contact."""

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


def load_contacts():
    """Loads contacts from a file into a dictionary of Contact objects."""
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                  name, phone, email = row
                  contact = Contact(name, phone, email)
                  contacts[name] = contact
    return contacts


def save_contacts(contacts):
    """Saves contacts from the dictionary to the file."""
    with open(CONTACTS_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for contact in contacts.values():
            writer.writerow([contact.name, contact.phone, contact.email])


def add_contact(contacts):
    """Adds a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact with this name already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contact = Contact(name, phone, email)
    contacts[name] = contact
    print("Contact added successfully.")


def view_contacts(contacts):
    """Displays all contacts."""
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n--- Contact List ---")
    for contact in contacts.values():
        print(contact) # using the Contact class __str__ method

def search_contact(contacts):
    """Searches for a contact by name."""
    name = input("Enter name to search: ").strip()
    if name in contacts:
        contact = contacts[name]
        print(contact) # using the Contact class __str__ method
    else:
        print("Contact not found.")


def update_contact(contacts):
    """Updates existing contact information."""
    name = input("Enter name of contact to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email address: ").strip()
        contact = contacts[name]
        contact.phone = phone
        contact.email = email
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Deletes a contact from the dictionary."""
    name = input("Enter name of contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting. Contacts saved.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
