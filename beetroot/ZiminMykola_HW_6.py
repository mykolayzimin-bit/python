
import random


# Task 1
# The greatest number.
my_list = []
while len(my_list) < 10:
    my_list.append(random.randint(1,100))
largest = max(my_list)
print(my_list)
print(largest)

# Task 2
# Exclusive common numbers.
list_1 = []
list_2 = []

while len(list_1) < 10:
    list_1.append(random.randint(1,10))
while len(list_2) < 10:
    list_2.append(random.randint(1,10))
    
common_numbers = list(set(list_1) & set(list_2))
    
print(list_1, list_2, sep="\n")
print(common_numbers)

# Task 3
# Extracting numbers.
list_100 = list(range(1, 101))
list_new = []
count = 0
while count <= len(list_100) - 1:
    if list_100[count]%7 == 0 and list_100[count]%5 != 0:
        list_new.append(list_100[count])
    count += 1
print(list_new)