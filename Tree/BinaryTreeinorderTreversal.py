class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dft_inorder(root, result)
        return result

    def dft_inorder(self, node, result):
        if node:
            self.dft_inorder(node.left, result)
            result.append(node.val)
            self.dft_inorder(node.right, result)