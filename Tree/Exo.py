class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    # def bubbleSort(nums):
    #     c = 0
    #     check = True
    #     for i in range(len(nums)-1): 
    #         for j in range(len(nums)-i-1):
    #             if nums[j] > nums[j+1]:
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]
    #                 check = False

    #             c += 1
    #         if check: 
    #             break 

    @staticmethod
    def converttoTree(nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = Node(nums[mid])
        root.left = Node.converttoTree(nums[:mid])
        root.right = Node.converttoTree(nums[mid + 1:])
        return root

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

def targetDepth(root, target):
    if not root:
        return -1
    q = [(root, 1)]
    level = 0
    while q:
        for i in range(len(q)):
            node, level = q.pop(0)
            if node.val == target:
                return level
            if node.left and node.left.val == target:
                return level + 1
            if node.right and node.right.val == target:
                return level + 1
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
    return -1

nums = [1, 10, 3, 4, 5, 6, 66, 11, 9, 34, 88, 44, 90, 89, 7]
Node.bubbleSort(nums)
root = Node.converttoTree(nums)
print(targetDepth(root, 66))
