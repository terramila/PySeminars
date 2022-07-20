print("Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.")
limit = int(input("Введите предел: "))
list_num = []
i = -limit
while (i<=limit):
    list_num.append(i)
    i += 1
print(list_num)