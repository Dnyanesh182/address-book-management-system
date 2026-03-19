# UC5 – Prevent Duplicate Entries

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

    def is_duplicate(self, person):
        for contact in self.contacts:
            if (
                (contact.first_name == person.first_name and contact.last_name == person.last_name) or
                contact.phone == person.phone or
                contact.email == person.email
            ):
                return True
        return False

    def add_contact(self, person):
        if self.is_duplicate(person):
            print("❌ Duplicate contact detected! Not added.")
            return
        self.contacts.append(person)
        print("✅ Contact added successfully!")

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)


# Example Usage
if __name__ == "__main__":
    book = AddressBook()

    p1 = Person("John", "Doe", "9876543210", "john@example.com", "Pune")
    p2 = Person("John", "Doe", "9876543210", "john@example.com", "Mumbai")  # duplicate

    book.add_contact(p1)
    book.add_contact(p2)  # should be rejected

    book.display_contacts()