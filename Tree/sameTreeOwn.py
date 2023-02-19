# T,M = O(n)

class Node :

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bft(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    q1 = [root1]
    q2 = [root2]

    while q1 and q2:
        node1 = q1.pop(0)
        node2 = q2.pop(0)

        if node1.value != node2.value:
                return False

        if node1.left and node2.left:
            q1.append(node1.left)
            q2.append(node2.left)
        elif node1.left or node2.left:
            return False

        if node1.right and node2.right:
            q1.append(node1.right)
            q2.append(node2.right)
        elif node1.right or node2.right:
            return False

    return True


root1 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
root2 = Node(8, Node(9, Node(19), Node(5)), Node(3, Node(6), Node(7)))

result = bft(root1, root2)
print(result)
