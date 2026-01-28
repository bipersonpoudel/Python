import random
character="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
a=int(input("Enter the password length "))
password=""
for i in range (a):
    pas=random.choice(character)
    password=password+pas

print("Your password is :",password)