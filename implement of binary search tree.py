class Node:
    def __init__(self, visitor_name, entry_time, purpose):
        self.visitor_name = visitor_name
        self.entry_time = entry_time
        self.purpose = purpose
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a log entry
    def insert(self, visitor_name, entry_time, purpose):
        new_node = Node(visitor_name, entry_time, purpose)

        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.visitor_name.lower() < current.visitor_name.lower():
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    # Search for a visitor
    def search(self, visitor_name):
        return self._search(self.root, visitor_name)

    def _search(self, current, visitor_name):
        if current is None:
            return None

        if current.visitor_name.lower() == visitor_name.lower():
            return current

        elif visitor_name.lower() < current.visitor_name.lower():
            return self._search(current.left, visitor_name)

        else:
            return self._search(current.right, visitor_name)

    # Find minimum node
    def find_min(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    # Delete a log entry
    def delete(self, visitor_name):
        self.root = self._delete(self.root, visitor_name)

    def _delete(self, root, visitor_name):
        if root is None:
            return root

        if visitor_name.lower() < root.visitor_name.lower():
            root.left = self._delete(root.left, visitor_name)

        elif visitor_name.lower() > root.visitor_name.lower():
            root.right = self._delete(root.right, visitor_name)

        else:
            # Node with one child or no child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.find_min(root.right)

            root.visitor_name = temp.visitor_name
            root.entry_time = temp.entry_time
            root.purpose = temp.purpose

            root.right = self._delete(root.right, temp.visitor_name)

        return root

    # Inorder Traversal
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print("Name:", root.visitor_name,
                  "| Time:", root.entry_time,
                  "| Purpose:", root.purpose)
            self._inorder(root.right)

    # Postorder Traversal
    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print("Name:", root.visitor_name,
                  "| Time:", root.entry_time,
                  "| Purpose:", root.purpose)

    # Count total entries
    def count_entries(self):
        return self._count(self.root)

    def _count(self, root):
        if root is None:
            return 0

        return 1 + self._count(root.left) + self._count(root.right)


# Main Program
bst = BinarySearchTree()

while True:
    print("\n--- LOG BOOK MANAGEMENT ---")
    print("1. Insert Log Entry")
    print("2. Delete Log Entry")
    print("3. Search Log Entry")
    print("4. Display Entries (Inorder)")
    print("5. Display Entries (Postorder)")
    print("6. Count Total Entries")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Visitor Name: ")
        time = input("Enter Entry Time: ")
        purpose = input("Enter Purpose: ")

        bst.insert(name, time, purpose)
        print("Log entry inserted successfully!")

    elif choice == 2:
        name = input("Enter Visitor Name to delete: ")
        bst.delete(name)
        print("Log entry deleted successfully!")

    elif choice == 3:
        name = input("Enter Visitor Name to search: ")
        result = bst.search(name)

        if result:
            print("\nVisitor Found!")
            print("Name:", result.visitor_name)
            print("Entry Time:", result.entry_time)
            print("Purpose:", result.purpose)
        else:
            print("Visitor not found!")

    elif choice == 4:
        print("\n--- Log Entries in Sorted Order ---")
        bst.inorder()

    elif choice == 5:
        print("\n--- Log Entries in Postorder ---")
        bst.postorder()

    elif choice == 6:
        print("Total Log Entries:", bst.count_entries())

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

