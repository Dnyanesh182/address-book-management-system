# UC8 – Sort Contacts (Multi-Criteria)

class Person:
    def __init__(self, first_name, last_name, phone, email, address, city, state, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return (
            f"{self.full_name()} | {self.phone} | {self.email} | "
            f"{self.address}, {self.city}, {self.state} - {self.zip_code}"
        )


class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name not in self.address_books:
            self.address_books[name] = []
            print(f"✅ Address book '{name}' created")

    def add_contact(self, book_name, person):
        if book_name not in self.address_books:
            print("❌ Address book not found")
            return

        self.address_books[book_name].append(person)
        print(f"✅ Contact added to '{book_name}'")

    def get_all_contacts(self):
        contacts = []
        for book_name, persons in self.address_books.items():
            for person in persons:
                contacts.append((book_name, person))
        return contacts

    def sort_contacts(self, sort_by):
        contacts = self.get_all_contacts()

        if sort_by == "name":
            return sorted(contacts, key=lambda item: item[1].full_name().lower())
        if sort_by == "city":
            return sorted(contacts, key=lambda item: item[1].city.lower())
        if sort_by == "zip":
            return sorted(contacts, key=lambda item: item[1].zip_code)

        print("❌ Invalid sort criteria")
        return []


# Example Usage
if __name__ == "__main__":
    manager = AddressBookManager()

    manager.add_address_book("family")
    manager.add_address_book("friends")

    p1 = Person("John", "Doe", "9876543210", "john@example.com", "MG Road", "Pune", "Maharashtra", "411001")
    p2 = Person("Jane", "Smith", "9123456780", "jane@example.com", "Link Road", "Mumbai", "Maharashtra", "400001")
    p3 = Person("Amit", "Patil", "9988776655", "amit@example.com", "FC Road", "Pune", "Maharashtra", "411004")

    manager.add_contact("family", p1)
    manager.add_contact("friends", p2)
    manager.add_contact("friends", p3)

    sorted_contacts = manager.sort_contacts("name")

    print("\nSorted Contacts:")
    for book_name, person in sorted_contacts:
        print(f"[{book_name}] {person}")