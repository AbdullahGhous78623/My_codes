class Node:
    def __init__(self, value):  # Corrected the function name and added colons
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Initially, the stack is empty, so the top is None

    def isempty(self):
        return self.top == None  # Checks if the stack is empty

    def push(self, value):
        new_node = Node(value)  # Creates a new node with the given value
        new_node.next = self.top  # Links the new node to the current top
        self.top = new_node  # Updates the top to the new node

    def traverse(self):
        temp = self.top  # Start from the top of the stack
        while temp != None:  # Traverse until the end of the stack
            print(temp.data)  # Print the data of the current node
            temp = temp.next  # Move to the next node
