a=[2,4,5,7,8,4,5]
b=[]

for i in range(1,len(a)+1):
    b+=[a[-i]]
print(b)