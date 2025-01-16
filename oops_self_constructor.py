class Greeting:
    college="Delhi Public School"
    id=1234
    def __init__(self,name,age,occupation):
        self.o=name
        self.p=age
        self.q=occupation
        
    def info(self):
        print("My name is:",self.o)
    
    

a = Greeting("harry",24,"HR")



print(a.o)
print(a.p)
print(a.q)
print(a.id)
Greeting.info(a)
a.info()
