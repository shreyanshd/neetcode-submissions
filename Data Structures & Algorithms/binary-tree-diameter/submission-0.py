# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        res = 0
        while q:
            node = q.popleft()
            d = self.depth(node.left) + self.depth(node.right)
            res = max(res, d)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res            
    

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))