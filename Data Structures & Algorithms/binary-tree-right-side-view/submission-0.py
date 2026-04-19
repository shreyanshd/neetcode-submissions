# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = deque()
        q.append(root)
        while q:
            cnt = len(q)
            elem = None
            for _ in range(cnt):
                elem = q.popleft()
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            result.append(elem.val)
        return result