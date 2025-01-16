# Sorting


# def BubbleSort(arr):

#     for i in range(0,len(arr)-1):
#         sorted=True

#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 sorted=False
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#         if sorted:
#             break 
#     return arr 
    



# arr=BubbleSort([2,67,5,34,35,3,423,2,4,2,24,5,35,3,5,2,5353])
# print(arr)


# def SelectionSort(arr):
#     for i  in range(len(arr)):
#         min_index=i
#         for j in range(i+1,len(arr)):
#             if arr[min_index]>arr[j]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr



# def InsertionSort(arr):
#     for i in range(1,len(arr)):
#         temp=arr[i]
#         j=i-1
#         while j>=0 and temp<arr[j]:
#             arr[j+1]=arr[j]

#             j-=1
#         arr[j+1]=temp

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else :
        pivot=arr[0]
        lesser=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:]if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
a=quick_sort([954,45,43264,32,5,35,235,645])
print(a)




