# Task 1
# A Person class

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")
        
# Task 2
# Doggy age

class Dog:
    age_factor = 7
    def __init__(self, age):
        self.age = age
    
    def human_age(self):
        return self.age*self.age_factor
    
# Task 3
# TV controller

class TVController:
    def __init__(self, channels):
        self.channels = channels
        
    curr_channel = 0
    
    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[len(self.channels) - 1]

    def turn_channel(self, num):
        self.curr_channel += num - 1
        return self.channels[num - 1]

    def next_channel(self):
        self.curr_channel += 1
        return self.channels[self.curr_channel]

    def previous_channel(self):
        self.curr_channel -= 1
        return self.channels[self.curr_channel]

    def current_channel(self):
        return self.channels[self.curr_channel]

    def exists(self, num):
        if num <= len(self.channels):
            return "Yes"
        else:
            return "No"

    def exists(self, channel: str):
        if channel in self.channels:
            return "Yes"
        else:
            return "No"
        
controller = TVController(["BBC", "Discovery", "TV1000"])

print(controller.first_channel()) #== "BBC"

print(controller.last_channel()) #== "TV1000"

print(controller.turn_channel(1)) #== "BBC"

print(controller.next_channel()) #== "Discovery"

print(controller.previous_channel()) #== "BBC"

print(controller.current_channel()) #== "BBC"

print(controller.exists(4)) #== "No"

print(controller.exists("BBC")) #== "Yes"