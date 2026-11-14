# Task 1

def with_index(iterable, start=0):
    n = start
    for item in iterable:
        yield n, item
        n += 1
        
# data = ['a', 'b', 'c']
# for idx, val in with_index(data, start=1):
#     print(idx, val)
# print(list(with_index(data)))


# Task 2

def in_range(start, end, step=1):
    if step != 0:
        count = start
        
        if step > 0:
            while count < end:
                yield count
                count += step
        elif step < 0:
            while count > end:
                yield count
                count += step
    else:
        raise ValueError("Zero step!")

# for num in in_range(1, 5):    
#     print(num, end=" ") # 1, 2, 3, 4.
# print() # to wrap the line
# print(list(in_range(0, 10, 3))) # 0, 3, 6, 9.
# print(list(in_range(5, 0, -1))) # 5, 4, 3, 2, 1.
# print(list(in_range(5, 1))) #[]
# print(list(in_range(1, 5, -1))) # []
# print(list(in_range(1, 5, 0))) # ValueError("Zero step!").


# Task 3

class MyIterable:
    def __init__(self, data):
        self.data = list(data)
        
    def __iter__(self):
        count = 0
        while count < len(self.data):
            yield self.data[count]
            count += 1
            
    def __getitem__(self, index):
        return self.data[index]
            
# Test implementation
my_collection = MyIterable([10, 20, 30, 40, 50])
print(my_collection[0])

# 1. for-in (first loop)
print("First circle for:")
for item in my_collection:
    print(item, end=" ")
print()

# 2. for-in (second loop)
print("Second circle for:")
for item in my_collection:
    print(item, end=" ")
print()

# 3.Call the element by using []
print("First elem:", my_collection[0])   # Expected: 10
print("Last elem:", my_collection[-1])   # Expected: 50
print("Slice:", my_collection[1:4])       # Expected: [20, 30, 40]

# 4. Out of range
try:
    print(my_collection[100])
except IndexError:
    print("IndexError has been caught")