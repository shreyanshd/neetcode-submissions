# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val

        def dfs(node):
            if not node:
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0,  dfs(node.right))

            self.maxPath = max(self.maxPath, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return self.maxPath
