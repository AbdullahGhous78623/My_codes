class Person:
    School_name="Delhi public school"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.id=2
        
    def info(self):
            return (f'The name of the student is {self.name}, The age of the student is {self.age}, The id of the student is {self.id}')
    

obj1=Person("Abdullah",24)
obj2=Person("niamatullah",21)
Person.School_name="Doon public School"

print(obj1.School_name)
print(Person.School_name)




# print(obj2.School_name)
# print(obj1.name)
# print(obj2.name)
# obj1.School_name="doon public School"
# print(obj1.School_name)
# print(obj1.id)

# a=obj1.info()
# b=obj2.info()
# print(a,b, sep="\n")



