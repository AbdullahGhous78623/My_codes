import math
a=[43,56,54,61,56,43,65,78,34,42,90,43]
e1=a[:len(a)//2]
e2=[]
for i in range(0,(len(a)//2)):
    max_value=-math.inf
    for j in e1:
        if max_value<j:
            max_value=j
    e2+=[max_value]
    e1.remove(max_value)
e3=a[len(a)//2:]

e4=[]
for k in range((len(a)//2),len(a)):
    min_value=math.inf
    for l in e3:
        if min_value>l:
            min_value=l
    e4+=[min_value]
    e3.remove(min_value)
print(e4)
print(e2)

print(e2+e4)           



