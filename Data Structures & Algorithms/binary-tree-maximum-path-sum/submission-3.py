# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def getMaxSum(node):
            if not node:
                return float('-inf')
            
            s = node.val
            left_sum = getMaxSum(node.left)
            right_sum = getMaxSum(node.right)
            self.max_sum = max(self.max_sum, left_sum, right_sum, s + left_sum + right_sum)

            if max(left_sum, right_sum) > 0:
                s += max(left_sum, right_sum)
            
            self.max_sum = max(self.max_sum, s)
            return s

        getMaxSum(root)
        return self.max_sum