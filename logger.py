from input import name_data, surname_data, phone_data, address_data, description_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    description = description_data()

    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name};{surname};{phone};{address};{description}\n\n')

def print_data():
    print('Вывод данных: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        phonebook_first = file.readlines()
        phonebook_first_v2 = []
        phonebook_middle = ''
        j = 0
        for i in range(len(phonebook_first)):
            if phonebook_first[i] == '\n' or i == len(phonebook_first) - 1:
                phonebook_first_v2.append(''.join(phonebook_first[j:i+1]))
                j = i
        phonebook_first = phonebook_first_v2
        print(''.join(phonebook_first))
    return phonebook_first

def put_data():
    phonebook_first = print_data()
    print("Какую запись вы хотите изменить? ")
    record_number = int(input('Введите номер записи: '))
    record_number -= 1
    print(f'Изменить данную запись\n{phonebook_first[record_number]}')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    description = description_data()
    phonebook_first = phonebook_first[:record_number] + [f'{name};{surname};{phone};{address};{description}\n'] + \
                      phonebook_first[record_number + 1:]
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(phonebook_first))
    print('Изменения успешно сохранены!')

def delete_data():
    phonebook_first = print_data()
    print("Какую запись по счету нужно удалить?")
    record_number = int(input('Введите номер записи: '))
    print(f'Удалить запись\n{phonebook_first[record_number - 1]}')
    phonebook_first = phonebook_first[:record_number] + phonebook_first[record_number + 1:]
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(phonebook_first))
    print('Изменения успешно сохранены')
