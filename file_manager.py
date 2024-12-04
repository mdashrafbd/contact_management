import os

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, email, phone, address = line.strip().split(',')
                contacts.append({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address
                })
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")
