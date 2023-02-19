class Node :
    def __init__(self, value, right=None, left=None):
        self.value = value 
        self.right = right
        self.left = left

def is_symmetric(left_subtree, right_subtree):
    if not left_subtree and not right_subtree:
        return True
    if not left_subtree or not right_subtree:
        return False
    if left_subtree.value != right_subtree.value:
        return False
    return is_symmetric(left_subtree.left, right_subtree.right) and is_symmetric(left_subtree.right, right_subtree.left)

def is_symmetric_tree(root):
    if not root:
        return True
    return is_symmetric(root.left, root.right)

root = Node(1, Node(2), Node(2, Node(4), Node(3)))

result = is_symmetric_tree(root)
print(result)
