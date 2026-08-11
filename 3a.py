stack = []
size = 5

def push():
    if len(stack) == size:
        print("Stack Overflow")
    else:
        item = input("Enter book title: ")
        stack.append(item)
        print("Book added.")

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Removed book:", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top book:", stack[-1])

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        print("Stack:", stack)
    elif ch == 5:
        break
    else:
        print("Invalid choice")
