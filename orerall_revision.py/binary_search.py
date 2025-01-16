list_=[32,3,44,2,45,25,256,356,2,245,24,654,3]

for j in range(len(list_)-1):
    swapped=False
    for i in range(len(list_)-1-j):
        if list_[i]>list_[i+1]:
            list_[i],list_[i+1]=list_[i+1],list_[i]
            swapped=True
    if not swapped:
        break
element=int(input("Type a number:"))
n1=0
n2=len(list_)-1
print(list_)
while n2>=n1:
    
    mid=(n1+n2)//2
    if list_[mid]==element:
        print(f"Element is at index {(n1+n2)//2}")
        break
    elif element>list_[mid]:
        n1=mid+1
    elif element<list_[mid]:
        n2=mid-1
else:
    print("Element not found!")



       

