contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@mail.com",
        "city": "Pune"
    },
    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },
    "Zara": {
        "phones": ["9000011111"],
        "email": "zara@mail.com",
        "city": "Pune"
    }
}


# Check whether phone number is valid
def valid_phone(number):
    return number.isdigit() and len(number) == 10


# Check whether number belongs to another contact
def number_exists(number, current_name=None):
    for name, details in contacts.items():
        if name != current_name and number in details["phones"]:
            return True

    return False


# 1. Add Contact
def add_contact():
    name = input("Enter name: ")

    if name in contacts:
        print("Contact already exists!")
        return

    number = input("Enter phone number: ")

    if not valid_phone(number):
        print("Invalid number! Enter exactly 10 digits.")
        return

    if number_exists(number):
        print("This number already belongs to another contact!")
        return

    email = input("Enter email: ")
    city = input("Enter city: ")

    contacts[name] = {
        "phones": [number],
        "email": email,
        "city": city
    }

    print("Contact added successfully!")


# 2. Add Another Number
def add_number():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found!")
        return

    number = input("Enter another phone number: ")

    if not valid_phone(number):
        print("Invalid number! Enter exactly 10 digits.")
        return

    if number_exists(number):
        print("This number already belongs to another contact!")
        return

    if number in contacts[name]["phones"]:
        print("Number already exists in this contact!")
        return

    contacts[name]["phones"].append(number)

    print("Number added successfully!")


# 3. Update Email or City
def update_contact():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found!")
        return

    print("1. Update Email")
    print("2. Update City")

    choice = input("Enter choice: ")

    if choice == "1":
        contacts[name]["email"] = input("Enter new email: ")
        print("Email updated successfully!")

    elif choice == "2":
        contacts[name]["city"] = input("Enter new city: ")
        print("City updated successfully!")

    else:
        print("Invalid choice!")


# 4. Delete Contact
def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# 5. Search Contact
def search_contact():
    name_part = input("Enter name to search: ").lower()

    found = False

    for name, details in contacts.items():
        if name_part in name.lower():
            print(name, ":", details)
            found = True

    if not found:
        print("No matching contact found!")


# 6. Reports
def reports():

    # Reverse Lookup using Dictionary Comprehension
    reverse_lookup = {
        number: name
        for name, details in contacts.items()
        for number in details["phones"]
    }

    print("\nReverse Lookup Dictionary:")
    print(reverse_lookup)

    # Search by phone number
    number = input("\nEnter number for reverse lookup: ")

    if number in reverse_lookup:
        print("Number belongs to:", reverse_lookup[number])
    else:
        print("Number not found!")

    # Contacts grouped by city
    city_groups = {}

    for name, details in contacts.items():
        city = details["city"]
        city_groups.setdefault(city, []).append(name)

    print("\nContacts Grouped by City:")
    print(city_groups)

    # Contacts with more than one number
    multiple_numbers = {
        name: details["phones"]
        for name, details in contacts.items()
        if len(details["phones"]) > 1
    }

    print("\nContacts with More Than One Number:")
    print(multiple_numbers)

    # Print whole directory alphabetically
    print("\nDirectory in Alphabetical Order:")

    for name in sorted(contacts):
        details = contacts[name]

        print("\nName:", name)
        print("Phone Numbers:", details["phones"])
        print("Email:", details["email"])
        print("City:", details["city"])


# Main Menu
while True:
    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        add_number()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        search_contact()

    elif choice == "6":
        reports()

    elif choice == "7":
        print("Exiting Phone Directory...")
        break

    else:
        print("Invalid choice!")