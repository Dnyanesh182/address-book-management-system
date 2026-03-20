# UC6 – Add Multiple Address Books

class Person:
    def __init__(self, first_name, last_name, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | {self.address}"


class AddressBookManager:
    def __init__(self):
        self.address_books = {}  # dictionary of address books

    def add_address_book(self, name):
        if name not in self.address_books:
            self.address_books[name] = []
            print(f"✅ Address book '{name}' created")
        else:
            print("❌ Address book already exists")

    def add_contact(self, book_name, person):
        if book_name not in self.address_books:
            print("❌ Address book not found")
            return

        # Duplicate check within that book
        for contact in self.address_books[book_name]:
            if (
                (contact.first_name == person.first_name and contact.last_name == person.last_name) or
                contact.phone == person.phone or
                contact.email == person.email
            ):
                print("❌ Duplicate contact detected!")
                return

        self.address_books[book_name].append(person)
        print(f"✅ Contact added to '{book_name}'")

    def display_all(self):
        for book, contacts in self.address_books.items():
            print(f"\n📘 {book.upper()}:")
            for contact in contacts:
                print(contact)


# Example Usage
if __name__ == "__main__":
    manager = AddressBookManager()

    manager.add_address_book("family")
    manager.add_address_book("friends")
    manager.add_address_book("office")

    p1 = Person("John", "Doe", "9876543210", "john@example.com", "Pune")
    p2 = Person("Jane", "Smith", "9123456780", "jane@example.com", "Mumbai")

    manager.add_contact("family", p1)
    manager.add_contact("friends", p2)

    manager.display_all()