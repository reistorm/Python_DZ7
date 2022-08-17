from input import name_data
from input import surname_data
from input import phone_data
from input import address_data
from input import description_data

list = [f'Name: {name_data}', f'Surname: {surname_data}', f'Phone: {phone_data}', f'Address: {address_data}', f'Description: {description_data}']

def write_pb():
    f = open('phonebook.txt', 'a')
    for i in list:
        f.write(i + '\n')
    f.write('\n')
    f.close()
