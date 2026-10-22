import os

def count_lines(file_object): # рахуємо кількість рядків
    return len(file_object.readlines())


def count_chars(file_object): # рахуємо кількість символів
    return len(file_object.read())


def test(name):
    if name == "mymod.py": # шукаємо повний шлях згідно з переданим ім'ям
        name = os.path.abspath(__file__)
        
    try:
        with open(name, 'r', encoding='utf-8') as file:
            lines = count_lines(file)
            file.seek(0) #повертаємо курсор
            chars = count_chars(file)
            
            print(f"Файл: {name}")
            print(f"Количество строк: {lines}")
            print(f"Количество символов: {chars}")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл '{name}' не найден.")
