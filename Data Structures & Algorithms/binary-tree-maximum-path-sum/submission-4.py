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
            
            left_sum = getMaxSum(node.left)
            right_sum = getMaxSum(node.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

            s = node.val + max(left_sum, right_sum)
            self.max_sum = max(self.max_sum, s)
            return s

        getMaxSum(root)
        return self.max_sum