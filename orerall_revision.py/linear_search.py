class LinearSearch:
    def linear_search(self,n,target):
        for i in n:
            if i==target:
                return f"Element {target} found!"
        else:
            return f"Element {target} not found!"


a=list(map(int,input("Type a list:").split()))
target=int(input("Type the element you want to find:"))
obj=LinearSearch()
b=obj.linear_search(a,target)
print(b)