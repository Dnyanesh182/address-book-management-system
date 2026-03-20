from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from address_book import Person, AddressBookManager, DuplicateContactError


def test_add_contact():
    manager = AddressBookManager()
    manager.add_address_book("family")

    person = Person(
        "John", "Doe", "9876543210", "john@example.com",
        "MG Road", "Pune", "Maharashtra", "411001", ["VIP"]
    )

    manager.add_contact("family", person)

    assert len(manager.address_books["family"]) == 1
    assert manager.address_books["family"][0].first_name == "John"


def test_duplicate_contact():
    manager = AddressBookManager()
    manager.add_address_book("family")

    person1 = Person(
        "John", "Doe", "9876543210", "john@example.com",
        "MG Road", "Pune", "Maharashtra", "411001", ["VIP"]
    )

    person2 = Person(
        "John", "Doe", "9876543210", "john@example.com",
        "FC Road", "Pune", "Maharashtra", "411004", ["Family"]
    )

    manager.add_contact("family", person1)

    try:
        manager.add_contact("family", person2)
        assert False
    except DuplicateContactError:
        assert True