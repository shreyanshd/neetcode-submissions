# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder, inorder):
            if not preorder or len(preorder) == 0:
                return None
            
            val = preorder[0]
            idx = inorder.index(val)
            root = TreeNode(val)
            root.left = build(preorder[1:idx+1], inorder[0:idx])
            root.right = build(preorder[idx+1:], inorder[idx+1:])
            return root
        
        return build(preorder, inorder)
