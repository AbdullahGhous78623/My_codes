class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.n
    def insert_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
    def __str__(self):
        str=""
        reference=self.head
        while reference!=None:
            str+=f"{reference.data}"+"->"
            reference=reference.next
        return str[:-2]
    def append(self,data):
        new_node=Node(data)
        self.n+=1
        reference=self.head
        if self.head==None:
            self.head=new_node
            
            return
        
        while reference.next:
            reference=reference.next
        reference.next=new_node
    def insert_after(self,after,data):
        new_node=Node(data)
        reference=self.head
        while reference!=None:
            
            if reference.data==after:
                break
            reference=reference.next
        if reference==None:
            print(f"Value {after} not found in the linked list.") 
        else:
            new_node.next=reference.next
            reference.next=new_node
            self.n+=1
    def clear(self):
        self.head=None
        self.n=0


L=LinkedList()
L.insert_middle(8,12)


    





