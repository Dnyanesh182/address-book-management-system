# UC7 – Search Person (Advanced)

class Person:
    def __init__(self, first_name, last_name, phone, email, address, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} | "
            f"{self.phone} | {self.email} | "
            f"{self.address}, {self.city}, {self.state}"
        )


class AddressBookManager:
    def __init__(self):
        self.address_books = {}

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

        for contact in self.address_books[book_name]:
            if (
                (contact.first_name == person.first_name and contact.last_name == person.last_name)
                or contact.phone == person.phone
                or contact.email == person.email
            ):
                print("❌ Duplicate contact detected!")
                return

        self.address_books[book_name].append(person)
        print(f"✅ Contact added to '{book_name}'")

    def search_person(self, name=None, city=None, state=None):
        results = []

        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                full_name = f"{contact.first_name} {contact.last_name}".lower()

                if (
                    (name and name.lower() in full_name) or
                    (city and city.lower() == contact.city.lower()) or
                    (state and state.lower() == contact.state.lower())
                ):
                    results.append((book_name, contact))

        return results


# Example Usage
if __name__ == "__main__":
    manager = AddressBookManager()

    manager.add_address_book("family")
    manager.add_address_book("friends")

    p1 = Person("John", "Doe", "9876543210", "john@example.com", "MG Road", "Pune", "Maharashtra")
    p2 = Person("Jane", "Smith", "9123456780", "jane@example.com", "Link Road", "Mumbai", "Maharashtra")
    p3 = Person("Jack", "Taylor", "9988776655", "jack@example.com", "FC Road", "Pune", "Maharashtra")

    manager.add_contact("family", p1)
    manager.add_contact("friends", p2)
    manager.add_contact("friends", p3)

    matches = manager.search_person(city="Pune")

    print("\nSearch Results:")
    for book_name, person in matches:
        print(f"[{book_name}] {person}")