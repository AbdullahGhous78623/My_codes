# def greet (fx):
#     def mfx():
#         print("Goodmorning")
#         fx()
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("hello world")


# hello()

def greet (fx):
    def mfx(*args,**kwargs):
        print("Goodmorning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def add(a,b):
    print(a+b)



add()



