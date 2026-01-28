class Complex:
    def __init__(self, real,img):
        self.real=real
        self.img=img

    def show_number(self):
        print(self.real ,"i + ",self.img,"j")

    def add(self,num1,num2):
        newreal=num1.real +num2.real
        newimg=num1.img+num2.img
        print("The addition of the complex number is :")
        print(newreal,"i +",newimg,"j")

num1=Complex(1,2)
num1.show_number()
num2=Complex(3,4)        
num2.show_number()
num1.add(num1,num2)