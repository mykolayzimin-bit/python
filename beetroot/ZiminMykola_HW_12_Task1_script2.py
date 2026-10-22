# Task1
# script2 відкриває файл myfile.txt читає його зміст і виводить цей зміст в консоль.

# нижче наведено скрипт який спрацює лише якщо буде запущений з
# тієї ж самої директорії що й myfile.txt
# with open("myfile.txt", 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
# якщо запустити з іншої папки - видасть помилку, не може знайти myfile.txt
# аби вирішити цю проблему, можна вказати повний шлях: with open("C:\Users\Mykola_Z\OneDrive\Desktop\Программирование\python\beetroot\myfile.txt", 'r')


# Але існує більш універсальний варіант:

import os

current_dir = os.path.dirname(os.path.abspath(__file__)) # з'ясовуємо шлях до директорії даного файлу, оскільки myfile.txt теж в ній знаходиться.
full_path = os.path.join(current_dir, "myfile.txt") # додаємо до шляху назву текстового файлу
# print(full_path)
with open(full_path, 'r', encoding='utf-8') as file:
    print(file.read())