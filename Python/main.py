''' ROCK PAPER SCISSOR USING PYTHON
1=rock
0=paper
-1=scissors
'''
import random
computer = random.choice([-1, 0, 1])
you=input("Enter your choice (r=rock p=paper and s= scissors) ")
youdict={"r":1,"p":0,"s":-1}
you =youdict[you]

if (computer==-1 and you==1):
    print("Computer : Scissors")
    print("You:rock")
    print("You Won")
elif (computer==1 and you==0):
    print("Computer : Rock")
    print("You:Paper")
    print("You Won")
elif (computer==0 and you==-1):
    print("Computer : Paper")
    print("You: Scissors")
    print("You Won")
    
elif (computer==-1 and you==0):
    print("Computer : Scissors ")
    print("You: Paper")
    print("Computer Won")
elif (computer==0 and you==1):
    print("Computer : Paper")
    print("You: Rock")
    print("Computer Won")

elif (computer==1 and you==-1):
    print("Computer : Rock")
    print("You:Scissors")
    print("Computer Won")
elif (computer==1 and you==1):
    print("Computer : Rock")
    print("You:Rock")
    print("Draw")
elif (computer==0 and you==0):
    print("Computer : Paper")
    print("You: Paper")
    print("Draw")
elif (computer==-1 and you==-1):
    print("Computer : Scissors ")
    print("You: Scissors")
    print("Draw")
