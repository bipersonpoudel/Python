'''#wap to print greatest of 3 numbers using func
def great_among_three():
    a=int(input("Enter a number "))
    b=int(input("Enter a number "))
    c=int(input("Enter a number "))
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        print("Invalid Numbers")

print("Greatest number is ",great_among_three())
#wap to convert celcius into fahrenheit usng fucntions
def conversion_of_celcius_into_fahrenheit():
    c=int(input("Enter the temperature in celcius "))
    f=((9*c)/5)+32
    print("The temperature in fahrenheit is ",f)
    return 0

conversion_of_celcius_into_fahrenheit()'''
#wap to print sum of first n natural numbers using recursive
a=int(input("Enter a number "))
def sum(a):
    if (a==0):
        return 0
    elif (a==1):
        return 1
    else :
        return  sum(a-1) + a
print("Sum is ", sum(a))