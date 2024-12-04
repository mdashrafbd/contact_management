from contact_manager import add_contact, view_contacts, remove_contact, search_contacts
from file_manager import load_contacts, save_contacts
from utils import validate_name, validate_phone_number

def display_menu():
    print("\n--- Contact Book Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

def main():
    contacts = load_contacts()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            if not validate_name(name):
                print("Invalid name. Please enter a valid string.")
                continue
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            if not validate_phone_number(phone, contacts):
                print("Invalid or duplicate phone number. Please enter a valid number.")
                continue
            address = input("Enter address: ")
            add_contact(contacts, name, email, phone, address)
            save_contacts(contacts)
        
        elif choice == '2':
            view_contacts(contacts)
        
        elif choice == '3':
            phone = input("Enter the phone number of the contact to remove: ")
            if remove_contact(contacts, phone):
                save_contacts(contacts)
            else:
                print("No contact found with that phone number.")
        
        elif choice == '4':
            query = input("Enter the name, email, or phone number to search: ")
            search_contacts(contacts, query)
        
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
