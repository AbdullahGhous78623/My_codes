def toggle():

    ch=input("Type:")
    upper_case=""
    for i in ch:
        if i>="a" and i<="z":

            upper=(chr(ord(i)-32))
            upper_case=upper_case+upper
        elif  i>="A"and i<="Z":
            lower=chr(ord(i)+32)
            upper_case=upper_case+lower
        

        else:
            upper_case+=i

    



    print(upper_case)

toggle()