from collections import Counter

def isValid( s):
    dictionary={")":"(","]":"[","}":"{"}
    dictionary=Counter(dictionary)
    Output=False
    if len(s)%2==0:
        i=0
        
        for _ in range(len(s)//2):
            if s[i]==dictionary[s[i+1]]:
                i+=2
                Output=True
            elif s[i]==dictionary[s[-i-1]]:
                i+=1
                Output=True
            else:
                if s[i] in dictionary.keys():
                    i+=1
                    Output=False
    return Output


a=isValid("(([]){})")
print(a)