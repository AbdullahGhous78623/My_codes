class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        # Empty linked list
        self.head=None
        # no of nodes in the LL
        self.n=0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1


L=LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.insert_head(5)


print(len(L))