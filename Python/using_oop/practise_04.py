class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def show_details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Role: ",self.role)
        print("Department: ",self.dept)
        print("Salary: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "Tech", "100000")
        
        
eng1=Engineer("Biperson",18)
eng1.show_details()

