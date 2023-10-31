from collections import UserDict
import re
import sys


class Field:  # 1
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):  # 2
    # реалізація класу
    # def __init__(self, valu):
    #     self.name = valu

    pass


class Phone(Field):  # 3
    # phone = []
    # реалізація класу

    def __init__(self, value):
        sovp = re.findall('^(?:[( )-]*\d){10}[()-]*$', value)
        if sovp != []:
            while not sovp[0].isdigit():
                check_dig = sovp[0]
                for char in check_dig:
                    if not char.isdigit():
                        sovp[0] = sovp[0].replace(char, '')
            self.value = value
        else:
            raise ValueError

    def __str__(self):
        return 'ebtvoyu'


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        # print(phone.phone())
        self.phones.append(phone)
        pass

    def edit_phone(self, phone_was, phone_been):
        for ph in self.phones:
            if ph == phone_was:
                self.phones[self.phones.index(ph)] = phone_been

    def remove_phone(self):
        pass

    def find_phone():
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    # def __init__(self):
    #     self.address_book = {}

    def add_record(self, rec_list):
        # print(self.data)
        # self.address_book(Record.name) = '22323'
        self[str(rec_list.name)] = rec_list.phones
        print(self.data)

    def find(self, find_name):
        for name, record in self.data.items():
            
            if name == find_name:
                ret_class = Record(find_name)
                # print(1)
                # print(name, record)
                # print(2)
                # dict_rec = {name: record}
                return ret_class#dict_rec
            else:
                print('Nothing finded...')
                return None

    def delete(self, name):
        for name_book, record in self.address_book.items():
            print(name_book)
            if name_book == name:
                dele = True
                break

        if dele == True:
            self.address_book.pop(name_book)
        else:
            print('Nothing finded...')
        print(self.address_book)


def main():
    # Створення нової адресної книги
    book = AddressBook()
    # sys.exit()
    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # print(john_record)

    # Додавання запису John до адресної книги
    # print(type(john_record))

    book.add_record(john_record)
    # Створення та додавання нового запису для Jane

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі

    print(book.data)
    for name, record in book.data.items():

        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")

    print(f'>>> {john}')
    print(john)
    print(john.phones)

    sys.exit()
    john.edit_phone("1234567890", "1112223333")
    print(2)
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    sys.exit()

    # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


main()
