# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def multiple_num():
    var1 = "snow"
    var2 = 5
    var3 = True
    var4 = 1.87
    var5 = 5*3

print(f"Tne number of local variables is: {len(multiple_num.__code__.co_varnames)}") # Виводить в консоль кількість локальних змінних

# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def outer_func():
    def inner_func():
        return "The function was transmitted"
    return inner_func

f = outer_func()
print(f())

# Task 3

# Write a function called "choose_func" which takes a list of nums and 2 callback functions. If all nums inside the list are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2):
    filtered_nums = filter(lambda num: num > 0, nums)
    if len(list(filtered_nums)) == len(nums):
        return func1(nums)
    else:
        return func2(nums)

# Assertions

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))