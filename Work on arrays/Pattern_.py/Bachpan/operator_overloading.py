class operator_overloading:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def __add__(self):
        return()


v1=operator_overloading(2,3,4)
v2=operator_overloading(5,6,7)

v3=v1+v2