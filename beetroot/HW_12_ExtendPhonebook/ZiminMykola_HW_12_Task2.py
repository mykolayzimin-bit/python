import sys
import os
import json

def read_file():
    with open(sys.argv[1], "r", encoding='utf-8') as file:
        phone_book_file = json.load(file)
        return(phone_book_file)
    
def update_file(list):
    with open(sys.argv[1], "w", encoding='utf-8') as file:
        json.dump(list, file)

def add_new_entries(users_list):
    first_name = input("Enter First name: ")
    last_name = input("Enter Last name: ")
    telephone_number = input("Enter the phone number: ")
    city = input("Enter the city name: ")
    state = input("Enter the state name: ")
    
    users_list.append({
    "first_name": first_name,
    "last_name": last_name,
    "telephone_number": telephone_number,
    "city": city,
    "state": state
    })
    
    update_file(users_list)

def search_by_first_name(first_name, users_list):
    users = [user for user in users_list if user.get("first_name") == first_name]
    print(users)

def search_by_last_name(last_name, users_list):
    users = [user for user in users_list if user.get("last_name") == last_name]
    print(users)

def search_by_full_name(full_name, users_list):
    try:
        first_name, last_name = full_name.split()
        users = [user for user in users_list if user.get("first_name") == first_name and user.get("last_name") == last_name]
        print(users)
    except ValueError:
        print("Please enter both First name and Last name separated by a space.")

def search_by_telephone_number(phone_number, users_list):
    users = [user for user in users_list if user.get("telephone_number") == phone_number]
    return users

def search_by_city_or_state(city_or_state, users_list):
    users = [user for user in users_list if user.get("city") == city_or_state or user.get("state") == city_or_state]
    print(users)

def delete_by_telephone_number(phone_number, users_list): # умова: один номер - один користувач
    try:
        index = next((i for i, item in enumerate(users_list) if item.get("telephone_number") == phone_number), None)
        del users_list[index]
    except TypeError:
        print("You entered the number that not exist")

def update_by_telephone_number(phone_number, users_list):
    indexes = [index for index, user in enumerate(users_list) if user.get("telephone_number") == phone_number]
    
    if not indexes:
        print("You entered the number that not exist")
        return

    first_name = input(f"Enter new first name (current: {users_list[indexes[0]]['first_name']}) or press Enter to skip: ")
    if first_name:
        users_list[indexes[0]]['first_name'] = first_name
    last_name = input(f"Enter new last name (current: {users_list[indexes[0]]['last_name']}) or press Enter to skip:")
    if last_name:
        users_list[indexes[0]]['last_name'] = last_name
    telephone_number = input(f"Enter new phone number (current: {users_list[indexes[0]]['telephone_number']}) or press Enter to skip: ")
    if telephone_number:
        users_list[indexes[0]]['telephone_number'] = telephone_number
    city = input(f"Enter new city (current: {users_list[indexes[0]]['city']}) or press Enter to skip: ")
    if city:
        users_list[indexes[0]]["city"] = city
    state = input(f"Enter new state (current: {users_list[indexes[0]]['state']}) or press Enter to skip: ")
    if state:
        users_list[indexes[0]]["state"] = state
    
    print(users_list[indexes[0]])

if len(sys.argv) < 2:
    raise ValueError("Give the name of phone book!")
elif not os.path.isfile(sys.argv[1]):
    raise FileNotFoundError("The file is not exist")
else:
    users_list = read_file()
    print("""Choose the operation:
                    Add new entries - "1"
                    Search by first name - "2"
                    Search by last name - "3"
                    Search by full name - "4"
                    Search by telephone number - "5"
                    Search by city or state - "6"
                    Delete a record for a given telephone number - "7"
                    Update a record for a given telephone number - "8"
                    exit the program - "stop"
                """)
    while True:
        user_input = input("Choose the operation: ")
        if user_input == "1": #Add new entries
            add_new_entries(users_list)
        elif user_input == "2": #Search by first name
            first_name = input("Enter the First name: ")
            search_by_first_name(first_name, users_list)
        elif user_input == "3": # Search by last name
            last_name = input("Enter the Last name: ")
            search_by_last_name(last_name, users_list)
        elif user_input == "4": # Search by full name
            full_name = input("Enter the Full name: ")
            search_by_full_name(full_name, users_list)
        elif user_input == "5": # Search by telephone number
            phone_number = input("Enter the Telephone number: ")
            print(search_by_telephone_number(phone_number, users_list))
        elif user_input == "6": # Search by city or state
            city_or_state = input("Enter the City or State name:")
            search_by_city_or_state(city_or_state, users_list)
        elif user_input == "7": # Delete a record for a given telephone number
            phone_number = input("Enter the phone number: ")
            delete_by_telephone_number(phone_number, users_list)
        elif user_input == "8": # Update a record for a given telephone number
            phone_number = input("Enter the phone number: ")
            update_by_telephone_number(phone_number, users_list)
        elif user_input == "stop": # exit the program
            update_file(users_list)
            break
