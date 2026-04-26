"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        def clone(node):
            if node in nodeMap:
                return nodeMap[node]
            
            copy = Node(node.val)
            nodeMap[node] = copy
            for m in node.neighbors:
                copy.neighbors.append(clone(m))
            
            return copy
        
        return clone(node) if node else None


        