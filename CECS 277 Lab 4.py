
from Contacts import Contact

def read_file():
    contacts = []
    with open('addresses.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            contact = Contact(*data)
            contacts.append(contact)
    return sorted(contacts)

def write_file(contacts):
    with open('addresses.txt', 'w') as file:
        for contact in contacts:
            file.write(repr(contact) + '\n')

def get_menu_choice():
    print("\nRolodex Menu:")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")
    choice = input("> ")
    return choice

def modify_contact(contact):
    while True:
        print("\nModify Menu:")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Save")
        choice = input("> ")
        if choice == '1':
            contact.first_name = input("Enter new first name: ")
        elif choice == '2':
            contact.last_name = input("Enter new last name: ")
        elif choice == '3':
            contact.phone = input("Enter new phone number: ")
        elif choice == '4':
            contact.address = input("Enter new address: ")
        elif choice == '5':
            contact.city = input("Enter new city: ")
        elif choice == '6':
            contact.zip = input("Enter new zip code: ")
        elif choice == '7':
            break
        else:
            print("Invalid choice")

def main():
    contacts = read_file()
    while True:
        choice = get_menu_choice()
        if choice == '1':
            print(f"Number of contacts: {len(contacts)}")
            for idx, contact in enumerate(contacts, 1):
                print(f"{idx}. {contact}")

        elif choice == '2':
            first_name = input("Enter new contact: \nFirst name: ")
            last_name = input("Last name: ")
            phone = input("Phone #: ")
            address = input("Address: ")
            city = input("City: ")
            zip = input("Zip: ")
            new_contact = repr(Contact(first_name, last_name, phone, address, city, zip))
            contacts.append(new_contact)
            #contacts = sorted(contacts)

        elif choice == '3':
            search_type = input("Search:\n1. Search by last name:\n2. Search by zip:\n> ").lower()
            if search_type == '1':
                search_term = input("Enter last name: ")
                matches = [contact for contact in contacts if contact.last_name.lower() == search_term.lower()]
            elif search_type == '2':
                search_term = input("Enter zip code: ")
                matches = [contact for contact in contacts if contact.zip == search_term]
            else:
                print("Invalid input - should be an integer 1 or 2")
                continue
            if matches:
                for match in matches:
                    print(match)
            else:
                print("No matches found")

        elif choice == '4':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            match = None
            for contact in contacts:
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    match = contact
                    break
            if match:
                print(match)
                modify_contact(match)
                #contacts = sorted(match)    
            else:
                print("Contact not found")

        elif choice == '5':
            write_file(contacts)
            print("Saving File \nEnding Program...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
