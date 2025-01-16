rows=int(input("write the number of rows:"))


for i in range(rows):
    if i==0:
        print((rows-i-1) * " "+ (i+1) * "*")
    elif i==rows-1:
        print((2*rows-1) * "*")
    else:
        print((rows-i-1) * " "+ "*" + (2*i-1) * " " + "*")
