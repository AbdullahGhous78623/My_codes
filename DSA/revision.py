class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

        self.n=self.n+1
    def __str__(self):
        current=self.head
        result=""
        while current !=None:
            result=result+str(current.data)+"->"
            current=current.next
        return result[:-2]

a=LinkedList()
a.insert_head(2)
a.insert_head(4)
a.insert_head(5)
a.insert_head(3)
a.insert_head(2)
a.insert_head(4)
a.insert_head(5)
a.insert_head(3)
a.insert_head(2)
a.insert_head(4)
a.insert_head(5)
a.insert_head(3)
a.insert_head(2)
a.insert_head(4)
a.insert_head(5)
a.insert_head(3)
a.insert_head(2)
a.insert_head(4)
a.insert_head(5)
a.insert_head(3)

print(a)
print(len(a))



        





