rows=int(input("Select the number:"))
a=rows//2
for i in range(a+1):
    print((a-i)*" "+(i+1)*"*")
for j in range(a):
    print((j+1)*" "+(a-j)*"*")