class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def minDepth(self, root):
        if not root:
            return 0

        q = [(root, 1)]

        while q:
            node, depth = q.pop(0)

            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth+1))

            if node.right:
                q.append((node.right, depth+1))

        return 0


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(root.minDepth(root))  
