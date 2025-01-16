def String(Anagram):
    j=""
    for i in Anagram:
        if i>="A" and i<="Z":
            i=chr(ord(i)+32)
            j+=i
        else:
            j+=i
    

    
    es=""
    for nc  in range(97,123):
    
    
        for l in j:
            if ord(l)==nc:
                es+=l
    return es
        
a=String(input("Type:")) 
b=String(input("Type:"))   
   


        


if a==b:
    print("The string is anagram")
else:
    print("The string is not anagram")

            

