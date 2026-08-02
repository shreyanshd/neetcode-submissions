# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def dfs(node):
            if not node:
                return float('-inf')
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            self.maxPath = max(self.maxPath, leftSum, rightSum)

            curr = node.val
            if leftSum > 0 and rightSum > 0:
                self.maxPath = max(self.maxPath, curr + leftSum + rightSum)
                curr += max(leftSum, rightSum)
            elif leftSum > 0:
                self.maxPath = max(self.maxPath, curr + leftSum)
                curr += leftSum
            elif rightSum > 0:
                self.maxPath = max(self.maxPath, curr + rightSum)
                curr += rightSum
            else:
                self.maxPath = max(self.maxPath, curr)
            
            return curr
        
        dfs(root)
        return 0 if self.maxPath == float('-inf') else self.maxPath
