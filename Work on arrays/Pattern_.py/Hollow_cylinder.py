rows = int(input("Type the row:"))
column=int(input("Type the column:"))
for i in range(rows):
    if i==0 or i==rows-1:
        print(column*"*")
    else:
        print("*"+(column-2)*" "+"*")