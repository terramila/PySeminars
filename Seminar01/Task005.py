number = input("Введите дробное число: ")
if int(number)%1 == 0:
    print("нет")
else:
    char_list = number.split(",")
    print(char_list[1][0])