
# Task 1

import random

numberToGess = random.randint(1,10)
# print(numberToGess)
usersNumber = int(input("Guess the number from 1 to 10: "))

if usersNumber == numberToGess:
    print(f"Congratulations! The number was: {numberToGess}")
else:
    print(f"Sorry mate, but the number is: {numberToGess} and yours was: {usersNumber}")
    
    
# Task 2

name = input("What's your name?: ")
age = int(input("How old are you?: "))

print(f"Hello {name}, on your next birthday you’ll be {age+1} years")

# Task 3

targetString = input("Give us yours string here: ") # Запрашиваем строку у пользователя
count = len(targetString) - 1

for repetition in range(5):  #Выполняем 5 раз генерацию рандомного слова
    positionNums = ""
    iterator = 0

    while iterator <= count:
        ranPosition = random.randint(0, len(targetString) - 1)
        if positionNums:
            already_exists = False
            for i in positionNums:
                if ranPosition == int(i):
                    already_exists = True
                    break
            if not already_exists:
                positionNums += str(ranPosition)
                iterator += 1
        else:
            positionNums += str(ranPosition)
            iterator += 1                          
                    
    # Печатаем буквы перемешанной строки
    for num in positionNums:
        print(f"{targetString[int(num)]}", end="")
    # Вместо перехода на новую строку ставим разделитель между 5-ю результатами
    print(", ", end="") 
