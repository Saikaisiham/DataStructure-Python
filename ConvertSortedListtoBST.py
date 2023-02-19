class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = build_bst(nums[:mid])
    root.right = build_bst(nums[mid+1:])
    return root
