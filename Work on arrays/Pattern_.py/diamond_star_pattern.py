rows=int(input("Please type the integer number of your choice:"))
a=rows//2
for i in range(a+1):
    print((a-i)*" "+(i+1)*"*"+i*"*")
for j in range(a):
    print((j+1)*" "+(a-j)*"*"+(a-j-1)*"*")