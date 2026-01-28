'''def avg():
    a=int(input("Enter a number "))
    b=int(input("Enter a number "))
    c=int(input("Enter a number "))
    avg=(a+b+c)/3
    print("Average is ",avg)


avg()'''
#wap to input any three numbers and find out which one is the largest number using user defined functions

'''def largest_among_three():
    a=int(input("Enter a number "))
    b=int(input("Enter a number "))
    c=int(input("Enter a number "))
   
   
    if(a>b and a>c):
        print("Greatest Number is ",a)
    elif(b>a and c>a):
         print("Greatest Number is ",b)
    elif(c>a and c>b):
         print("Greatest Number is ",c)
    else:
        print("Invalid Numbers")

largest_among_three()'''


'''
WAP TO ACCEPT AGE OF 10 PEOPLE WORKING IN YOUR COMPANY AND COUNT THE NUMBER OF EMPLOYEES 
A. WHOSE AGE IS MORE THAN OR EQUAL TO 60
B. WHOSE AGE IS LESS THAN 35

USING FUNCTIONS
'''
'''def age_of_people_in_the_company():
    i=1
    while(i<=10):
        a[]
        i=i+1
'''
# WAP TO CHECK WHETHER A NUMBER IS PRIME OR NOT USING FUNCTIONS
def prime_or_not():
    a=int(input("Enter a number "))
    i=1
    c=0
    while(i<=a):
        if(a%i==0):
            c=c+1
        i=i+1
    if(c==2):
        print("The Number is prime")
    elif(c>2):
        print("The number is composite")
    else:
        print("The Number is neither prime nor composite")
prime_or_not()