import os

def convert_to_int(string: str):
    return [int(number) for number in string]

path = os.path.join('folder', 'equation.txt')
with open(path, 'r') as data:
    numbers = data.readlines()
    list_number = convert_to_int(numbers)
    print(list_number)
    discr = list_number[1]**2 - 4*list_number[0]*list_number[2]
    x_1 = (-list_number[1] + discr**0.5) / (2 * list_number[0])
    x_2 = (-list_number[1] - discr**0.5) / (2 * list_number[0])

with open(path, 'a') as data:
    data.write("\nX1 = " + str(x_1))
    data.write("\nX2 = " + str(x_2))
