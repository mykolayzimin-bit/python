
# Task 1

sentence = input("Input a sentence: ")
sentence_list = sentence.split()
my_dict = {}

count = 0
while count < len(sentence_list):

    if sentence_list[count] == "-" or sentence_list[count] == "," or sentence_list[count] == "." or sentence_list[count] == "!" or sentence_list[count] == "?": # Очистка від елемиентів, що є розділяючими знаками
        sentence_list.remove(sentence_list[count])
        count = 0
    elif "-" in sentence_list[count]: # Очистка від елементів, що можуть бути в середині окремого елементу
        new_elems = sentence_list[count].split("-")
        sentence_list.remove(sentence_list[count])
        for elem in new_elems:
            sentence_list.insert(count, elem)
            count += 1
        count = 0
    else: count += 1
        
for i, w in enumerate(sentence_list): # Прибираємо зайві символи покраях елементів
    sentence_list[i] = str(w).strip(",.-")

for i, elem in enumerate(sentence_list): # Наповнюємо словник
    my_dict[elem] = i
    
print(my_dict)


# Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_pice = {}

for key in stock:
    total_pice[key] = stock[key]*prices[key]
    
print(total_pice)


# Task 3

my_list = [(i, i**2) for i in range(1,11)]
print(my_list)

# Task 4

days = ["Monday", "Tuesday",  "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_dict = {days[i]:i+1 for i in range(len(days))}
days_dict_reversed = {i+1:days[i] for i in range(len(days))}
# Або можна було б так:
#days_dict_reversed = {value: key for key, value in days_dict.items()}

print(days_dict)
print(days_dict_reversed)