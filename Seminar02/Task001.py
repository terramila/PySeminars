number = int(input("Введите количество шагов: "))

def list_from(number: int):
    list_numbers = []
    for element in range (0, number):
        list_numbers.append((-3)**element)
    return list_numbers

print(list_from(number))