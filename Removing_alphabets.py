string=input("Type:")
newstring=""
for i in string:
    if (i >="a" and i<="z" ) or(i>="A" and i<="Z"):
        pass
    else:
        newstring+=i
print(newstring)
