class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dft_inorder(node, result):
    if node:
        dft_inorder(node.left, result)
        result.append(node.value)
        dft_inorder(node.right, result)

def dft(root):
    result = []
    dft_inorder(root, result)
    return result


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
result = dft(root)
print(result)


[4, 2, 5, 1, 6, 3, 7]