# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root):
        if not root :
            return 0

        q = [root]

        level = 0

        while q :
            for i in range(len(q)):
                node = q.pop(0)

                if node.left :
                    q.append(node.left)

                if node.right : 
                    q.append(node.right)

            level += 1

        return level


# Define a binary tree
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

# Get the maximum depth of the tree
print(root.maxDepth(root))  # Output: 3 