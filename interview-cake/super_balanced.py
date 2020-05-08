"""
In this problem, we were asked to write a method that will identify
whether a binary tree is "superbalanced", which the problem defines as
a tree with no pair of leaves being more than 1 depth apart.
"""


class Node(object):
    """
    This class is template for creating a binary tree node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def insert_left(self, value):
        self.left = Node(value)
        return self.left

    def insert_right(self, value):
        self.right = Node(value)
        return self.right


class SuperBalancedTree(object):
    """
    This class is template for creating a tree. It includes a method for
    checking if it is "superbalanced"
    """

    def __init__(self, root_value):
        self.root = Node(root_value)
        self.min_depth = None
        self.max_depth = None
        self.nodes_and_depths_for_review = []

    def __str__(self):
        return f"Min_Depth: {self.min_depth}; Max_Depth: {self.max_depth}"

    def _set_min_max_depth(self, node_depth):
        if self.min_depth is None and self.max_depth is None:
            self.min_depth = node_depth
            self.max_depth = node_depth
        else:
            self.min_depth = min(self.min_depth, node_depth)
            self.max_depth = max(self.max_depth, node_depth)

    def is_super_balanced(self):
        # Returns True if a tree is "superbalanced", meaning:
        #   - the difference between any pair of leaves is
        #       no greater than 1.

        if self.root is None:
            return True

        # add root,depth tuple to list of nodes for review
        self.nodes_and_depths_for_review.append((self.root, 0))

        # Iterate while there are (nodes, depth) tuples remaining to review
        while len(self.nodes_and_depths_for_review) > 0:
            node_and_depth = self.nodes_and_depths_for_review.pop()
            node = node_and_depth[0]
            depth = node_and_depth[1]

            # if node is a leaf, have we viloated the "superbalanced" property?
            if node.is_leaf():
                self._set_min_max_depth(depth)
                if((self.max_depth - self.min_depth) > 1):
                    return False
            else:
                # add child nodes (and their depths) to review lists
                if node.left:
                    self.nodes_and_depths_for_review.append(
                        (node.left, depth + 1))
                if node.right:
                    self.nodes_and_depths_for_review.append(
                        (node.right, depth + 1))
        return True
