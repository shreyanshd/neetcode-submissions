"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        nodeMap = {}
        node = head
        while node:
            clone = Node(node.val)
            nodeMap[node] = clone
            node = node.next

        node = head
        while node:
            clone = nodeMap[node]
            cloneNext = nodeMap.get(node.next, None)
            cloneRandom = nodeMap.get(node.random, None)
            clone.next = cloneNext
            clone.random = cloneRandom
            node = node.next
        
        return nodeMap[head]
        


