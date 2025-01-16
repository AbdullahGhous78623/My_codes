import math

a=[21,32,35,65,46,21]


b=[]
for i in range(len(a)):
    min_value=math.inf
    for j in a:
        if min_value>j:
            min_value=j
    b+=[min_value]
    a.remove(min_value)


c=b[len(b)//2:]
d=b[:len(b)//2]


e=sorted(c, reverse=True)
print(d+e)