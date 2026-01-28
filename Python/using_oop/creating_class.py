'''class Student:
    def __init__(self):
        print("Adding a new student  ")
    name="bipson"


s1=Student()
print(s1.name)'''


'''class Student:
    def __init__(self,fullname):
        self.name=fullname


s1=Student("Bipson")
print(s1.name)'''




class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

s1=Student("Bipson",98)
s2=Student("Bharat",87)
print(s1.name,s1.marks)
print(s2.name,s2.marks)