# Task1
# A simple function.

def favorite_movie(movie_name):
    print(f"My favorite movie is named {movie_name}")
    
favorite_movie("Matrix")

# Task2
# Creating a dictionary.

def make_country(country, capital):
    country_dict = {"country": country,
                    "capital": capital
                    }
    print(country_dict)
    
make_country("France", "Paris")

# Task3
# A simple calculator.

def make_operation(operator, *numbers:int):
    if operator == "+":
        return sum(numbers)
    elif operator == "-":
        return numbers[0] - sum(numbers[1:])
    elif operator == "*": #Вирішив не використовувати import (для різноманітності)
        multiply_list = list(numbers)
        multiplication = multiply_list[0]
        for i in range(1, len(multiply_list)):
            multiplication *= multiply_list[i]
        return multiplication
    
print(make_operation("-", 1,2,3,4,5,6))