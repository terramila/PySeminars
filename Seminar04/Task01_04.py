import os

def convert_to_int(string: str):
    return [int(number) for number in string.split(" ")]

path = os.path.join('folder', 'file.txt')
with open(path, 'r') as data:
    numbers = data.readline()
    list_number = convert_to_int(numbers)


    print(f"В файле {path} минимальное значение {min(list_number)} и максимальное значение {max(list_number)}")