# wap to print the greatest number from four number entered by user
'''a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))
c=int(input("Enter Third Number ") )
d=int(input("Enter Fourth Number "))
if (a>b and a>c and a>d):
    print("Greatest numbr is ", a)
elif (b>a and b>c and b>d):
    print("Greatest number is ",b )

elif (c>a and c>b and c>d):
    print("Greatest number is ",c )

else:
    print("Greatest is ", d)

#wap to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.
a=int(input("Enter marks of first subject out of 100"))
b=int(input("Enter marks of second subject out of 100"))
c=int(input("Enter marks of third subject out of 100"))
total=a+b+c
perc=(total/300)*100
if (perc>=40 and a>=33 and b>=33 and c>=33):
    print("Congrats You have passed the exam")
    print("Your Percentage is ", perc)

else :
    print("Sorry! You have Failed your exam")
#wap to detect the spam. Following words are spam
s="MAKE A LOT OF MONEY"

t= "BUY NOW" 

u= "SUBSCRIBE THIS"

v="CLICK THIS"

a=input("Enter your comment ")
a=a.upper()
if ((s in a) or (t in a) or (u in a) or (v in a)):
    print("This is a spam")

else:
    print("Not a spam")



a=input("Enter  your Username ")
if (len(a)<10):
    print("This Username contains less than 10 characters")

else:
    print("This Username contains more than 10 characters")


#wap which finds out whether given name is present in the list or not
list=["biperson","bipson","ram","shyam"]
name=input("Enter your name ")
name=name.lower()
if (name in list):
    print(" C0ngrats on aboard!! Your name is present on the list.")
else:
    print("Sorry! Not on the list")'''
'''
wap to calculate the grade of a student from his marks from the following scheme
90-100 =>Ex
80-90 =>A
70-80 =>B
60-70 =>C
50-60 =>D
<50 =>F


a=int(input("Enter Your Marks Out of 100 "))
if(a>=90 and a<100):
    print("Ex")
    
elif(a>=80 and a<90):
    print("A")
elif(a>=70 and a<80):
    print("B")
elif(a>=60 and a<70):
    print("C")
elif(a>=50 and a<60):
    print("D")
elif(a<50):
    
    print("F")
    
else:
    print("Invalid Marks")'''
#wap to find out whether a given post os talking about "bipson" or not
post=input("Enter the post ")
post=post.lower()
if("bipson" in post):
    print("The post is Talking about Mr.Bipson ")

else:
    print("The post is not about Mr.Bipson")
