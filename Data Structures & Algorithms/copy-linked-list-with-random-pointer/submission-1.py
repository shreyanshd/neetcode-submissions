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
            clone.next = nodeMap.get(node.next, None)
            clone.random = nodeMap.get(node.random, None)
            node = node.next
        
        return nodeMap[head]
        


