org_text = input("Введите изначальную строку через запятую: ")
find_text = input("Введите искомую подстроку: ")

org_text = org_text.split(",")
find_list = []
count = 0
print(org_text)
print(find_text)

for index in range(len(org_text)):
    if str(find_text) == org_text[index]:
        count += 1
        if count > 1:
            print(f"Второе вхождение по индексу {index}")
            break
else:
    print("Второго вхождения нет")