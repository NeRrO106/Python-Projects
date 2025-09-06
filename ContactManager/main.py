import xml.etree.ElementTree as ET
import os
from operator import contains


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"{self.name} - {self.phone}, {self.email}."

class ContactManager:
    def __init__(self, filename = "contactmanager.xml"):
        self.contacts=[]
        self.filename = filename
        self.load_contacts()
    def load_contacts(self):
        if os.path.exists(self.filename):
            tree = ET.parse(self.filename)
            root = tree.getroot()
            self.contacts = [Contact(contact.find("name").text, contact.find("phone").text, contact.find("email").text) for contact in root.findall("contact")]
        else:
            print("No data file found, starting with an empty contact list.")
    def save_contacts(self):
        root = ET.Element("contacts")
        for contact in self.contacts:
            contact_elem = ET.Element("contact")
            name_elem = ET.SubElement(contact_elem, "name")
            name_elem.text = contact.name
            phone_elem = ET.SubElement(contact_elem, "phone")
            phone_elem.text = contact.phone
            email_elem = ET.SubElement(contact_elem, "email")
            email_elem.text = contact.email
            root.append(contact_elem)
        tree = ET.ElementTree(root)
        tree.write(self.filename)
        print("Contacts saved successfully.")
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact: {name} was added succesfully")
    def search_contact(self, name):
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                return contact
        return None
    def edit_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            print(f"Editing contact: {contact}")
            new_name = input(f"Enter new name (or press Enter to keep '{contact.name}'): ") or contact.name
            new_phone = input(f"Enter new phone (or press Enter to keep '{contact.phone}'): ") or contact.phone
            new_email = input(f"Enter new email (or press Enter to keep '{contact.email}'): ") or contact.email

            # Update contact details
            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            self.save_contacts()
            print(f"Contact {name} has been updated.")
        else:
            print(f"Contact with name '{name}' not found.")


def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            manager.add_contact(name, phone, email)
            manager.save_contacts()
        elif choice == 2:
            name = input("Enter the name of the contact to edit: ")
            manager.edit_contact(name)
        elif choice == 3:
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()