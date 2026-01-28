a=int(input("Enter a number "))
def fact(a):
   if(a==0 or a==1):
      return 1
 
   return a*fact(a-1)

b=fact(a) 
print(b)