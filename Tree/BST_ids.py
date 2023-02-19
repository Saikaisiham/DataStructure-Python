class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if not curr.left:
                        curr.left = Node(val)
                        break
                    else:
                        curr = curr.left
                else:
                    if not curr.right:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right
                        
    def delete(self, val):
        if not self.root:
            return
        else:
            # search for val
            parent = None
            curr = self.root
            while curr and curr.val != val:
                parent = curr
                if val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
            if not curr:
                return

            # If the node with value val is found, the method checks if the node has a left child. If it does not 
            # have a left child, the method simply deletes the node by replacing it with its right child (if it has one).
            if not curr.left:
                if not parent:
                    self.root = curr.right
                elif curr.val < parent.val:
                    parent.left = curr.right
                else:
                    parent.right = curr.right
            elif not curr.right:
                if not parent:
                    self.root = curr.left
                elif curr.val < parent.val:
                    parent.left = curr.left
                else:
                    parent.right = curr.left
            # If the node with value val has both a left and right child, the method finds the successor of the node 
            # (i.e., the node with the smallest value in its right subtree). It then replaces the value of the node with 
            # the value of its successor
            # and deletes the successor node (which can be done recursively using the delete method).
            else:
                successor = curr.right
                while successor.left:
                    successor = successor.left
                curr.val = successor.val
                self.delete(successor.val)
                
    def search(self, val):
        curr = self.root
        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
