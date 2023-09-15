from collections import UserDict
import sys


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    # реалізація класу
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(phone)
        pass

    def edit_phone(self, was, been):
        for phone in self.phones:
            if phone == was: 
                self.phones[self.phones.index(phone)] = been

    def find_phone(self, phone):
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):
        self.address_book = {}

    def add_record(self, rec_list):
        # print(self.data)
        # self.address_book(Record.name) = '22323'
        self.address_book[str(rec_list.name)] = rec_list.phones
        print(self.address_book)
        pass

    def find(self, find_name):
        for name, record in self.address_book.items():
            if name == find_name:
                return record
            else:
                print('Nothing finded...')
                return None


def main():
    # Створення нової адресної книги
    book = AddressBook()
    # sys.exit()
    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    print(john_record.phones)

    # Додавання запису John до адресної книги
    # print(type(john_record))

    book.add_record(john_record)
    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі

    print(book.address_book)
    for name, record in book.address_book.items():
        print(name)
        print(record)

    print('yep')

    # Знаходження та редагування телефону для John
    john = book.find("John")
    print(john)
    john_record.edit_phone("1234567890", "1112223333")
    print(2)
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john_record.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


main()
