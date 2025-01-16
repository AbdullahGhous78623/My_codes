class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        #Empty Linked List
        self.head = None
        #NO of nodes in the LL
        self.n = 0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
    def __str__(self):
        string=""
        reference=self.head
        while reference!=None:
            string=string+str(reference.data)+ "->"
            reference=reference.next
        return string[:-2]
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.n+=1
            return
        reference=self.head
        while reference.next!=None:
            reference=reference.next
        reference.next=new_node
        self.n+=1
    def insert_after(self,insert_element,insert_at):
        new_node=Node(insert_element)
        
        reference=self.head
        while reference!=None:
            if reference.data==insert_at:
                break
            

            reference=reference.next
        if reference!=None:
            reference1=reference.next
            reference.next=new_node
            reference.next.next=reference1
            self.n+=1
        else :
            return "Value not found!"
    def clear(self):
        self.head=None
        self.n=0
    def delete_head(self):
        if self.head==None:
            return "Empty Linked List"
        self.head=self.head.next
        self.n-=1
    def pop(self):
        if self.head==None:
            return "Empty Linked List"
        reference=self.head
        # kya linked list me ek item hai
        if reference.next==None:
             return self.delete_head()
        while reference.next.next!=None:
            reference=reference.next
        reference.next=None
        self.n-=1
    def remove(self,value):
        if self.head==None:
            return "Empty LL"
        if self.head.data==value:
            return self.delete_head()
        reference=self.head
        while reference.next!=None:
            if reference.next.data==value:
                
                break
            reference=reference.next
        if reference.next!=None:
            reference.next=reference.next.next
        else:
            return "Item not found!"   
    def search(self,value):
         
        reference=self.head
        count=0

        while reference!=None:
            
            if reference.data==value:
                return count
            reference=reference.next
            count+=1
        return "Not found"
    def __getitem__(self,index):
        reference=self.head
        count=0
        while reference!=None:
            if count==index:
                return reference.data
            reference=reference.next
            count+=1
        return "Index Out of range"
    
                
            
          

    
obj=LinkedList()
obj.insert_head(1)
obj.insert_head(2)
obj.insert_head(3)
obj.insert_head(4)
obj.insert_head(5)
print(obj)
print(obj.insert_after(8,200))
print(obj)



