# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0

        def dfs(node: TreeNode, maxVal: int):
            if not node:
                return
            if node.val >= maxVal:
                self.total += 1
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        if not root:
            return 0
        dfs(root, root.val)
        return self.total