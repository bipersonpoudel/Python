'''f=open("poems.txt","r")
data=f.read()
if ("twinkle" in data):
    print("Twinkle is present in the poem")

else:
    print("Tinkle is not present in the poem")    
f.close()'''
'''import random
def game():
  
    return random.randint(1,16)
score=game()
f=open("Hi-score.txt","r")
hiscore = int(f.read())


f.close()
f=open("Hi-score.txt","w")
if (score>int(hiscore) or hiscore==""):
    f.write(str(score))
f.close()'''
'''f=open("table.txt","w")
f.write("Multiplication table")
f.close()

def multiply(n):
    i=1
    while (i<=10):
        m=n*i
        a=n+""*",i, "=",m"
        f=open("table.txt","a")
        f.write(a)
        f.close
        i=i+1

n=int(input("Enter a number "))
multiply(n)'''




'''word="donkey"
f=open("about_donkey.txt","r")
data=f.read()

datanew=data.replace("donkey","######")
f.close()
f=open("about_donkey.txt","w")
f.write(datanew)
f.close'''
'''words=["donkey","is","animal","good"]
f=open("about_donkey.txt","r")
data=f.read()
for words in data:
    data=data.replace(data,"######")
f.close()
f=open("about_donkey.txt","w")
f.write(data)
f.close'''
#wap