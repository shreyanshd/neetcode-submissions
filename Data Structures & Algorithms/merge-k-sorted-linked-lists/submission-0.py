# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = [node for node in lists]
        dummy = merged = ListNode()
        while k:
            minNode = self.popMin(k)
            if minNode.next:
                k.append(minNode.next)
            merged.next = minNode
            merged = merged.next
        return dummy.next

    def popMin(self, k: List[Optional[ListNode]]) -> ListNode:
        minVal = math.inf
        minIndex = 0
        for i, node in enumerate(k):
            if node.val < minVal:
                minVal = node.val
                minIndex = i
        k[minIndex], k[-1] = k[-1], k[minIndex]
        return k.pop()