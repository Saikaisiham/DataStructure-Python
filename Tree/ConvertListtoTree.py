class Node:
    def __init__(self, val, right=None, left=None):
        self.right = right
        self.left = left
        self.val = val

    def builds(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = Node(nums[mid])
        root.left = self.builds(nums[:mid])
        root.right = self.builds(nums[mid + 1:])

        return root

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

root = Node(0)
nums = [1, 2, 3, 4, 5, 6, 7]
root = root.builds(nums)
root.inorder()
