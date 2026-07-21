class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
def display(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next

print("None")

print("\n original linked list")
display(head)

print("\n Insert_beginning")
new_node=Node(5)
new_node.next=n1
n1=new_node
display(n1)

print("\n insert_middle")
new_node=Node(25)
temp=n1
while temp.data!=20:
    temp=temp.next
    new_node.next=temp.next
temp.next=new_node
display(n1)

print("\n insert_end")
new_node=Node(40)
temp=n1
while temp.next:
    temp=temp.next
temp.next=new_node
display(n1)

print("\n Deletion_Beginning")
n1=n1.next
display(n1)

print("\n Deletion_middle")
temp=n1
while temp.next.data!=25:
    temp=temp.next
temp.next=temp.next.next
display(n1)

print("\n Deletion_End")
temp=n1
while temp.next.next:
    temp=temp.next
temp.next=None
display(n1)
