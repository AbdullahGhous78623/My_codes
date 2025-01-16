class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.front is None:
            self.front=new_node
            self.rear=self.front
        else:
            self.rear.next=new_node
            self.rear=new_node
    def is_empty(self):
        return self.front==None
    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        dequeue_val=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return dequeue_val
    def size(self):
        pass
    def peek_front(self):
        pass
        
    def traverse(self):
        reference=self.front
        while reference != None:
            print(reference.data,end=" ")
            reference=reference.next


q=Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(8)
q.enqueue(90)
print(q.traverse())


            
