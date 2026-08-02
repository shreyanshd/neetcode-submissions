# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validBST(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return (
                validBST(node.left, lo, node.val) and
                validBST(node.right, node.val, hi)
            )
        
        return validBST(root, float('-inf'), float('inf'))
