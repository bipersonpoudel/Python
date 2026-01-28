import random
def get_user_choice():
    user=input("Rock, Paper or Scissors (r/p/s) ")
    user=user.lower()
    return user

def computer_choice():
    computer=random.choice("rps")
    return computer
def play_game():
    if (user=="r" and computer=="p"):
        print("You choose rock")
        print("Computer choose paper")
        print("Computer Won, You lose")
    elif (user=="p" and computer=="s"):
        print("You choose paper")
        print("Computer choose scissors")
        print("Computer Won, You lose")
    elif (user=="s" and computer=="r"):
        print("You choose Scissors")
        print("Computer choose Rock")
        print("Computer Won, You lose")
    elif (user=="s" and computer=="p"):
        print("You choose Scissors")
        print("Computer choose Paper")
        print("You Won, Computer lose")
    elif (user=="r" and computer=="s"):
        print("You choose Rock ")
        print("Computer choose Scissors")
        print("You Won, Computer lose")
    elif (user=="p" and computer=="r"):
        print("You choose Paper ")
        print("Computer choose Rock")
        print("You Won, Computer lose")
    elif (user=="p" and computer=="p"):
        print("You choose Paper ")
        print("Computer choose Paper")
        print("Draw")
    elif (user=="r" and computer=="r"):
        print("You choose Rock")
        print("Computer choose Rock")
        print("Draw")
    elif (user=="s" and computer=="s"):
        print("You choose Scissors ")
        print("Computer choose Scissors")
        print("Draw")

    else:
        print("Enter a valid choice")

    


while True:

    user=get_user_choice()
    computer=computer_choice()

    play_game()
    
    choice=input("Do You want to Continue (y/n) ")
    choice=choice.lower()
    if (choice=="n"):
        break
   

print("Thanks For playing")
 
