rows=int(input("type the number of rows:"))

for i in range(rows):
    print((rows-i-1)*" "+(i+1)*"*"+i*"*")