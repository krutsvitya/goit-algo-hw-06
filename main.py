from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10:
            super().__init__(value)
        else:
            pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_instance = self.find_phone(phone)
        if phone_instance:
            self.phones.remove(phone_instance)
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone, new_phone):
        phone_instance = self.find_phone(old_phone)
        if phone_instance:
            # Заміна старого телефону на новий
            index = self.phones.index(phone_instance)
            self.phones[index] = Phone(new_phone)
        else:
            raise ValueError("Old phone number not found")


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def __str__(self):
        result = []
        for key in self.data:
            result.append(f"{str(key)}: {str(self.data[key])}")
        return "\n".join(result)

    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        if self.data[name]:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        self.data.pop(name)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")


