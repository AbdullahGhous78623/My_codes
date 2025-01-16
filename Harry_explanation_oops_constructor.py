class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, my name is", self.name, "and I am ",self.age, "years old.")

# Create an object of the Person class
person1 = Person("John", 30)

# Access attributes
print(person1.name)  # Output: John
print(person1.age)   # Output: 30

# Call a method
person1.greet()  # Output: Hello, my name is John and I am 30 years old.
