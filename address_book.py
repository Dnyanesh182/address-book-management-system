# UC9 – File I/O + JSON Persistence

import json
import csv


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

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["phone"],
            data["email"],
            data["address"],
            data["city"],
            data["state"],
            data["zip_code"]
        )

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | "
            f"{self.address}, {self.city}, {self.state} - {self.zip_code}"
        )


class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name not in self.address_books:
            self.address_books[name] = []

    def add_contact(self, book_name, person):
        if book_name not in self.address_books:
            self.address_books[book_name] = []
        self.address_books[book_name].append(person)

    def save_to_json(self, filename):
        data = {
            book_name: [person.to_dict() for person in contacts]
            for book_name, contacts in self.address_books.items()
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("✅ Address book saved to JSON")

    def load_from_json(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        self.address_books = {
            book_name: [Person.from_dict(person_data) for person_data in contacts]
            for book_name, contacts in data.items()
        }
        print("✅ Address book loaded from JSON")

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["book_name", "first_name", "last_name", "phone", "email", "address", "city", "state", "zip_code"]
            )
            for book_name, contacts in self.address_books.items():
                for person in contacts:
                    writer.writerow([
                        book_name,
                        person.first_name,
                        person.last_name,
                        person.phone,
                        person.email,
                        person.address,
                        person.city,
                        person.state,
                        person.zip_code
                    ])
        print("✅ Address book saved to CSV")

    def load_from_csv(self, filename):
        self.address_books = {}
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                book_name = row["book_name"]
                person = Person(
                    row["first_name"],
                    row["last_name"],
                    row["phone"],
                    row["email"],
                    row["address"],
                    row["city"],
                    row["state"],
                    row["zip_code"]
                )
                if book_name not in self.address_books:
                    self.address_books[book_name] = []
                self.address_books[book_name].append(person)
        print("✅ Address book loaded from CSV")

    def display_all_contacts(self):
        for book_name, contacts in self.address_books.items():
            print(f"\n[{book_name}]")
            for person in contacts:
                print(person)


# Example Usage
if __name__ == "__main__":
    manager = AddressBookManager()

    manager.add_address_book("family")
    manager.add_address_book("friends")

    manager.add_contact("family", Person("John", "Doe", "9876543210", "john@example.com", "MG Road", "Pune", "Maharashtra", "411001"))
    manager.add_contact("friends", Person("Jane", "Smith", "9123456780", "jane@example.com", "Link Road", "Mumbai", "Maharashtra", "400001"))

    manager.save_to_json("address_book.json")
    manager.save_to_csv("address_book.csv")

    manager.load_from_json("address_book.json")
    manager.display_all_contacts()