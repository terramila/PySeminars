org_text = input("Введите изначальную строку через запятую: ")
find_text = input("Введите искомую подстроку: ")

org_text = org_text.split(",")
find_list = []

for element in org_text:
    if find_text in element:
        find_list.append(element)

print(find_list)