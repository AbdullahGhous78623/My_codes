def onlystr(str):
    str=str.lower()
    es=""
    for i in str:
        if i.isalpha():
            
            es+=i
    return es

a=onlystr("prep@insta")
b=onlystr("PREp%$$insta")

if a==b:
    print("String are same after removal of wildcard")
else:
    print("Dissimilar string")

