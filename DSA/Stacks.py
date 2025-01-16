class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def peek(self):
         if not self.isempty():
            return self.top.data
         else:
            return "Stack is Empty"
    def pop(self):
        if self.isempty():
            return "Stack is Empty" 
        else:
            popped_value=self.top.data
            self.top=self.top.next 
            return popped_value       
    def __str__(self):
        if self.isempty():
            return "Stack is Empty"
        reference=self.top
        String=""
        
        while reference!=None:
            String=String+str(reference.data)+"->"
            reference=reference.next
        return String[:-2]
        

stack=Stack()

stack.push(4)
stack.push(5)
stack.push(9)

print(stack)
print(stack.peek())




