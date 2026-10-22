# Модули и библиотеки
# Вариант А
import random
val = random.randint(1,100)
print(f"Случайное число: {val}")

# Вариант Б
from random import randint
val = randint(1, 100)
print(f"Случайное число: {val}")

# Вариант В
import random as rnd
val = rnd.randint(1, 100)
print(f"Случайное число: {val}")