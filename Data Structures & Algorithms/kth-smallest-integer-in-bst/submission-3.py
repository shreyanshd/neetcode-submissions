# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def count(node):
            if not node: return 0
            return 1 + count(node.left) + count(node.right)
        
        leftCount = count(root.left)
        if k <= leftCount:
            return self.kthSmallest(root.left, k)
        elif k == leftCount + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - leftCount - 1)
        