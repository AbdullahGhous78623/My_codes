list=[2,4,1,4,5,6,7,4,6,3,0.1]

list1=[]
for i in range (0,len(list)):
    maximum=max(list)
    list1+=[maximum]
    list.remove(maximum)
print(list1)

def bubble_sort(arr):
    for i in range (len(arr)):
        sorted=0
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sorted=1
        if sorted==0:
            break

        
    return arr


a=bubble_sort([27,32,633,554,33,65,2,56,3,56])
print(a)

def selection_sort(arr):
    for i in range(len(arr)):
        
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

a=selection_sort([23,2,34,45,33,23,5])
print(a)

