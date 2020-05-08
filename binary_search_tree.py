class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        node = self.root
        inserted = False
        while not inserted:
            if new_val > node.value:
                if node.right is None:
                    node.right = Node(new_val)
                    inserted = True
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = Node(new_val)
                    inserted = True
                else:
                    node = node.left

    def search(self, find_val):
        node = self.root
        while node:
            if node.value == find_val:
                return True
            elif find_val < node.value:
                node = node.left
            else:
                node = node.right
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(6)

# Check search
# Should be True
print(tree.search(12))
# Should be False
print(tree.search(6))
