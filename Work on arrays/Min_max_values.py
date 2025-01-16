def Min_Max(List):
    a=List[0]
    for i in List:
        if a>i:
            a=i
    b=List[0]
    for i in List:
        if b<i:
            b=i
    return (f"The min value of the  List is:{a}\nThe max value in the List is:{b}")

a=Min_Max((input("Write a list of your choice:")))
print(a)
