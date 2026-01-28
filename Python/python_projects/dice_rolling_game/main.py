import random
while True:
    choice=input("Do you want to roll the dice (y/n) ")
    if (choice=="y" or choice=="Y"):
        print((random.randint(1,6),random.randint(1,6)))

    elif(choice=="n" or choice=="N"):
        print("Thanks for playing")
        break

    else:
        print("Invalid Choice")
   
