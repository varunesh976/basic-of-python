class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top is None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.is_empty():
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

stack=stack()
n=int(input("Enter the number:"))
for i in range(n):
    value=int(input("Enter element:"))
    stack.push(value)
print("peek:",stack.peek())
while not stack.is_empty():
    print("peek:",stack.peek())
    print("pop:",stack.pop())
    print("Is Empty:",stack.is_empty())
