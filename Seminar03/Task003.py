import time

limit = int(input("Введите предел: "))

def random_number(limit: int):
    rnd_number = str(time.time())
    rnd_number = rnd_number.split(".")
    rnd_number = int(rnd_number[1])
    while True:
        if rnd_number > limit:
            rnd_number %= 10
        else:
           return rnd_number

i = 0
while i < 10:
    print(random_number(limit))
    i += 1

