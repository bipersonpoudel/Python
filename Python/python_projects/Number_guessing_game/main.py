import random
print("Rules for the games :")
print("Computer will choose a random number between 1 - 100 and you have to guess it in low attempts as possible")
computer_choice=random.randint(1,100)
guess=0
attempt=1
while (guess!=computer_choice):
    attempt+=1
    try:
        guess=int(input("Enter your guess : "))
        if(guess>computer_choice):
            print("Try some lower number")
        elif(guess<computer_choice):
            print("Try some greater number")
        elif(guess==computer_choice):
            print("Congrats!! You guessed it right in ",attempt," attempts")
    
    except ValueError:
        print("Enter a valid number")

        
   