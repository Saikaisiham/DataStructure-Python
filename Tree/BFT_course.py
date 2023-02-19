class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bft(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(bft(root))
