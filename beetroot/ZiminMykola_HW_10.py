
# Task1
# Imports practice

import mz_module_hw10 as module

print(module.say_hi("Mykola"))

# Task2
# The sys module
# Передумова: рівнем вище створив папку hw_10_module, де
# помістив файл syspath_test.py
import sys
# import syspath_test - виклик в цьому місці дає помилку ModuleNotFoundError: No module named 'syspath_test'
print(sys.path) 
sys.path.append("C:/Users/Mykola_Z/OneDrive/Desktop/Программирование/python/hw_10_module")
print(sys.path) # бачимо, що додався наш шлях до модулю
import syspath_test
# Імпорт спрацював: в консолі з'явилось повідомлення 'Hello sys.path!'

# Task3
# Basics, import, work with os module
import mymod

mymod.test("mymod.py")