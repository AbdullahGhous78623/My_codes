
class Solution(object):
    def compressedString(self, word):
        string=""
        k=None
        index=-1
        
        for i in word:
            index+=1
            if k==i:
                
                continue
            count=0
            
            
            for j in word[index:]:
                if i==j :
                    count+=1
                else:
                    break
            if count>9:
                count1=count//9 
                for k in range(count1):
                    string=string+"9"+i
                if count%9>0:
                    string=string+str(count%9)+i
            else:
                string=string+str(count)+i
            k=i
               
        return string
    


        


        