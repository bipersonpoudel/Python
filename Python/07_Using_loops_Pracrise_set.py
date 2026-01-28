#wap to print a multiplication table of a entered number
'''a=int(input("Enter the number "))
for i in range(11):
    m=a*i
    print(a, "*", i, "=",m)
#wap to greet all the person names stored in a list 'l' and which starts with s
l=["biperon","sankar","samikshya","sandhya","bipson"]
for i in l:
    if (i.startswith("s")) :
        print("Hello,",i ,"Welcome")

# Attempt question no 1 with while loop
i=1
a=int(input("Enter a number  "))
while(i<=10):
    print(a ,"*", i, "=",a*i)
    i=i+1
#wap to find whether a given number is prime or not
a=int(input("Enter a number "))

c=0
for i in range(a+1):
 
         
        
    if(a%2==0):
        c=c+1

if(c>2):
    print("The number is composite")

elif(c==2):
    print("The number is prime")
else:
    print("The number is neither prime nor composite")

#wap to find the sum of first n natural numbers using while loop
n=int(input("Enter a number  "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1

print("Sum is ",sum)
# wap to find factorial of given number using for lopp
a=int(input("Enter a number "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("Factorial is ",fact)'''
'''Wap to print following star pattern
  *
 ***
***** for n=3

'''
for i in range(3):
    for i in range(1,5,2):
        print("*")