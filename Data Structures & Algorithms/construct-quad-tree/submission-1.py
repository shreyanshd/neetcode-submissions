"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(i, j, n):
            if n == 1:
                val = grid[i][j] == 1
                return Node(val=val, isLeaf=True)
            
            n = n // 2
            topLeft = dfs(i, j, n)
            topRight = dfs(i, j + n, n)
            bottomLeft = dfs(i + n, j, n)
            bottomRight = dfs(i + n, j + n, n)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                val = topLeft.val
                node = Node(val=val, isLeaf=True)
            else:
                node = Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
            
            return node
        
        n = len(grid)
        return dfs(0, 0, n)
