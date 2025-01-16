double=lambda x:x*2

print(double(9))
avg=lambda x,y,z:(x+y+z)/3

print(avg(8,5,4))

def cube(q):
    return q**3

def func(x,cube,value):
    return x+cube(value)



a=func(3,cube,3)
print(a)

function=lambda x,cube,value:x+cube(value)

print(function(3,cube,3))