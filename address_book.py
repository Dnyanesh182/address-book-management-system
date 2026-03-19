# UC1 – Create Person Class

class Person:
    def __init__(self, first_name: str, last_name: str, phone: str, email: str, address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name}, "
            f"Phone: {self.phone}, "
            f"Email: {self.email}, "
            f"Address: {self.address}"
        )


# 🔹 Example Usage
if __name__ == "__main__":
    person = Person(
        "John",
        "Doe",
        "9876543210",
        "john@example.com",
        "Pune, India"
    )

    print(person)