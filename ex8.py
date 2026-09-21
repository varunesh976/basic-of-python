class Node:
    def __init__(self, enrollment_id, name):
        self.enrollment_id = enrollment_id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    def insert(self, root, enrollment_id, name):

        if root is None:
            return Node(enrollment_id, name)

        if enrollment_id < root.enrollment_id:
            root.left = self.insert(root.left, enrollment_id, name)

        elif enrollment_id > root.enrollment_id:
            root.right = self.insert(root.right, enrollment_id, name)

        else:
            print ("Enrollment ID already exists.")
            return root

        root.height = 1 + max(self.height(root.left),
                               self.height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and enrollment_id < root.left.enrollment_id:
            return self.right_rotate(root)

        if balance < -1 and enrollment_id > root.right.enrollment_id:
            return self.left_rotate(root)

        if balance > 1 and enrollment_id > root.left.enrollment_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and enrollment_id < root.right.enrollment_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, enrollment_id):

        if root is None:
            return root

        if enrollment_id < root.enrollment_id:
            root.left = self.delete(root.left, enrollment_id)

        elif enrollment_id > root.enrollment_id:
            root.right = self.delete(root.right, enrollment_id)

        else:

            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)

            root.enrollment_id = temp.enrollment_id
            root.name = temp.name

            root.right = self.delete(root.right,
                                     temp.enrollment_id)

        root.height = 1 + max(self.height(root.left),
                               self.height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, enrollment_id):

        if root is None:
            return None

        if enrollment_id == root.enrollment_id:
            return root

        if enrollment_id < root.enrollment_id:
            return self.search(root.left, enrollment_id)

        return self.search(root.right, enrollment_id)

    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)

            print root.enrollment_id, "-", root.name

            self.inorder(root.right)

    def count(self, root):

        if root is None:
            return 0

        return 1 + self.count(root.left) + self.count(root.right)


tree = AVLTree()
root = None

while True:

    print "\n--- Student Enrollment Management ---")
    print ("1. Insert Enrollment Record")
    print ("2. Delete Record by Enrollment ID")
    print ("3. Search Student Enrollment")
    print ("4. Display Records Sorted by Enrollment ID")
    print ("5. Count Total Enrollments")
    print ("6. Exit")

    choice = int(raw_input("Enter your choice: "))

    if choice == 1:

        enrollment_id = int(raw_input("Enter Enrollment ID: "))
        name = raw_input("Enter Student Name: ")

        root = tree.insert(root, enrollment_id, name)

        print ("Enrollment record inserted successfully.")

    elif choice == 2:

        enrollment_id = int(
            raw_input("Enter Enrollment ID to delete: ")
        )

        if tree.search(root, enrollment_id) is None:
            print ("Enrollment record not found.")
        else:
            root = tree.delete(root, enrollment_id)
            print ("Enrollment record deleted successfully.")

    elif choice == 3:

        enrollment_id = int(
            raw_input("Enter Enrollment ID to search: ")
        )

        result = tree.search(root, enrollment_id)

        if result is not None:
            print ("Student Found")
            print ("Enrollment ID:", result.enrollment_id)
            print ("Student Name:", result.name)
        else:
            print ("Student enrollment not found.")

    elif choice == 4:

        if root is None:
            print ("No enrollment records available.")
        else:
            print ("\nEnrollment Records:")
            tree.inorder(root)

    elif choice == 5:

        print ("Total Enrollments:", tree.count(root))

    elif choice == 6:

        print ("Program terminated.")
        break

    else:

        print ("Invalid choice.")
