class employee:
    name="biperson"
    language="python"
    salary=100000
    def __init__(self):
        print("I am creating an object")

biperson=employee()
biperson.age=18
print(biperson.language,biperson.name,biperson.salary,biperson.age)