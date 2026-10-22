def greet():
    name = input("Ваше имя? ")
    print(f"Привет, {name}!")

def check_age():
    age = input("Ваш возраст? ")
    
    try:
        age = int(age)
        if age >= 18:
            print("Доступ разрешен")
        elif 0 < age < 18:
            print("Доступ запрещен")
        else:
            print("Возраст должен быть целым числом большим 0")
    except ValueError:
        print("Возраст должен быть числом!")

def show_menu():
    return("Меню: 1-приветствие, 2-проверка возраста, 3-выход")

print(show_menu())

while True:
    choice = input("Сделайте ваш выбор ")
    
    if choice == "1":
        greet()
    elif choice == "2":
        check_age()
    elif choice == "3":
        break
    else:
        print("Неизвестная команда")