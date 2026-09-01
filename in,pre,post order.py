class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        return result

    def preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)
        return result


if __name__ == "__main__":
    tree = BinaryTree()

    book_titles = ["Mockingbird", "Beloved", "War and Peace",
                    "Dune", "Emma", "Frankenstein"]

    print("Inserting Book Titles into Binary Search Tree:")
    for title in book_titles:
        print(f" {title}")
        tree.insert(title)

    print("\nInorder Traversal:")
    print(tree.inorder(tree.root))

    print("\nPreorder Traversal:")
    print(tree.preorder(tree.root))

    print("\nPostorder Traversal:")
    print(tree.postorder(tree.root))
