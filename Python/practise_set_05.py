#wap to create a dictionary of nepali words with values as their english translation
'''words = {
    "sahayog":"help",
    "biralo":"cat",
    "kukur":"dog"


}
a=input("Enter the word : ")
print(words[a])

#wap to input 8 numbers from the user and display all the unique numbers.
s=set()
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
n=int(input("Enter the number "))
s.add(n)
print(s)'''


#wap to create a empty dictionary and allow 4 friends to enter their favourite language as value and use key as their names 
d={}
name=input("Enter your Name ")
lang=input("Enter your language ")
d.update({name:lang})
name=input("Enter your Name ")
lang=input("Enter your language ")
d.update({name:lang})
name=input("Enter your Name ")
lang=input("Enter your language ")
d.update({name:lang})
name=input("Enter your Name ")
lang=input("Enter your language ")
d.update({name:lang})
print(d)