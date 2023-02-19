class Tree:
    def __init__(self, right=None, left=None):
        self.right = right
        self.left = left

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node):
        if not node:
            return True

        lh = self.height(node.left)
        rh = self.height(node.right)

        if abs(lh - rh) <= 1 and self.is_balanced(node.left) and self.is_balanced(node.right):
            return True

        return False

# Define a binary tree
root = Tree(Tree(Tree(), Tree()), Tree(Tree(Tree(), Tree())))

# Check if the tree is balanced
print(root.is_balanced(root))  # Output: True