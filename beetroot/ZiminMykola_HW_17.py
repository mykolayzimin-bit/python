# Task 1
# School

class Person:
    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        
    def introduce(self):
        return f"My name is {self.first_name} {self.last_name}."
        
    def eat(self):
        return f"{self.first_name} is eating."
    
    def speak(self):
        return f"{self.first_name} is speaking."
    
    def walk(self):
        return f"{self.first_name} is walking."
    
    def think(self):
        return f"{self.first_name} is thinking."
    
class Teacher(Person):
    def __init__(self, first_name, last_name, age, height, weight, salary, diploma, license):
        super().__init__(first_name, last_name, age, height, weight)
        self.salary = salary
        self.diploma = diploma
        self.license = license
        
    def introduce(self):
            return super().introduce() + " " + f"I'm a teacher."
        
    def teach(self):
        return f"{self.first_name} is teaching"
        
class Student(Person):
    def __init__(self, first_name, last_name, age, height, weight):
        super().__init__(first_name, last_name, age, height, weight)
        
    def introduce(self):
            return super().introduce() + " " + f"I'm a student."
        
    def study(self):
        return f"{self.first_name} is studying"
    
# Task 2
# Mathematician

class Mathematician:
    
    def square_nums(self, list_nums: list):
        return list(map(lambda x: x**2, list_nums))

    def remove_positives(self, list_nums: list):
        return list(filter(lambda x: x < 0, list_nums))

    def filter_leaps(self, list_years: list):
        return list(filter(lambda x: x % 4 == 0, list_years))

    
m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# Task 3
# Product Store

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.storage = {}
        self.income = 0
    
    def add(self, product, amount):
        if product.name in self.storage:
            self.storage[product.name]["amount"] += amount
        else:
            self.storage[product.name] = {
            "product": product, 
            "amount": amount, 
            "price": product.price * 1.3
            }
    
    def set_discount(self, identifier, percent, identifier_type):
        if identifier_type == "name":
            if identifier in self.storage:
                self.storage[identifier]["price"] *= 1 - percent/100
            else:
                raise ValueError("No such product in the storage.")
        elif identifier_type == "type":
            found = False
            for item in self.storage.values():
                if item["product"].type == identifier:
                    found = True
                    item["price"] *= 1 - percent/100
            if not found:
                raise ValueError(f"There's no such type of product {identifier}")                    
        else:
            raise ValueError(f"Unknown identifier type: {identifier_type}")
    
    def sell_product(self, product_name, amount):
        if product_name in self.storage:
            if self.storage[product_name]["amount"] >= amount:
                self.storage[product_name]["amount"] -= amount
                self.income += amount*self.storage[product_name]["price"]
            else:
                raise ValueError(f"There are only {self.storage[product_name]['amount']}pcs of this product in the storage.")
        else:
            raise ValueError("No such product in the storage.")
    
    def get_income(self):
        return self.income
    
    def get_all_products(self):
        return self.storage
    
    def get_product_info(self, product_name):
        if product_name in self.storage:
            return (product_name, self.storage[product_name]["amount"])
        else:
            raise ValueError("No such product in the storage.")

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

print(s.get_product_info("Ramen"))

s.sell_product('Ramen', 10)

print(s.get_product_info("Ramen"))

assert s.get_product_info('Ramen') == ('Ramen', 290)

# Task 4
# Custom exception

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", 'a') as file:
            file.write(msg + '\n')
        super().__init__(msg)
        
try:
    raise CustomException("my own exception")
except CustomException as e:
    print("Exception has been catched successfuly")