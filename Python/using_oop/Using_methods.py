# Creating Class
class Student:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("Hello,",self.name)


#Creating Object
student1=Student("Bipson")
student1.hello()