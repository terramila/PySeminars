number = int(input("Введите число: "))
if (number % 5 == 0) and (number % 10 == 0):
    print(f"Число {number} кратно 5 и 10")
if (number % 15 == 0) and (number % 30 != 0):
    print(f"Число {number} кратно 15, но не 30")
