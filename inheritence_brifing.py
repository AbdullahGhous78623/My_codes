class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

# Create an instance of Employee
e1 = Employee("Rohan Das", 400)
e1.showDetails()  # Output: The name of Employee: 400 is Rohan Das

# Create an instance of Programmer
e2 = Programmer("Harry", 4100)
e2.showDetails()  # Output: The name of Employee: 4100 is Harry
e2.showLanguage()  # Output: The default language is Python

