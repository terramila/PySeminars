import os

def convert_to_int(string: str):
    return [int(number) for number in string.split(" ")]

path = os.path.join('folder', 'numbers.txt')
with open(path, 'r') as data:
    numbers = data.readline()
    list_number = convert_to_int(numbers)
    nok = 1
    new_nok = 0
    for element in list_number:
        nok *= element
    for index in range(1, nok):
        trigger = 0
        for element in list_number:
            if index%element == 0:
                trigger += 1
        if trigger == len(list_number):
            new_nok = index
            break

with open(path, 'a') as data:
    data.write(f"\nLeast common multiple for {str(list_number)[1:-1]} is {new_nok}")