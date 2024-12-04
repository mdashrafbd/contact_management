def add_contact(contacts, name, email, phone, address):
    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

def remove_contact(contacts, phone):
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print(f"Contact with phone number {phone} has been removed.")
            return True
    return False

def search_contacts(contacts, query):
    results = [contact for contact in contacts if query.lower() in str(contact.values()).lower()]
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print(f"No contacts found for '{query}'")
