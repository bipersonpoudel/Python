class programmer:
    company="Microsoft"
    def __init__(self, name, salary, pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode


p=programmer("Biperson",100000,123332)
q=programmer("Mahesh",50000,234252)
print(p.name,p.salary,p.pincode,p.company)
print(q.name,q.salary,q.pincode,q.company)

        