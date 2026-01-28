try :
    a=int(input("Enter a number: "))

except ValueError :
    print("Please enter a number")

except ZeroDivisionError:
    print("Number Can't be divided by zero !!! ")
