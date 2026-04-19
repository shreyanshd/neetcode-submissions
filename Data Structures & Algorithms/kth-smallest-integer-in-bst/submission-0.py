# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def preorder(node, elems):
            if not node:
                return
            preorder(node.left, elems)
            elems.append(node.val)
            preorder(node.right, elems)

        elems = []
        preorder(root, elems)
        return elems[k-1]       
