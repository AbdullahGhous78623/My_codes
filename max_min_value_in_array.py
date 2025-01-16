list=[32,43,65,76,89,75,45]
value1=list[0]
value2=list[0]
for i in list:
    if value1<i:
        value1=i
    elif value2>i:
        value2=i
print("maximum value:",value1,"and","minimum value:",value2)
