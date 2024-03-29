from collections import UserDict
import re
import sys
import copy

class Field:  # 1
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # return 'ebtvoyu Field'
        return str(self.value)


class Name(Field):  # 2
    # реалізація класу
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
        # return 'ebtvoyu Name'
    pass


class Phone(Field):  # 3
    # phone = []
    # реалізація класу

    def __init__(self, value):  # регуляр телефона 10
        # '^(?:[( )-]*\d){10}[()-]*$' # UA-10
        sovp = re.findall('^(\d){10}$', value)
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
        return 'ebtvoyu Phone'


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
        #     print(self.phones)
        # return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    # def __init__(self):
    #     self.address_book = {}

    def add_record(self, rec_list):
        # print(self.data)
        # self.address_book(Record.name) = '22323'
        self[str(rec_list.name)] = rec_list.phones
        # print(self.data)

    def find(self, find_name):
        print(f'getted>> {find_name}')
        # if find_name in self.data:
        print(f'data>> {self.data.get(find_name)}')
        nm = self.data.get(find_name)
        print(f'nm>> {nm}')
        nm = ['7777777777']
        print(f'nm>> {nm}')
        print(f'data>> {self.data.get(find_name)}')
        # for name, record in self.data.items():
            # print(name.__)
            # if name == find_name:
            #     ret_class = copy.copy(find_name)
            #     ret_class.phones = record
            #     return ret_class  # dict_rec

        print(f'Nothing finded about {find_name}...')
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
    jane = book.find('Jane')
    print(jane)
    john = book.find("John")

    # print(f'>>> {john}')
    # print(john)
    # print(john.phones)

    sys.exit()
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    john.name.value = 'Johny'
    print(john)
    print(john_record)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


main()
