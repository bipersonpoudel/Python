class Student:
   
    name="bipson"
    def change_name(self,name):
        Student.name=name

p1=Student()
p1.change_name("Biperson")
print(p1.name)
print(Student.name)