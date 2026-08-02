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
        def checkGrid(i, j, n):
            isLeaf = True
            val = grid[i][j]
            for x in range(i, i + n):
                for y in range(j, j + n):
                    if grid[x][y] != val:
                        isLeaf = False
                        break
            return (isLeaf, val)

        def getNode(i, j, n):
            isLeaf, val = checkGrid(i, j, n)
            if isLeaf:
                return Node(
                    val=val,
                    isLeaf=True,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )
            else:
                n = n // 2
                return Node(
                    val=val,
                    isLeaf=False,
                    topLeft=getNode(i, j, n),
                    topRight=getNode(i, j + n, n),
                    bottomLeft=getNode(i + n, j, n),
                    bottomRight=getNode(i + n, j + n, n)
                )
        
        n = len(grid)
        return getNode(0, 0, n)