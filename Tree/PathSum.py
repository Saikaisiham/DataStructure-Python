# gives a target and searching for the sum of nodes tha equal to sum
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def pathSum(node,curSum):
            if not node :
                return False

            curSum += node.val

            if not node.left and not node.right:
                return curSum == targetSum

            return (pathSum(node.left,curSum) or 
            pathSum(node.right,curSum))
        
        return pathSum(root,0)
