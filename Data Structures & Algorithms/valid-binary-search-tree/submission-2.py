# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(node, minVal, maxVal):
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return (
                checkBST(node.left, minVal, node.val) and
                checkBST(node.right, node.val, maxVal)
            )
        
        return checkBST(root, float('-inf'), float('inf'))