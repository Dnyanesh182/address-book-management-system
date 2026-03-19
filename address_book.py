# UC4 – Delete Contact

class Person:
    def __init__(self, first_name, last_name, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | {self.address}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person):
        self.contacts.append(person)

    def delete_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                print("✅ Contact deleted successfully!")
                return
        print("❌ Contact not found")

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)


# Example Usage
if __name__ == "__main__":
    book = AddressBook()

    p1 = Person("John", "Doe", "9876543210", "john@example.com", "Pune")
    p2 = Person("Jane", "Smith", "9123456780", "jane@example.com", "Mumbai")

    book.add_contact(p1)
    book.add_contact(p2)

    print("Before Deletion:")
    book.display_contacts()

    print("\nDeleting Contact...\n")
    book.delete_contact("John", "Doe")

    print("\nAfter Deletion:")
    book.display_contacts()