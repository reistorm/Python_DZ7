from logger import input_data, delete_data, put_data, print_data

def interface():
    print('В телефонном справочнике доступны 4 функции:\n'
          '1. Записать данные\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n')
    operation = int(input('Введите номер операции: '))

    while operation < 1 or operation > 4:
        print('Неправильно введена команда!')
        operation = int(input('Введите номер операции: '))

    if operation == 1:
        input_data()
    elif operation == 2:
        delete_data()
    elif operation == 3:
        put_data()
    elif operation == 4:
        print_data()