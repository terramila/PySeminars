org_text = input("Введите строку: ")
find_text = input("Введите искомую строку: ")

def text_finder(org_text: str, find_text: str):
    counter = 0
    for index in range (0, len(org_text) - len(find_text)+1):
        if find_text in org_text[index:index+len(find_text)]: counter += 1
    return counter

print(f"Текст '{find_text}' втречается в тексте {text_finder(org_text, find_text)} раз")