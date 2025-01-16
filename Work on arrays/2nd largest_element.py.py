import math
List=[23,43,54,67,21]
a=List[0]

for i in List:
    if a>i:
        a=i

b=math.inf


for i in List:
    if b>i and i!=a:
        b=i
print(b)