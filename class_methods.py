class Employee:
    company = "Apple"  

    def show(self):
        
        print(f"The name is {self.name} and the company is {self.company}")

    
    def Company(cls, newCompany):
        # Class method that changes the class attribute 'company'
        cls.company = newCompany


e1 = Employee()
e1.name = "Harry"  


e1.show()
Employee.company="tesla"


e1.Company("Tesla")


e1.show()


print(Employee.company)
