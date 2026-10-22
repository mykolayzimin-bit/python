try:
    a = 10
    val = input("Введите делитель : ")
    num = int(val)
    division = a/num
    print(f"Результат деления: {devision}")
except ValueError:
    print("Это не число")
except ZeroDivisionError:
    print("Деление на ноль недопустимо!")
else:
    print("Операция успешно выполнена")
finally:
    print("Программа завершила свою работу")