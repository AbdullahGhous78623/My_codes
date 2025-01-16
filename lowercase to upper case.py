ch=input("Type:")
upper_case=""
for i in ch:
    if i>="a" and i<="z":

        upper=(chr(ord(i)-32))
        upper_case=upper_case+upper
    else:
        upper_case+=i

    



print(upper_case)