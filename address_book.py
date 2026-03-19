# UC3 – Edit Existing Contact

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

    def edit_contact(self, first_name, last_name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                print("✅ Contact updated successfully!")
                return
        print("❌ Contact not found")

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)


# Example Usage
if __name__ == "__main__":
    book = AddressBook()

    p1 = Person("John", "Doe", "9876543210", "john@example.com", "Pune")
    book.add_contact(p1)

    book.display_contacts()

    print("\nUpdating Contact...\n")
    book.edit_contact("John", "Doe", phone="9999999999", address="Mumbai")

    book.display_contacts()