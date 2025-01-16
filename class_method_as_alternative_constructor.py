class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        
        return cls(string.split("-")[0],string.split("-")[1])

# Creating an instance using the regular constructor
e1 = Employee("Harry", 12000)
print(e1.name)    # Outputs: Harry
print(e1.salary)  # Outputs: 12000

# Creating an instance using the class method
string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)    # Outputs: John
print(e2.salary)  # Outputs: 12000


a="Abdullah-Niamatullah-12"
print(a.split("-")[0])





