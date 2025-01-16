class Employee:
    companyName = "Apple"  # Class attribute
    no_of_employees=0

    def __init__(self, name):
        self.name = name  # Instance attribute
        self.raise_amount = 0.02  # Instance attribute
        Employee.no_of_employees += 1  # Class-level operation (requires initialization)

    
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

    

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3  # Modify instance attribute
emp1.companyName = "Apple India"  # Modify class attribute via instance

# Show details of emp1
emp1.showDetails()  # Error in method: should be using class method or instance method correctly
Employee.companyName="Google"
print(Employee.companyName)
# Create another instance
emp2 = Employee("Rohan")
emp2.companyName = "Nestle"  # Modify class attribute via instance

# Show details of emp2
emp2.showDetails()  # Error in method: should be using class method or instance method correctly
