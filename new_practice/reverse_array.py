arr=[43,56,6,564,7,64,754,4443]


for i in range(len(arr)//2):
    arr[i],arr[-i-1]=arr[-i-1],arr[i]


print(arr)
