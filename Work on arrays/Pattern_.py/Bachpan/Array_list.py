import ctypes
class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    def __len__(self):
        return self.n
    def append(self,value):
        if self.n==self.size:
            self._resize(2*self.size)
        
        self.A[self.n]=value
        self.n=self.n+1
    def _resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B
    def __str__(self):
        result=''
        for i in range(self.n):
            result+=str(self.A[i])+ ","
        return "["+result[:-1]+"]"
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return "Index Error-Index out of range"
    def pop(self):
        if self.n==0:
            return "Empty list"
        print(self.A[self.n-1])
        self.n=self.n-1
    def clear(self):
        self.n=0
        self.size=1
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return "ValueError-Not in list"
    
# INSERT,DELETE,REMOVE
        

        
a=MeraList()
a.append(89)
a.append("hello")
a.append(87)
a.append(67)
print(len(a))
print(a[0])
print(a[100])
(a.clear())
print(a)

