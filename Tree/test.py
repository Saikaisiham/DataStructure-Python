class Tree :
    def __init__(self,right=None,left=None):
         
        self.right = right 
        self.left = left 

    def height(self,node):
        if not node :
            return False

        return 1+max(self.height(node.left),self.height(node.right))

    def is_Balanced(node):
        if not node :
            return True

        right_height = self.height(node.right)
        left_height = self.height(node.left)

        if abs(left_height - right_height) <= 1 and self.is_Balanced(node.left) and self.is_Balanced(node.right):
            return True

        return False


root = Tree(Tree(Tree(), Tree()), Tree(Tree(Tree(), Tree())))

# Check if the tree is balanced
print(root.is_Balanced(root)) 
