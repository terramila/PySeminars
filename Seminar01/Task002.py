numbers = input("Введите числа через пробел: ")
num_list = numbers.split(" ")
max_num = num_list[0]
for i in num_list:
    if i > max_num:
        max_num = i

print(f"Максимальное число - {max_num}")