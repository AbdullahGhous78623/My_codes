list_=[32,3,44,2,45,25,256,356,2,245,24,654,3]

for j in range(len(list_)-1):
    swapped=False
    for i in range(len(list_)-1-j):
        if list_[i]>list_[i+1]:
            list_[i],list_[i+1]=list_[i+1],list_[i]
            swapped=True
    if not swapped:
        break

print(list_)

 