
# Task 1

str = "x"
if len(str)>=2:
    print(str[0:2]+str[-2:])
else:
    print("Empty String")
    
# Task 2

phoneNumber = "012345678"
if len(phoneNumber) != 10:
    print("The phone number has wrong length")
elif not(phoneNumber.isdigit()):
    print("The phone number is not numeric")
else:
    print("The phon number is valid")
    
# Task 3

print("Give me your answer: 30 + 3 is?")
answer = 31
if answer != 33:
    print("No, it's not!")
else:
    print("Yes, you're right!")
    
# Task 4

myName = "Mykola"
givenName = "Mykolj"

myName = myName.lower()
givenName = givenName.lower()

if len(givenName) == len(myName):
    step = 0
    for char in givenName:
        if char != myName[step]:
            print(False)
            break
        step+=1
    if step == len(givenName):
        print(True)
else:
    print(False)