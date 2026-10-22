# Task1
# script1 Створюємо текстовий файл із текстом.

with open("myfile.txt", 'w', encoding='utf-8') as file:
    file.write("Hello file world!")

# Цей скрипт створив файл в тій самій директорії звідки був викликаний.