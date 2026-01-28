import random
n=random.randint(1,100)
a=0
guess=0
while(a!=n):
    guess+=1
    a=int(input("Guess the Number: "))
    if(a>n):
        print("Try some lower number")
    elif(a<n):
        print("Try some greater number")
    guess+=1
    
print("Congrats!! You have guessed the number correctly on ",guess, " attempt")