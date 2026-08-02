# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def dfs(node, canRob):
            if not node:
                return 0

            if (node, canRob) in cache:
                return cache[(node, canRob)]

            r1, r2 = 0, 0
            if canRob:
                r1 = node.val
                r1 += dfs(node.left, False)
                r1 += dfs(node.right, False)
            
            r2 = dfs(node.left, True) + dfs(node.right, True)
            cache[(node, canRob)] = max(r1, r2)
            return cache[(node, canRob)]
        
        return dfs(root, True)