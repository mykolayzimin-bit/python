try:
    age = int(input(f"Введите ваш возраст: "))
    if(age < 0):
        raise MemoryError("Возраст должен быть положительным")
    print(f"Ваш возраст: {age}")
    
except ValueError:
    print("Возраст должен быть целым числом")
    
except MemoryError as e:
    print(e)