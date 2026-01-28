# create a student calss that takes naem and marks of 3 subject
#  as argument in constructor. then a method to print average
 

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
       
    def average(self):
       sum=0
       for val in self.marks:
           sum += val
       print("Hello",self.name,"Your Average is :",sum/3) 
    
   

student1=Student("Bipson",[98,91,93])     
student1.average()