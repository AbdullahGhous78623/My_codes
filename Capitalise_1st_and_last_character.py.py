String=input("Type:")
New_String=""
if len(String)>0:
    
    
    if (String[0]>="a" and String[0]<="z"):
        Cap_Elemenmt=chr(ord(String[0])-32)
        New_String+=Cap_Elemenmt
    else:
        New_String+=String[0]

    for i in String[1:(len(String)-1)] :
    
        New_String+=i
    if len(String)>1:
        
        if (String[-1]>="a" and String[-1]<="z"):
            Cap_Elemenmt=chr(ord(String[-1])-32)
            New_String+=Cap_Elemenmt
        else:
            New_String+=String[-1]

print(New_String)
