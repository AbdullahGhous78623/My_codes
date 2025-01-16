from collections import Counter

Input ="heellooo" 

for i,j in Counter(Input).items():
    if j>1:
        print(i,end=" ")