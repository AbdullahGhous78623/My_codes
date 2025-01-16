def greet(fx):
    def mfx(self):
        print("Goodmorning")
        fx(self)
        print("Thanks for using this function")
    return mfx

class Decorator:
    @greet
    def hello(self):
        print("hello world")
    @staticmethod
    def sum(a,b):
        print(a+b)

# hello()
# greet(hello)()

obj=Decorator()
# obj.hello()


obj.sum(5,5)
Decorator.sum(5,8)



