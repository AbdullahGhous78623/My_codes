def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)


a=power(2,3)
print(a)