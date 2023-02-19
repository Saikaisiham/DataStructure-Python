from typing import List

class Node :
    def __init__(self, value, right=None, left=None):
        self.value = value 
        self.right = right
        self.left = left


def bft(self,root):

    # if not root :
    #     return 0

    # q = [root]
    # level = 0

    # while q :
    #     for i in range(len(q)) :
    #         node = q.pop(0)

    #         if node.left :
    #             q.append(node.left)
    #         if node.right : 
    #             q.append(node.right)

    #     level += 1
    # return level

    if not root :
        return 0

    return 1 + max (self.bft(node.left),self.bft(node.right))

root = Node(8, Node(3), Node(3, Node(6), Node(7)))

result = bft(root)
print(result)
