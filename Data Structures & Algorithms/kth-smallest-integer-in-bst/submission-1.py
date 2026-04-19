# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node, elems):
            if not node:
                return
            inorder(node.left, elems)
            elems.append(node.val)
            inorder(node.right, elems)

        elems = []
        inorder(root, elems)
        return elems[k-1]       
