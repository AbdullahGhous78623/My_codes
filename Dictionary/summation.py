Input = {"a": 100, "b":200, "c":300}
sum=0
for i in Input.values():
    sum+=i
    

print(sum)

Input = {"a": 100, "b":200, "c":300}
sum=0
for i in Input:
    sum+=Input[i]

print(sum)
Input = {"a": 100, "b":200, "c":300}
sum=0
for i in Input.keys():
    sum+=Input[i]

print(sum)
Input = {"a": 100, "b":200, "c":300}
sum=0
for _,j in Input.items():
    sum+=j

print(sum)
Input = {"a": 100, "b":200, "c":300}
sum=0
for i in Input:
    sum+=Input.get(i)

print(sum)
    