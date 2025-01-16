class MyClass:
   

    def __init__(self, value):
        self.value = value


    @classmethod
    def create_instance(cls, value):
        # Factory method that creates an instance of MyClass
        return cls(value)




obj = MyClass.create_instance(42)
print(obj.value)  # Output: 42
