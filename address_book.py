# UC10 – Enterprise-Level Features

import json
import csv
import uuid
import logging


logging.basicConfig(
    filename="address_book.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ContactError(Exception):
    pass


class DuplicateContactError(ContactError):
    pass


class AddressBookFileError(ContactError):
    pass


class Person:
    def __init__(self, first_name, last_name, phone, email, address, city, state, zip_code, tags=None, contact_id=None):
        self.contact_id = contact_id if contact_id else str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.tags = tags if tags else []

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            "contact_id": self.contact_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "tags": self.tags
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
            data["zip_code"],
            data.get("tags", []),
            data.get("contact_id")
        )

    def __str__(self):
        return (
            f"{self.contact_id} | {self.full_name()} | {self.phone} | {self.email} | "
            f"{self.address}, {self.city}, {self.state} - {self.zip_code} | Tags: {', '.join(self.tags)}"
        )


class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name not in self.address_books:
            self.address_books[name] = []
            logging.info(f"Created address book: {name}")

    def add_contact(self, book_name, person):
        if book_name not in self.address_books:
            self.address_books[book_name] = []

        for contact in self.address_books[book_name]:
            if (
                (contact.first_name == person.first_name and contact.last_name == person.last_name)
                or contact.phone == person.phone
                or contact.email == person.email
            ):
                logging.warning(f"Duplicate contact rejected in {book_name}: {person.full_name()}")
                raise DuplicateContactError("Duplicate contact detected")

        self.address_books[book_name].append(person)
        logging.info(f"Added contact {person.full_name()} to {book_name}")

    def filter_by_tag(self, tag):
        results = []
        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if tag.lower() in [t.lower() for t in contact.tags]:
                    results.append((book_name, contact))
        return results

    def filter_by_city(self, city):
        results = []
        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if contact.city.lower() == city.lower():
                    results.append((book_name, contact))
        return results

    def save_to_json(self, filename):
        data = {
            book_name: [person.to_dict() for person in contacts]
            for book_name, contacts in self.address_books.items()
        }

        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            logging.info(f"Saved address books to JSON: {filename}")
        except OSError as error:
            logging.error(f"Failed to save JSON file {filename}: {error}")
            raise AddressBookFileError(f"Failed to save JSON file: {error}")

    def load_from_json(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.address_books = {
                book_name: [Person.from_dict(person_data) for person_data in contacts]
                for book_name, contacts in data.items()
            }
            logging.info(f"Loaded address books from JSON: {filename}")
        except (OSError, json.JSONDecodeError) as error:
            logging.error(f"Failed to load JSON file {filename}: {error}")
            raise AddressBookFileError(f"Failed to load JSON file: {error}")

    def display_all_contacts(self):
        for book_name, contacts in self.address_books.items():
            print(f"\n[{book_name}]")
            for person in contacts:
                print(person)


# Example Usage
if __name__ == "__main__":
    manager = AddressBookManager()

    manager.add_address_book("family")
    manager.add_address_book("office")

    try:
        manager.add_contact(
            "family",
            Person("John", "Doe", "9876543210", "john@example.com", "MG Road", "Pune", "Maharashtra", "411001", ["VIP", "Family"])
        )
        manager.add_contact(
            "office",
            Person("Jane", "Smith", "9123456780", "jane@example.com", "Link Road", "Mumbai", "Maharashtra", "400001", ["Work"])
        )
    except DuplicateContactError as error:
        print(f"❌ {error}")

    print("\nFiltered by tag 'VIP':")
    for book_name, person in manager.filter_by_tag("VIP"):
        print(f"[{book_name}] {person}")

    print("\nFiltered by city 'Mumbai':")
    for book_name, person in manager.filter_by_city("Mumbai"):
        print(f"[{book_name}] {person}")

    try:
        manager.save_to_json("enterprise_address_book.json")
        manager.load_from_json("enterprise_address_book.json")
    except AddressBookFileError as error:
        print(f"❌ {error}")