# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {n: i for i, n in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            
            val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(val)
            k = index[val]
            root.left = dfs(l, k-1)
            root.right = dfs(k+1, r)
            return root
        
        return dfs(0, len(inorder) - 1)