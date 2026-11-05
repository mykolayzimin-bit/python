# Task 1
# Method overloading.Polymorphyzm.

class Animal:
    def talk(self):
        pass
    
class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("meow")
        
def make_them_speak(instance):
    instance.talk()
    
murzik = Cat()
bobik = Dog()
    
make_them_speak(murzik)
make_them_speak(bobik)

# Task 2
# Library

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        
    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        author.books.append(book)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book
    
    def group_by_author(self, author):
        filtered_books = []
        for book in self.books:
            if book.author == author:
                filtered_books.append(book)
        return filtered_books
    
    def group_by_year(self, year: int):
        filtered_by_years = []
        for book in self.books:
            if book.year == year:
                filtered_by_years.append(book)
        return filtered_by_years
    
    def __str__(self):
        return f"Library: {self.name}"
    
    def __repr__(self):
        return f"Library(name='{self.name}')"

class Book:
    
    books_ammount = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.books_ammount += 1
        
    def __str__(self):
        return f"Book: {self.name}, Year: {self.year}, Author: {self.author.name}"
    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

class Author:
    
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
        
    def __str__(self):
        return f"Author: {self.name}, Country: {self.country}, Date of birth: {self.birthday}"
    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}')"

# Все перевірив - працює. Просто видалив зайвий код (бо його було багато).

# Task 3
# Fraction

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denomenator is equal to zero!")
        self.num = num
        self.den = den
        
    def __str__(self):
        return f"Fraction: {self.num}/{self.den}"
    
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __add__(self, other):
        return Fraction(self.num*other.den + self.den*other.num, self.den*other.den)
    
    def __sub__(self, other):
        return Fraction(self.num*other.den - self.den*other.num, self.den*other.den)
    
    def __mul__(self, other):
        return Fraction(self.num*other.num, self.den*other.den)
    
    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Denomenator is equal to zero!")
        return Fraction(self.num*other.den, self.den*other.num)
    
    def __eq__(self, other):
        if other is None or not isinstance(other, Fraction):
            return False
        return self.num*other.den == other.num*self.den

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))