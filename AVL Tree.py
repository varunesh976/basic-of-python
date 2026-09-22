
 
class AVLNode:
    def __init__(self, enrollment_id, student_name, course):
        self.enrollment_id = enrollment_id
        self.student_name = student_name
        self.course = course
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

    def update_height(self, node):
        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )


    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        self.update_height(y)
        self.update_height(x)

        return x


    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, node, enrollment_id, student_name, course):

        if node is None:
            return AVLNode(enrollment_id, student_name, course)

        if enrollment_id < node.enrollment_id:
            node.left = self.insert(
                node.left,
                enrollment_id,
                student_name,
                course
            )

        elif enrollment_id > node.enrollment_id:
            node.right = self.insert(
                node.right,
                enrollment_id,
                student_name,
                course
            )

        else:
            print("Enrollment ID already exists!")
            return node

   
        self.update_height(node)

    
        balance = self.get_balance(node)

        if balance > 1 and enrollment_id < node.left.enrollment_id:
            return self.right_rotate(node)

     
        if balance < -1 and enrollment_id > node.right.enrollment_id:
            return self.left_rotate(node)

    
        if balance > 1 and enrollment_id > node.left.enrollment_id:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

    
        if balance < -1 and enrollment_id < node.right.enrollment_id:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

 
    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

 
    def delete(self, node, enrollment_id):

        if node is None:
            return node

        if enrollment_id < node.enrollment_id:
            node.left = self.delete(node.left, enrollment_id)

        elif enrollment_id > node.enrollment_id:
            node.right = self.delete(node.right, enrollment_id)

        else:
           
            if node.left is None:
                return node.right

      
            elif node.right is None:
                return node.left

       
            temp = self.min_value_node(node.right)

            node.enrollment_id = temp.enrollment_id
            node.student_name = temp.student_name
            node.course = temp.course

            node.right = self.delete(
                node.right,
                temp.enrollment_id
            )

     
        self.update_height(node)

        balance = self.get_balance(node)

     
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

 
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

      
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

    
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

 
    def search(self, node, enrollment_id):

        if node is None:
            return None

        if enrollment_id == node.enrollment_id:
            return node

        if enrollment_id < node.enrollment_id:
            return self.search(node.left, enrollment_id)

        return self.search(node.right, enrollment_id)


    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)

            print(
                f"Enrollment ID: {node.enrollment_id} | "
                f"Student: {node.student_name} | "
                f"Course: {node.course}"
            )

            self.inorder(node.right)


    def count(self, node):

        if node is None:
            return 0

        return (
            1
            + self.count(node.left)
            + self.count(node.right)
        )



avl = AVLTree()
root = None

while True:

    print("\n========== STUDENT ENROLLMENT SYSTEM ==========")
    print("1. Insert Enrollment Record")
    print("2. Delete Record by Enrollment ID")
    print("3. Search for Student Enrollment")
    print("4. Display All Enrollment Records")
    print("5. Count Total Enrollments")
    print("6. Exit")
    print("===============================================")

    choice = input("Enter your choice: ")

   
    if choice == "1":

        try:
            enrollment_id = int(input("Enter Enrollment ID: "))
            student_name = input("Enter Student Name: ")
            course = input("Enter Course Name: ")

       
            if avl.search(root, enrollment_id) is not None:
                print("Enrollment ID already exists!")
            else:
                root = avl.insert(
                    root,
                    enrollment_id,
                    student_name,
                    course
                )
                print("Enrollment record inserted successfully.")

        except ValueError:
            print("Please enter a valid numeric Enrollment ID.")


    elif choice == "2":

        try:
            enrollment_id = int(
                input("Enter Enrollment ID to delete: ")
            )

            if avl.search(root, enrollment_id) is None:
                print("Enrollment record not found.")
            else:
                root = avl.delete(root, enrollment_id)
                print("Enrollment record deleted successfully.")

        except ValueError:
            print("Please enter a valid numeric Enrollment ID.")

    elif choice == "3":

        try:
            enrollment_id = int(
                input("Enter Enrollment ID to search: ")
            )

            result = avl.search(root, enrollment_id)

            if result is not None:
                print("\nEnrollment Found!")
                print("-----------------------------")
                print("Enrollment ID :", result.enrollment_id)
                print("Student Name  :", result.student_name)
                print("Course        :", result.course)
            else:
                print("Enrollment record not found.")

        except ValueError:
            print("Please enter a valid numeric Enrollment ID.")

    elif choice == "4":

        if root is None:
            print("No enrollment records available.")
        else:
            print("\n===== ENROLLMENT RECORDS =====")
            print("(Sorted by Enrollment ID)")
            avl.inorder(root)

 
    elif choice == "5":

        total = avl.count(root)

        print("\nTotal Enrollments:", total)

  
    elif choice == "6":

        print("Thank you for using the Student Enrollment System!")
        break

    else:
        print("Invalid choice. Please enter 1-6.")
